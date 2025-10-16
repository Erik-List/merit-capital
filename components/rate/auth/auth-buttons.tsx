"use client"

import * as React from "react"
import { Button } from "@/components/ui/button"
import { LinkedinLogo, XLogo } from "@phosphor-icons/react"
import { LockClosedIcon } from "@radix-ui/react-icons"
import { useToast } from "@/hooks/use-toast"
import { createClient } from "@/utils/supabase/client"

interface AuthButtonsProps {
  provider?: 'linkedin' | 'x'
  isAuthenticated: boolean
  userEmail?: string
  mockState?: boolean
  onDisconnect?: () => void
}

export function AuthButtons({ 
  provider,
  isAuthenticated,
  userEmail,
  mockState = false,
  onDisconnect,
}: AuthButtonsProps) {
  const { toast } = useToast()
  const [linkedInLoading, setLinkedInLoading] = React.useState(false)
  const [xLoading, setXLoading] = React.useState(false)
  const supabase = createClient()

  const handleLinkedInAuth = async () => {
    try {
      setLinkedInLoading(true)
      const currentPath = window.location.pathname
      const { error } = await supabase.auth.signInWithOAuth({
        provider: 'linkedin_oidc',
        options: {
          redirectTo: `${window.location.origin}/auth/callback?next=${currentPath}`,
        },
      })
      
      if (error) throw error
    } catch (error) {
      console.error('Error initiating auth:', error)
      toast({
        title: "Authentication Failed",
        description: "Please try again or use a different method",
        variant: "destructive",
      })
    } finally {
      setLinkedInLoading(false)
    }
  }

  const handleSignOut = async () => {
    try {
      if (mockState) {
        onDisconnect?.()
        return
      }
      const { error } = await supabase.auth.signOut()
      if (error) throw error
      window.location.reload()
      toast({ title: "Successfully disconnected", description: "Your account has been unlinked" })
    } catch (error) {
      console.error('Error signing out:', error)
      toast({
        title: "Error disconnecting",
        description: "Please try again",
        variant: "destructive",
      })
    }
  }

  const handleXAuth = async () => {
    try {
      setXLoading(true)
      const currentPath = window.location.pathname
      const { error } = await supabase.auth.signInWithOAuth({
        provider: 'twitter',
        options: {
          redirectTo: `${window.location.origin}/auth/callback?next=${currentPath}`,
        },
      })
      
      if (error) throw error
    } catch (error) {
      console.error('Error initiating auth:', error)
      toast({
        title: "Authentication Failed",
        description: "Please try again or use a different method",
        variant: "destructive",
      })
    } finally {
      setXLoading(false)
    }
  }

  if (isAuthenticated && provider) {
    const Icon = provider === 'linkedin' ? LinkedinLogo : XLogo
    const text = provider === 'linkedin' ? "Connected via LinkedIn" : "Connected via X"

    return (
      <div className="rounded-lg border glass divide-y">
        <div className="p-3 flex items-center justify-center space-x-2">
          <Icon weight="regular" className="h-5 w-5 text-success" />
          <span className="font-medium">{text}</span>
          {userEmail && (
            <span className="text-sm text-muted-foreground">
              ({userEmail})
            </span>
          )}
        </div>
        <Button 
          variant="ghost" 
          className="w-full p-3 h-auto flex items-center justify-center space-x-2 text-muted-foreground hover:text-destructive"
          onClick={handleSignOut}
        >
          <LockClosedIcon className="h-4 w-4" />
          <span className="font-medium">Disconnect Account</span>
        </Button>
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <div className="flex gap-4">
        <Button 
          variant="outline" 
          size="icon"
          className="flex-1 h-12"
          onClick={handleLinkedInAuth}
          disabled={linkedInLoading || xLoading}
        >
          <LinkedinLogo 
            className="h-6 w-6"
            weight="regular"
          />
          <span className="sr-only">Sign in with LinkedIn</span>
        </Button>
        <Button 
          variant="outline" 
          size="icon"
          className="flex-1 h-12"
          onClick={handleXAuth}
          disabled={linkedInLoading || xLoading}
        >
          <XLogo 
            className="h-6 w-6"
            weight="regular"
          />
          <span className="sr-only">Sign in with X</span>
        </Button>
      </div>
    </div>
  )
} 

