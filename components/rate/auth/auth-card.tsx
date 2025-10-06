import { Card, CardTitle, CardHeader, CardDescription, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"
import { AuthButtons } from "./auth-buttons"
import { createClient } from "@/utils/supabase/server"
import { cookies } from 'next/headers'

interface AuthCardProps extends React.ComponentProps<typeof Card> {
  isLoading?: boolean;
}

export async function AuthCard({ 
  className, 
  isLoading = false,
  ...props 
}: AuthCardProps) {
  const cookieStore = await cookies()
  const supabase = createClient(cookieStore)
  const { data: { user } } = await supabase.auth.getUser()
  
  const authState = {
    isAuthenticated: !!user,
    provider: user ? 'linkedin' as const : undefined,
    userEmail: user?.email
  }

  if (isLoading) {
    return (
      <Card className={cn("w-full", className)} {...props}>
        <CardHeader>
          <div className="h-7 w-48 bg-muted rounded animate-fast-pulse" />
          <div className="h-10 w-full bg-muted rounded animate-fast-pulse mt-2" />
        </CardHeader>
        <CardContent>
          <div className="space-y-6">
            <div className="space-y-4">
              <div className="flex gap-4">
                <div className="h-12 flex-1 bg-muted rounded animate-fast-pulse" />
                <div className="h-12 flex-1 bg-muted rounded animate-fast-pulse" />
              </div>
            </div>
            <div className="h-4 w-72 mx-auto bg-muted rounded animate-fast-pulse" />
          </div>
        </CardContent>
      </Card>
    )
  }

  return (
    <Card className={cn("w-full", className)} {...props}>
      <CardHeader>
        <CardTitle>Verify Your Identity</CardTitle>
        <CardDescription>
          Authenticate yourself to provide honest investor feedback to help your fellow founders choose their investors
          more wisely.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          <AuthButtons 
            isAuthenticated={authState.isAuthenticated}
            provider={authState.provider}
            userEmail={authState.userEmail}
          />
          <div className="text-sm text-muted-foreground text-center">
            <a href="#" className="underline">
              See how we anonymize & encrypt your data
            </a>
          </div>
        </div>
      </CardContent>
    </Card>
  )
} 