"use client"

import { useEffect } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Table, TableBody, TableRow, TableCell } from "@/components/ui/table"

export function InfoSlide({ setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded }: SlideProps) {
  useEffect(() => {
    setControlsVisible(false)
    setProgressVisible(false)
    setProgressIncluded(false)
    setCanProceed(true)
  }, [setCanProceed, setControlsVisible, setProgressVisible, setProgressIncluded])

  return (
    <div className="space-y-5">
      <div className="space-y-4">
        <div className="text-2xl font-medium">Preview how to rate your captable investors.</div>
        <div className="w-fit glass border border-input/30 rounded-md px-3 py-2 text-sm">3-7 minutes rating duration · 0-10 questions on multiple categories</div>
        <div className="inline-block rounded-md border border-input/30 overflow-hidden">
          <Table className="w-auto">
            <TableBody>
              <TableRow>
                <TableCell className="text-muted-foreground p-3 text-left">Investment Speed</TableCell>
                <TableCell className="text-muted-foreground p-3 text-left border-l border-input/30">Investment Process</TableCell>
              </TableRow>
              <TableRow>
                <TableCell className="text-muted-foreground p-3 text-left">Investor Brand</TableCell>
                <TableCell className="text-muted-foreground p-3 text-left border-l border-input/30">Company Building Support</TableCell>
              </TableRow>
              <TableRow>
                <TableCell className="text-muted-foreground p-3 text-left">Follow-on Commitment</TableCell>
                <TableCell className="text-muted-foreground p-3 text-left border-l border-input/30">Additional Considerations</TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </div>
      </div>
    </div>
  )
}


