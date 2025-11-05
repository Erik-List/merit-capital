#!/usr/bin/env ts-node

import 'dotenv/config'
import { Client as PgClient } from 'pg'
import { createClient as createSupabaseClient } from '@supabase/supabase-js'

type Flags = {
  replace: boolean
  investors: string[] | null
}

function parseFlags(argv: string[]): Flags {
  const flags: Flags = { replace: false, investors: null }
  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i]
    if (arg === '-replace' || arg === '--replace') {
      flags.replace = true
    } else if (arg === '-investor' || arg === '--investor') {
      const next = argv[i + 1]
      if (!next || next.startsWith('-')) {
        throw new Error('Expected a comma-separated list after -investor')
      }
      flags.investors = next.split(',').map(s => s.trim()).filter(Boolean)
      i++
    }
  }
  return flags
}

type InvestorRow = {
  id: string
  name: string
  slug: string
  investment_concept: string | null
  history: string | null
  icon_url: string | null
}

async function main() {
  const { replace, investors } = parseFlags(process.argv)

  const DATABASE_URL = process.env.DATABASE_URL
  const OPENAI_API_KEY = process.env.OPENAI_API_KEY
  const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL
  const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
  const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY

  if (!DATABASE_URL) throw new Error('Missing DATABASE_URL in environment')
  if (!OPENAI_API_KEY) throw new Error('Missing OPENAI_API_KEY in environment')
  if (!SUPABASE_URL) throw new Error('Missing NEXT_PUBLIC_SUPABASE_URL in environment')
  if (!SUPABASE_ANON_KEY && !SUPABASE_SERVICE_ROLE_KEY) throw new Error('Provide either NEXT_PUBLIC_SUPABASE_ANON_KEY or SUPABASE_SERVICE_ROLE_KEY in environment')

  const pg = new PgClient({ connectionString: DATABASE_URL })
  await pg.connect()

  const supabaseKey = (SUPABASE_SERVICE_ROLE_KEY || SUPABASE_ANON_KEY) as string
  const supabase = createSupabaseClient(SUPABASE_URL, supabaseKey)

  // 1) Fetch investors
  const whereParts: string[] = []
  const values: any[] = []
  let paramIndex = 1
  if (!replace) {
    whereParts.push('(icon_url IS NULL OR icon_url = \'\')')
  }
  if (investors && investors.length > 0) {
    whereParts.push(`slug = ANY($${paramIndex}::text[])`)
    values.push(investors)
    paramIndex++
  }
  const whereSql = whereParts.length > 0 ? 'WHERE ' + whereParts.join(' AND ') : ''
  const query = `
    SELECT id, name, slug, investment_concept, history, icon_url
    FROM "public"."Investor"
    ${whereSql}
    ORDER BY slug ASC
  `
  const { rows } = await pg.query<InvestorRow>(query, values)

  if (rows.length === 0) {
    console.log('No investors matched criteria. Nothing to do.')
    await pg.end()
    return
  }

  console.log(`Processing ${rows.length} investor(s)${replace ? ' with replace' : ''}${investors ? ` [${investors.join(', ')}]` : ''}`)

  for (const investor of rows) {
    try {
      // 2) Generate image 256x256 PNG via gpt-image-1
      const prompt = `create a logo (fav)icon for vc a investor: ${investor.name}\n\n` +
        `here is a description of the Investor: ${investor.investment_concept ?? ''}\n\n` +
        `Further information: ${investor.history ?? ''}\n\n` +
        `- square image \n- have a single-tone color background that matches with the logo \n- only include the icon and no text \n- logo fills image, but has 1/4 of space padding to each side`

      const resp = await (globalThis as any).fetch('https://api.openai.com/v1/images/generations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          model: 'gpt-image-1',
          prompt,
          n: 1,
          size: '1024x1024',
          output_format: 'png',
          background: 'opaque'
        }),
      })
      if (!resp.ok) {
        const txt = await resp.text()
        throw new Error(`OpenAI image generation failed (${resp.status}): ${txt}`)
      }
      const data = await resp.json() as { data: { b64_json: string }[] }
      const b64 = data?.data?.[0]?.b64_json
      if (!b64) throw new Error('No image data returned from OpenAI')
      const buffer = Buffer.from(b64, 'base64')

      // 3) Upload to Supabase Storage bucket "Icon Images"
      const filePath = `investors/${investor.slug}.png`
      // Remove existing when replace true
      if (replace) {
        await supabase.storage.from('Icon Images').remove([filePath])
      }
      const { error: uploadError } = await supabase.storage
        .from('Icon Images')
        .upload(filePath, buffer, { contentType: 'image/png', upsert: replace })
      if (uploadError && uploadError.message && !uploadError.message.includes('The resource already exists')) {
        throw uploadError
      }

      const { data: publicUrlData } = supabase.storage.from('Icon Images').getPublicUrl(filePath)
      const publicUrl = publicUrlData.publicUrl

      // 4) Update Investor.icon_url
      await pg.query(
        `UPDATE "public"."Investor" SET icon_url = $1, updated_at = now() WHERE id = $2`,
        [publicUrl, investor.id]
      )

      console.log(`Updated ${investor.slug} -> ${publicUrl}`)
    } catch (err: any) {
      console.error(`Failed processing ${investor.slug}:`, err?.message || err)
    }
  }

  await pg.end()
}

main().catch(err => {
  console.error(err)
  process.exit(1)
})


