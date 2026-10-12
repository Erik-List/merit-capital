'use client';

import { useState } from 'react';
import { cn } from '@/lib/utils';
import type { InvestorOutcomes, OutcomeCounts, StageOutcome } from '@/lib/investor-outcomes';

interface InvestmentOutcomesProps {
  name: string;
  outcomes: InvestorOutcomes;
}

/** Entries at a stage before a share is drawn; under it the count stands alone. */
const SHARE_FLOOR = 10;

type OutcomeKey = keyof Pick<StageOutcome, 'oneB' | 'tenB' | 'hundredB' | 'isPublic'>;

/** One chip and its four rows: a stage, or "All" for every company. */
type OutcomeRow = OutcomeCounts & { stage: StageOutcome['stage'] | typeof ALL };
const ALL = 'All';

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
      <div className="h-full bg-primary" style={{ width: `${whole > 0 ? (part / whole) * 100 : 0}%` }} />
    </div>
  );
}

/**
 * Stage chips and one stage at a time, four rows for the picked stage with
 * the share large and the count beneath (Erik, 2026-09-30). It opens on
 * "All", the first chip (Erik, 2026-10-08). The same layout at every width:
 * the `lg` table was dropped for it (Erik, 2026-10-12).
 */
function OutcomeByStage({ rows }: { rows: OutcomeRow[] }) {
  const [picked, setPicked] = useState<OutcomeRow['stage']>(rows[0].stage);
  const stage = rows.find((row) => row.stage === picked) ?? rows[0];
  const thin = stage.entries < SHARE_FLOOR;

  return (
    <div className="space-y-4">
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
        {count(stage.entries)} {stage.entries === 1 ? 'company' : 'companies'}
        {stage.stage === ALL ? ' across every entry stage' : ` first invested in at ${stage.stage}`}
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
 * columns. One stage at a time behind chips, at every width.
 */
export function InvestmentOutcomes({ name, outcomes }: InvestmentOutcomesProps) {
  const stages = outcomes.stages.filter((stage) => stage.entries > 0);
  if (stages.length === 0) return null;
  // "All" leads: every counted company, entry stage on record or not.
  const rows: OutcomeRow[] = [{ stage: ALL, ...outcomes.all }, ...stages];

  return (
    <section className="space-y-4">
      <div className="space-y-2">
        <div className="text-lg font-semibold">Investment Outcome by entry stage</div>
        <p className="text-xs text-muted-foreground">
          What became of the companies {name} first invested in at each stage. The entry round is on record for{' '}
          {formatShare(outcomes.covered, outcomes.companies)} of its companies.
        </p>
      </div>
      <OutcomeByStage rows={rows} />
    </section>
  );
}
