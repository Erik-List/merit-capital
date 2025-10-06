import { AuthCard } from "@/components/rate/auth/auth-card"
import { RateForm } from "@/components/rate/rate-form"
import { createClient } from "@/utils/supabase/server"
import { cookies } from 'next/headers'

export default async function RatePage() {
  // Check auth state server-side
  const cookieStore = await cookies()
  const supabase = createClient(cookieStore)
  const { data: { user } } = await supabase.auth.getUser()
  
  // Get provider from user metadata or email domain
  const getProvider = () => {
    if (!user) return undefined
    // Check if user came from X OAuth
    if (user.app_metadata.provider === 'twitter') return 'x'
    // Check if user came from LinkedIn OAuth
    if (user.app_metadata.provider === 'linkedin_oidc') return 'linkedin'
    return undefined
  }
  
  const authState = {
    isAuthenticated: !!user,
    provider: getProvider(),
    userEmail: user?.email
  }

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-2xl mx-auto space-y-8">
          <h1 className="text-4xl font-bold">Rate an Investor</h1>
          <AuthCard />
          <RateForm />
        </div>
      </div>
    </div>
  )
}