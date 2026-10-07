import { NextResponse } from 'next/server';
import { z } from 'zod';
import { INVESTOR_NAME_MAX } from '@/lib/investor-requests';

// The "Request an Investor" form of the index posts here. The request is
// stored in public.investor_requests with the service role (the public holds
// no write grant on it), then emailed to Erik through Resend. Stored means
// done: a failed email is logged and does not fail the request, because the
// row is on record.

export const dynamic = 'force-dynamic';

const NOTIFY_TO = 'erik@meritcapit.al';
// Resend's shared sender: without a verified domain it delivers to the
// account's own address only, which is the one recipient here.
const NOTIFY_FROM = 'Merit Capital <onboarding@resend.dev>';

const requestSchema = z.object({
  email: z.string().trim().email().max(254),
  investor: z.string().trim().min(1).max(INVESTOR_NAME_MAX),
  // Hidden in the form; only a script fills it.
  website: z.string().optional(),
});

async function store(email: string, investor: string): Promise<void> {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY!;
  const response = await fetch(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest/v1/investor_requests`, {
    method: 'POST',
    headers: {
      apikey: serviceKey,
      Authorization: `Bearer ${serviceKey}`,
      'Content-Type': 'application/json',
      Prefer: 'return=minimal',
    },
    body: JSON.stringify({ email, investor_name: investor }),
    cache: 'no-store',
  });
  if (!response.ok) {
    throw new Error(`investor_requests answered ${response.status}`);
  }
}

async function notify(email: string, investor: string): Promise<void> {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) throw new Error('RESEND_API_KEY is not set');
  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: NOTIFY_FROM,
      to: [NOTIFY_TO],
      reply_to: email,
      subject: `Investor request: ${investor}`,
      text: `Investor: ${investor}\nRequested by: ${email}\n\nFiled through the index. Reply to this email to answer the requester.`,
    }),
    cache: 'no-store',
  });
  if (!response.ok) {
    throw new Error(`Resend answered ${response.status}: ${await response.text()}`);
  }
}

export async function POST(request: Request) {
  const parsed = requestSchema.safeParse(await request.json().catch(() => null));
  if (!parsed.success) {
    return NextResponse.json({ error: 'A valid email and an investor name are required' }, { status: 400 });
  }
  const { email, investor, website } = parsed.data;
  // A filled hidden field is a script: answer as if stored, keep nothing.
  if (website) return NextResponse.json({ ok: true });

  try {
    await store(email, investor);
  } catch (error) {
    console.error('Failed to store the investor request', error);
    return NextResponse.json({ error: 'The request could not be stored' }, { status: 502 });
  }

  try {
    await notify(email, investor);
  } catch (error) {
    console.error('Investor request stored, but the email was not sent', error);
  }
  return NextResponse.json({ ok: true });
}
