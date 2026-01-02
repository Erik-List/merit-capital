"use client"

import React, { useEffect, useMemo, useState } from "react"
import type { SlideProps } from "../wizard/rating-wizard"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select"
import { X, PlusCircle } from "lucide-react"

export type Investor = { id: string; name: string; investor_type: "Institutional" | "Individual"; institutionName?: string; associatedInstitutionId?: string; affiliationType?: "Angel" | "Associated" }
type InstitutionRow = { kind: "institution"; investor: Investor }
type IndividualRow = { kind: "individual"; investor: Investor }
type Row = InstitutionRow | IndividualRow

type Props = SlideProps & {
  investors: Investor[]
  setInvestors: (next: Investor[]) => void
  // cleanup hooks for downstream rating state
  clearInvestorFromStates?: (ids: string[]) => void
}

type NewType = "Angel" | "Institution"

export function ListSlide({ setControlsVisible, setProgressVisible, setProgressIncluded, setCanProceed, onNext, investors, setInvestors, clearInvestorFromStates }: Props) {
  const [showForm, setShowForm] = useState(false)
  const [newType, setNewType] = useState<NewType>("Angel")
  const [personName, setPersonName] = useState("")
  const [institutionName, setInstitutionName] = useState("")

  useEffect(() => {
    setControlsVisible(false)
    setProgressVisible(false)
    setProgressIncluded(false)
    setCanProceed(true)
    return () => {}
  }, [setControlsVisible, setProgressVisible, setProgressIncluded, setCanProceed])

  const institutionalInvestors = useMemo(() => 
    investors.filter(i => i.investor_type === "Institutional"), 
    [investors]
  )
  
  const individualInvestors = useMemo(() => 
    investors.filter(i => i.investor_type === "Individual"), 
    [investors]
  )

  const pairs: Row[] = useMemo(() => {
    const institutionRows: InstitutionRow[] = institutionalInvestors.map(inv => ({ 
      kind: "institution", 
      investor: inv 
    }))
    const individualRows: IndividualRow[] = individualInvestors.map(inv => ({ 
      kind: "individual", 
      investor: inv 
    }))
    return [...institutionRows, ...individualRows]
  }, [institutionalInvestors, individualInvestors])

  const headline = useMemo(() => {
    if (pairs.length === 0) {
      return "Are these the investors on your captable?"
    }

    // Get display names - preserve original capitalization
    const getDisplayName = (row: Row): string => {
      if (row.kind === "institution") {
        return row.investor.institutionName || row.investor.name
      }
      return row.investor.name
    }

    const firstNames = pairs.slice(0, 2).map(getDisplayName)
    const remaining = Math.max(0, pairs.length - firstNames.length)

    const name1 = firstNames[0]
    
    if (pairs.length === 1) {
      // Single investor: "Is [name] an investor on your captable?"
      return `Is ${name1} an investor on your captable?`
    }

    if (pairs.length === 2) {
      // Two investors: "Are [name1] and [name2] investors on your captable?"
      const name2 = firstNames[1]
      return `Are ${name1} and ${name2} investors on your captable?`
    }

    // Three or more investors
    const name2 = firstNames[1]
    if (remaining === 1) {
      // Exactly 3: "Are [name1], [name2], and [name3] investors on your captable?"
      const name3 = getDisplayName(pairs[2])
      return `Are ${name1}, ${name2}, and ${name3} investors on your captable?`
    } else {
      // 4+: "Are [name1], [name2], and [X] more investors on your captable?"
      return `Are ${name1}, ${name2}, and ${remaining} more investors on your captable?`
    }
  }, [pairs])

  function removeInvestor(id: string) {
    const remaining = investors.filter(i => i.id !== id)
    setInvestors(remaining)
    clearInvestorFromStates?.([id])
  }

  const canAdd = useMemo(() => {
    if (newType === "Angel") return personName.trim().length > 0
    return personName.trim().length > 0 && institutionName.trim().length > 0
  }, [newType, personName, institutionName])

  function addInvestor() {
    if (!canAdd) return
    if (newType === "Angel") {
      const angel: Investor = { id: `ind-${cryptoRandom()}`, name: personName.trim(), investor_type: "Individual", affiliationType: "Angel" }
      setInvestors([...investors, angel])
    } else {
      const institution: Investor = { 
        id: `inst-${cryptoRandom()}`, 
        name: personName.trim(), 
        investor_type: "Institutional",
        institutionName: institutionName.trim()
      }
      setInvestors([...investors, institution])
    }
    setPersonName("")
    setInstitutionName("")
    setShowForm(false)
  }

  return (
    <div className="space-y-5">
      <div className="text-2xl font-medium">{headline}</div>

      <div className="grid grid-cols-1 md:grid-cols-[1fr_1px_1fr] gap-4">
        <div className="space-y-0">
          {pairs.filter((_, idx) => idx % 2 === 0).map((row: Row, idx) => {
            return (
            <div key={idx} className="flex items-center gap-2 border-b border-input/30 pb-0">
              <div className="min-w-0">
                {row.kind === "institution" ? (
                  <div className="leading-tight">
                    <div className="text-sm truncate">
                      {row.investor.name}{row.investor.institutionName ? ` with ${row.investor.institutionName}` : ''}
                    </div>
                  </div>
                ) : (
                  <div className="leading-tight">
                    <div className="text-sm truncate">{row.investor.name}</div>
                  </div>
                )}
              </div>
              <Button variant="link" className="p-0" onClick={() => removeInvestor(row.investor.id)}>
                <X className="h-3 w-3" />
              </Button>
            </div>
            )
          })}
          {!showForm ? (
            <div className="flex items-center gap-2 pb-0">
              <Button variant="link" className="p-0 text-sm" onClick={() => setShowForm(true)}>+ Add investors</Button>
            </div>
          ) : null}
        </div>

        <div className="w-px bg-input/50 hidden md:block" />

        <div className="space-y-0">
          {pairs.filter((_, idx) => idx % 2 === 1).map((row: Row, idx) => {
            return (
            <div key={idx} className="flex items-center gap-2 border-b border-input/30 pb-0">
              <div className="min-w-0">
                {row.kind === "institution" ? (
                  <div className="leading-tight">
                    <div className="text-sm truncate">
                      {row.investor.name}{row.investor.institutionName ? ` with ${row.investor.institutionName}` : ''}
                    </div>
                  </div>
                ) : (
                  <div className="leading-tight">
                    <div className="text-sm truncate">{row.investor.name}</div>
                  </div>
                )}
              </div>
              <Button variant="link" className="p-0" onClick={() => removeInvestor(row.investor.id)}>
                <X className="h-3 w-3" />
              </Button>
            </div>
            )
          })}
        </div>
      </div>

      {showForm ? (
        <div className="mt-2 grid grid-cols-1 md:grid-cols-4 gap-3 items-end">

            
            <Input className="w-auto" value={personName} onChange={(e) => setPersonName(e.target.value)} placeholder="Investor name" />
           
            <Select value={newType} onValueChange={(v: NewType) => setNewType(v)}>
              <SelectTrigger className="w-full"><SelectValue placeholder="Select type" /></SelectTrigger>
              <SelectContent>
                <SelectItem value="Angel">Angel</SelectItem>
                <SelectItem className="w-auto" value="Institution">Institution</SelectItem>
              </SelectContent>
            </Select>

          {newType === "Institution" ? (
            <div>
              <Input value={institutionName} onChange={(e) => setInstitutionName(e.target.value)} placeholder="Institution" />
            </div>
          ) : null}
          <div className="flex gap-2">
            <Button aria-label="Cancel" variant="outline" onClick={() => { setShowForm(false); setPersonName(""); setInstitutionName(""); }}>
              <X className="h-4 w-4" />
            </Button>
            <Button aria-label="Add investor" disabled={!canAdd} onClick={addInvestor}>
              <PlusCircle className="h-4 w-4" />
            </Button>
          </div>
        </div>
      ) : null}

      {/* Hook up single-CTA */}
      <div className="hidden">
        <Button onClick={onNext}>Confirm selection</Button>
      </div>
    </div>
  )
}

function cryptoRandom() {
  // simple fallback for unique-ish ids without crypto import
  return Math.random().toString(36).slice(2, 9)
}

