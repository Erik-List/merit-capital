import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  return NextResponse.redirect(new URL('/', request.url), 308);
}

export async function HEAD(request: Request) {
  return NextResponse.redirect(new URL('/', request.url), 308);
}


