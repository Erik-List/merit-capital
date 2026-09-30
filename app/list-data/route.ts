import { NextResponse } from 'next/server';
import { loadListData, REVALIDATE_SECONDS } from '@/lib/list-data';

// The investor list's one data request: the slim investor rows plus every
// company as a packed number group (lib/list-data.ts). Dynamic, so a failed
// upstream read is answered as an error and never cached as a page; the
// upstream pages and the edge both hold a good answer for REVALIDATE_SECONDS.

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    const data = await loadListData();
    return NextResponse.json(data, {
      headers: {
        'Cache-Control': `public, s-maxage=${REVALIDATE_SECONDS}, stale-while-revalidate=${REVALIDATE_SECONDS * 6}`,
      },
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: 'Upstream data service unreachable' }, { status: 502 });
  }
}
