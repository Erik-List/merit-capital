"use client"

import { useEffect, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { AuthButtons } from "@/components/rate/auth/auth-buttons"
import { Button } from "@/components/ui/button"

export function AuthSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded }: SlideProps) {
  const [mockAuthenticated, setMockAuthenticated] = useState(false)
  const [mockEmail] = useState("founder@example.com")
  const [mockProvider] = useState<"linkedin" | "x">("linkedin")

  useEffect(() => {
    setControlsVisible(false)
    setProgressVisible(true)
    setProgressIncluded(true)
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
            <>
              <AuthButtons isAuthenticated={false} />
              <div className="text-sm text-muted-foreground text-center">
                <button className="underline" onClick={() => setMockAuthenticated(true)}>
                  Use placeholder identity ({mockEmail})
                </button>
              </div>
            </>
          ) : (
            <div className="space-y-3">
              <AuthButtons isAuthenticated={true} provider={mockProvider} userEmail={mockEmail} />
              <Button variant="outline" onClick={() => setMockAuthenticated(false)}>Disconnect mock</Button>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}


