import { NextRequest, NextResponse } from 'next/server';
import { getPublicSpec } from '@/lib/public-spec';

// Public read proxy for the investor dataset.
//
// Forwards GET /data/* to the Supabase PostgREST endpoint and injects the anon
// key server-side, so agents and humans can query the data with zero headers:
//
//   GET /data/investors?investor_type=eq.Individual&order=name&limit=20
//
// GET /data (no path) returns the live OpenAPI spec that PostgREST generates
// from the database catalog, with the server URL rewritten to this proxy so
// docs and agent frameworks see the branded base URL. The spec, including all
// COMMENT ON descriptions, auto-updates with every schema change.
//
// Only GET is exported: the surface is read-only regardless of DB grants.

export const dynamic = 'force-dynamic';

// Request headers PostgREST uses that are safe to pass through on reads.
const FORWARDED_REQUEST_HEADERS = ['accept', 'accept-profile', 'range', 'range-unit', 'prefer'];

// Response headers worth surfacing (pagination info lives in content-range).
const FORWARDED_RESPONSE_HEADERS = ['content-type', 'content-range', 'content-profile'];

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ path?: string[] }> }
) {
  const { path } = await params;
  const segments = path ?? [];

  // Root path: serve the live OpenAPI spec, filtered to the public surface
  // and with the server URL rewritten from the Supabase host to this proxy.
  if (segments.length === 0) {
    const spec = await getPublicSpec();
    if (!spec) {
      return NextResponse.json(
        { error: 'Upstream data service unreachable' },
        { status: 502 }
      );
    }
    const origin = new URL(request.nextUrl.origin);
    // PostgREST emits OpenAPI 2.0 (swagger), which uses host + basePath.
    spec.host = origin.host;
    spec.basePath = '/data';
    spec.schemes = [origin.protocol.replace(':', '')];
    return NextResponse.json(spec);
  }

  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
  // Data requests use the anon key so database grants remain the access gate.
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

  const upstream = new URL(`${supabaseUrl}/rest/v1/${segments.join('/')}`);
  upstream.search = request.nextUrl.search;

  const headers: Record<string, string> = {
    apikey: anonKey,
    Authorization: `Bearer ${anonKey}`,
  };
  for (const name of FORWARDED_REQUEST_HEADERS) {
    const value = request.headers.get(name);
    if (value) headers[name] = value;
  }

  let response: Response;
  try {
    response = await fetch(upstream, { headers, cache: 'no-store' });
  } catch {
    return NextResponse.json(
      { error: 'Upstream data service unreachable' },
      { status: 502 }
    );
  }

  const responseHeaders = new Headers();
  for (const name of FORWARDED_RESPONSE_HEADERS) {
    const value = response.headers.get(name);
    if (value) responseHeaders.set(name, value);
  }

  return new NextResponse(response.body, {
    status: response.status,
    headers: responseHeaders,
  });
}
