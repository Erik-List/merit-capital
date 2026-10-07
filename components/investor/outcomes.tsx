'use client';

import { useState } from 'react';
import { cn } from '@/lib/utils';
import type { InvestorOutcomes, StageOutcome } from '@/lib/investor-outcomes';

interface InvestmentOutcomesProps {
  name: string;
  outcomes: InvestorOutcomes;
}

/** Entries at a stage before a share is drawn; under it the count stands alone. */
const SHARE_FLOOR = 10;

type OutcomeKey = keyof Pick<StageOutcome, 'oneB' | 'tenB' | 'hundredB' | 'isPublic'>;

const COLUMNS: ReadonlyArray<{ key: OutcomeKey; label: string }> = [
  { key: 'oneB', label: '$1B+ today' },
  { key: 'tenB', label: '$10B+ today' },
  { key: 'hundredB', label: '$100B+ today' },
  { key: 'isPublic', label: 'Public today' },
];

function formatShare(part: number, whole: number): string {
  if (whole <= 0) return '0%';
  const pct = Math.round((part / whole) * 1000) / 10;
  return `${pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1)}%`;
}

const count = (value: number) => value.toLocaleString('en-US');

function Bar({ part, whole, className }: { part: number; whole: number; className?: string }) {
  return (
    <div className={cn('h-1 overflow-hidden rounded-full bg-muted-foreground/30', className)} aria-hidden="true">
      <div className="h-full rounded-full bg-primary" style={{ width: `${whole > 0 ? (part / whole) * 100 : 0}%` }} />
    </div>
  );
}

/** One table cell: count, share and bar; under the floor the count alone. */
function Cell({ part, whole }: { part: number; whole: number }) {
  if (whole < SHARE_FLOOR) {
    // One company would move the share by ten points or more, so the count
    // stands alone.
    return (
      <td className="whitespace-nowrap py-2.5 pr-3 align-middle text-muted-foreground/80 tabular-nums">
        {part} of {whole}
      </td>
    );
  }
  return (
    <td className="whitespace-nowrap py-2.5 pr-3 align-middle tabular-nums">
      <div className="text-foreground">
        {count(part)} of {count(whole)} <span className="text-muted-foreground">· {formatShare(part, whole)}</span>
      </div>
      <Bar part={part} whole={whole} className="mt-1.5 w-full max-w-[104px]" />
    </td>
  );
}

/** The `lg` table: one row per stage, one column per outcome. */
function OutcomeTable({ rows }: { rows: StageOutcome[] }) {
  return (
    <div className="hidden overflow-x-auto lg:block">
      <table className="w-full min-w-[520px] border-collapse text-sm">
        <thead>
          <tr className="border-b border-input/30 text-left text-xs font-normal text-muted-foreground">
            <th className="whitespace-nowrap py-1.5 pr-3 font-normal">First invested at</th>
            {COLUMNS.map((column) => (
              <th key={column.key} className="whitespace-nowrap py-1.5 pr-3 font-normal">
                {column.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((stage) => (
            <tr key={stage.stage} className="border-b border-input/20 last:border-b-0">
              <td className="whitespace-nowrap py-2.5 pr-3 align-middle text-sm font-medium text-muted-foreground">
                {stage.stage}
              </td>
              {COLUMNS.map((column) => (
                <Cell key={column.key} part={stage[column.key]} whole={stage.entries} />
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/**
 * Below `lg`: stage chips and one stage at a time, four rows for the picked
 * stage with the share large and the count beneath (Erik, 2026-09-30). It
 * opens on the stage the investor entered most companies at.
 */
function OutcomeByStage({ rows }: { rows: StageOutcome[] }) {
  const [picked, setPicked] = useState(() => rows.reduce((best, row) => (row.entries > best.entries ? row : best)).stage);
  const stage = rows.find((row) => row.stage === picked) ?? rows[0];
  const thin = stage.entries < SHARE_FLOOR;

  return (
    <div className="space-y-4 lg:hidden">
      <div role="group" aria-label="First invested at" className="flex flex-wrap gap-1.5">
        {rows.map((row) => {
          const selected = row.stage === stage.stage;
          return (
            <button
              key={row.stage}
              type="button"
              aria-pressed={selected}
              onClick={() => setPicked(row.stage)}
              className={cn(
                'shrink-0 rounded-full border px-2.5 py-1.5 text-[13px] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring',
                selected
                  ? 'border-primary bg-primary text-primary-foreground'
                  : 'border-input/40 text-muted-foreground hover:text-foreground',
              )}
            >
              {row.stage}
            </button>
          );
        })}
      </div>
      <p className="text-xs text-muted-foreground">
        {count(stage.entries)} {stage.entries === 1 ? 'company' : 'companies'} first invested in at {stage.stage}
        {thin ? ' · too few for a share' : ''}
      </p>
      <div className="space-y-3">
        {COLUMNS.map((column) => {
          const part = stage[column.key];
          return (
            <div key={column.key} className="space-y-1.5">
              <div className="flex items-end justify-between gap-3">
                <span className="text-sm text-muted-foreground">{column.label}</span>
                {thin ? (
                  <span className="text-sm text-muted-foreground/80 tabular-nums">
                    {part} of {stage.entries}
                  </span>
                ) : (
                  <span className="text-right tabular-nums">
                    <span className="block text-lg font-medium leading-tight text-foreground">
                      {formatShare(part, stage.entries)}
                    </span>
                    <span className="block text-xs text-muted-foreground">
                      {count(part)} of {count(stage.entries)}
                    </span>
                  </span>
                )}
              </div>
              {thin ? null : <Bar part={part} whole={stage.entries} className="w-full" />}
            </div>
          );
        })}
      </div>
    </div>
  );
}

/**
 * What became of the companies the investor first invested in at each entry
 * stage. The bands nest, so a company at $100B+ is in the first three
 * columns. A table from `lg`; below it, one stage at a time behind chips.
 */
export function InvestmentOutcomes({ name, outcomes }: InvestmentOutcomesProps) {
  const rows = outcomes.stages.filter((stage) => stage.entries > 0);
  if (rows.length === 0) return null;

  return (
    <section className="space-y-4">
      <div className="space-y-2">
        <div className="text-lg font-semibold">Investment Outcome by entry stage</div>
        <p className="text-xs text-muted-foreground">
          What became of the companies {name} first invested in at each stage. The entry round is on record for{' '}
          {formatShare(outcomes.covered, outcomes.companies)} of its companies.
        </p>
      </div>
      <OutcomeTable rows={rows} />
      <OutcomeByStage rows={rows} />
    </section>
  );
}
