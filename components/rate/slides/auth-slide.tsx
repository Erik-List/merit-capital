"use client"

import { useEffect, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { AuthButtons } from "@/components/rate/auth/auth-buttons"

export function AuthSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded, onBack }: SlideProps) {
  const [mockAuthenticated, setMockAuthenticated] = useState(true)
  const [mockEmail] = useState("founder@example.com")
  const [mockProvider] = useState<"linkedin" | "x">("linkedin")

  useEffect(() => {
    setControlsVisible(true)
    setProgressVisible(false)
    setProgressIncluded(false)
    setCanProceed(mockAuthenticated)
  }, [mockAuthenticated, setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded])

  return (
    <div className="space-y-5">
      <Card className="border border-input/30">
        <CardHeader>
          <CardTitle>Verify Your Identity</CardTitle>
          <CardDescription>
            Authenticate to provide honest investor feedback that helps founders choose wisely.
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {!mockAuthenticated ? (
            <AuthButtons isAuthenticated={false} />
          ) : (
            <div className="space-y-3">
              <AuthButtons isAuthenticated={true} provider={mockProvider} userEmail={mockEmail} mockState onDisconnect={() => { setMockAuthenticated(false); setCanProceed(false); onBack(); }} />
              <div className="text-xs text-muted-foreground text-center">Connected (demo)</div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}


