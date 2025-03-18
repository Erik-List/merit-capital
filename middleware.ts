import { type NextRequest, NextResponse } from 'next/server'
import { updateSession } from '@/utils/supabase/middleware'

// Configuration for idea validation phase
const IDEA_VALIDATION_ENABLED = true // You can toggle this with an environment variable later
const PUBLIC_PATHS = [
  '/investor',
  '/idea-validation',
  '/_next',
  '/api',
  '/static',
  '/favicon.ico',
]

function isPublicPath(pathname: string): boolean {
  return PUBLIC_PATHS.some(path => pathname.startsWith(path))
}

export async function middleware(request: NextRequest) {
  // First handle session update
  const response = await updateSession(request)
  
  if (IDEA_VALIDATION_ENABLED) {
    const pathname = request.nextUrl.pathname
    
    // Check if the current path should be redirected
    if (!isPublicPath(pathname)) {
      const redirectUrl = new URL('/idea-validation', request.url)
      return NextResponse.redirect(redirectUrl)
    }
  }

  return response
}

export const config = {
  matcher: [
    /*
     * Match specific routes we want to protect
     */
    '/',
    '/rate',
    '/leaderboard',
    '/logs',
    '/:path*'
  ]
} 