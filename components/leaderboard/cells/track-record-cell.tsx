import * as React from 'react';
import { TableCell, TableHead } from '@/components/ui/table';
import { Info } from 'lucide-react';
import { Tooltip, TooltipTrigger, TooltipContent } from '@/components/ui/tooltip';

type TrackRecordJson = {
  one_b_companies?: { amount?: number; names?: string[] } | null;
  ten_b_companies?: { amount?: number; names?: string[] } | null;
  hundred_b_companies?: { amount?: number; names?: string[] } | null;
  ipo_companies?: { amount?: number; names?: string[] } | null;
  total_companies_invested?: number | null;
  investing_start_year?: number | null;
} | null;

function formatPercent(numerator: number, denominator: number): string {
  if (!Number.isFinite(numerator) || !Number.isFinite(denominator) || denominator <= 0) {
    return '0%';
  }
  const percent = (numerator / denominator) * 100;
  if (percent < 10 && percent > 0) {
    return `${percent.toFixed(1)}%`;
  }
  return `${Math.round(percent)}%`;
}

function formatYears(startYear?: number | null): string | null {
  if (!startYear || !Number.isFinite(startYear)) return null;
  const now = new Date();
  const currentYear = now.getUTCFullYear();
  const years = currentYear - startYear; // exclusive
  if (!Number.isFinite(years) || years < 0) return null;
  return `${Math.max(0, years)} years`;
}

function NamesWithTooltip({
  count,
  names,
  underline = true,
}: { count: number; names?: string[]; underline?: boolean }) {
  const MAX_INLINE = 10;
  const extra = Math.max(0, count - MAX_INLINE);
  const label = extra > 0 ? `+${extra}` : String(count);
  const display = underline ? <span className="underline">{label}</span> : <span>{label}</span>;
  const list = (names || []).join(', ');
  if (count <= 0) return <span className={underline ? 'underline' : undefined}>0</span>;
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <span>{display}</span>
      </TooltipTrigger>
      <TooltipContent className="max-w-xs whitespace-pre-wrap break-words text-xs">
        {list}
      </TooltipContent>
    </Tooltip>
  );
}

export function TrackRecordHeader({ className }: { className?: string }) {
  return (
    <TableHead className={className}>
      <div className="inline-flex items-center gap-1">
        <span>Track Record</span>
        <Tooltip>
          <TooltipTrigger asChild>
            <Info className="h-3.5 w-3.5 text-muted-foreground" />
          </TooltipTrigger>
          <TooltipContent className="max-w-sm text-xs">
            Shows the percentage of portfolio companies that reached 1B+, 10B+, 100B+ valuations or went public after initial investment.
          </TooltipContent>
        </Tooltip>
      </div>
    </TableHead>
  );
}

export default function TrackRecordCell({ trackRecord }: { trackRecord: TrackRecordJson }) {
  const tr = trackRecord || {};
  const one = tr.one_b_companies || {};
  const ten = tr.ten_b_companies || {};
  const hundred = tr.hundred_b_companies || {};
  const ipo = tr.ipo_companies || {};
  const total = (tr.total_companies_invested ?? null) as number | null;
  const startYear = (tr.investing_start_year ?? null) as number | null;

  const totalSafe = Number.isFinite(total as number) && (total as number) > 0 ? (total as number) : 0;
  const totalDisplay = Number.isFinite(total as number) ? (total as number) : null;
  const yearsStr = formatYears(startYear);

  const n1 = Number.isFinite(one.amount as number) ? (one.amount as number) : 0;
  const n10 = Number.isFinite(ten.amount as number) ? (ten.amount as number) : 0;
  const n100 = Number.isFinite(hundred.amount as number) ? (hundred.amount as number) : 0;
  const nIPO = Number.isFinite(ipo.amount as number) ? (ipo.amount as number) : 0;

  const p1 = formatPercent(n1, totalSafe);
  const p10 = formatPercent(n10, totalSafe);
  const p100 = formatPercent(n100, totalSafe);
  const pIPO = formatPercent(nIPO, totalSafe);

  const showAnyBigNumbers = n1 > 0 || n10 > 0 || n100 > 0 || nIPO > 0;

  return (
    <TableCell className="align-top">
      <div className="flex flex-col gap-1 text-xs">
        <div className="font-medium text-muted-foreground">
          {totalDisplay !== null ? `${totalDisplay} companies` : '0 companies'}
          {yearsStr ? ` in ${yearsStr}` : ''}
        </div>

        <div className="w-fit min-w-[120px] flex flex-col gap-0.5 glass rounded-sm border border-input/30 p-1">
          <div>
            {n1 > 0 ? (
              <>
                1B: {p1} (
                <NamesWithTooltip count={n1} names={one.names || []} />
                )
              </>
            ) : (
              <>1B: —</>
            )}
            {n10 > 0 && (
              <>
                {' · '}
                10B: {p10} (
                <NamesWithTooltip count={n10} names={ten.names || []} />
                )
              </>
            )}
          </div>

          {(n100 > 0 || nIPO > 0) && (
            <div>
              {n100 > 0 && (
                <>
                  100B: {p100} (
                  <NamesWithTooltip count={n100} names={hundred.names || []} />
                  )
                </>
              )}
              {n100 > 0 && nIPO > 0 && ' · '}
              {nIPO > 0 && (
                <>
                  IPO: {pIPO} (
                  <NamesWithTooltip count={nIPO} names={ipo.names || []} />
                  )
                </>
              )}
            </div>
          )}
        </div>
      </div>
    </TableCell>
  );
}

export function TrackRecordCellLoading() {
  return (
    <TableCell className="align-top">
      <div className="flex flex-col gap-1 text-xs">
        <div className="h-3 w-24 bg-muted/50 rounded" />
        <div className="h-3 w-36 bg-muted/50 rounded" />
      </div>
    </TableCell>
  );
}



