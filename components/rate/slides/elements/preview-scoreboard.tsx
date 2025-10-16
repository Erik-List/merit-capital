"use client"

import React from "react"

type Item = { id: string; label: string; score: number | null }

export function PreviewScoreboard({ items }: { items: Item[] }) {
  const ranked = React.useMemo(() => items.filter(i => i.score != null).sort((a, b) => (b.score! - a.score!)), [items])
  return (
    <ol className="text-xs space-y-1">
      {ranked.map((i, idx) => (
        <li key={i.id} className="flex items-center gap-2">
          <span className="text-muted-foreground w-5 text-right">#{idx + 1}</span>
          <span className="truncate flex-1">{i.label}</span>
          <span className="tabular-nums">{i.score}</span>
        </li>
      ))}
      {ranked.length === 0 ? (
        <li className="text-muted-foreground">No ratings yet</li>
      ) : null}
    </ol>
  )
}


