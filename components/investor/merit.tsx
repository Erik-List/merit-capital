"use client";

import { useMemo } from 'react';

import { Progress } from '@/components/ui/progress';
import { cn } from '@/lib/utils';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

type TrackRecordBucket = {
  amount?: number | null;
  names?: string[] | null;
} | null;

type TrackRecord = {
  total_companies_invested?: number | null;
  investing_start_year?: number | null;
  one_b_companies?: TrackRecordBucket;
  ten_b_companies?: TrackRecordBucket;
  hundred_b_companies?: TrackRecordBucket;
  ipo_companies?: TrackRecordBucket;
} | null;

// The shape recompute_investor_metrics writes: the decided cohort
// (sample_size) with its rate, and the seed entries it was drawn from, so the
// coverage of the rate is visible next to it. rate_percent is null when the
// cohort is empty. Since PRO-132 every seed entry is decided, so the cohort is
// the seed entries minus the censored and the coverage reads 100%.
type GraduationBucket = {
  rate_percent?: number | null;
  graduated?: number | null;
  sample_size?: number | null;
  seed_entries?: number | null;
  censored?: number | null;
} | null;

type GraduationRate = {
  seed_to_series_a?: GraduationBucket;
} | null;

interface InvestorMeritProps {
  investor: Investor;
}

const HIGHLIGHT_KEYS = ["one_b", "ten_b", "hundred_b", "ipo"] as const;

function normalizeTrackRecord(record: Investor['track_record']): TrackRecord {
  if (!record || typeof record !== 'object' || Array.isArray(record)) {
    return null;
  }
  return record as TrackRecord;
}

function normalizeGraduationRate(rate: Investor['graduation_rate']): GraduationRate {
  if (!rate || typeof rate !== 'object' || Array.isArray(rate)) {
    return null;
  }
  return rate as GraduationRate;
}

function calculatePercentage(count: number, total: number): string {
  if (!total || total <= 0 || !count) return '0%';
  const pct = Math.round((count / total) * 1000) / 10;
  const formatted = pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1);
  return `${formatted}%`;
}

// The seed entries gate rendering: the section shows whenever the investor
// has a seed book, even when nothing in it could be established yet (the row
// then says so instead of showing a rate). A bucket without seed_entries is
// the pre-coverage shape and renders only with a non-empty cohort.
function hasGraduationData(bucket: GraduationBucket | null | undefined): boolean {
  if (!bucket) return false;
  const seedEntries = Number(bucket.seed_entries);
  if (Number.isFinite(seedEntries) && seedEntries > 0) return true;
  const sample = Number(bucket.sample_size);
  return Number.isFinite(sample) && sample > 0;
}

type MilestoneKey = 'one_b' | 'ten_b' | 'hundred_b' | 'ipo';

interface TrackRecordMetrics {
  total: number;
  buckets: Record<MilestoneKey, number>;
}

// The buckets are cumulative (a $50B public company is in one_b, ten_b and
// ipo), so they are never summed against each other; each row renders its own
// count against the total.
function computeTrackRecordMetrics(trackRecord: TrackRecord): TrackRecordMetrics | null {
  if (!trackRecord) return null;
  const total = Number(trackRecord.total_companies_invested) || 0;
  return {
    total,
    buckets: {
      one_b: Number(trackRecord.one_b_companies?.amount) || 0,
      ten_b: Number(trackRecord.ten_b_companies?.amount) || 0,
      hundred_b: Number(trackRecord.hundred_b_companies?.amount) || 0,
      ipo: Number(trackRecord.ipo_companies?.amount) || 0,
    },
  };
}

function getYearSpan(startYear?: number | null): number | null {
  if (!startYear || !Number.isFinite(startYear)) return null;
  const currentYear = new Date().getFullYear();
  const span = currentYear - startYear;
  return span > 0 ? span : 1;
}

export function InvestorMerit({
  investor,
}: InvestorMeritProps) {
  const trackRecord = useMemo(() => normalizeTrackRecord(investor.track_record), [investor.track_record]);
  const trackMetrics = useMemo(() => computeTrackRecordMetrics(trackRecord), [trackRecord]);
  const graduationRate = useMemo(() => normalizeGraduationRate(investor.graduation_rate), [investor.graduation_rate]);

  const seedGraduation = graduationRate?.seed_to_series_a;
  const showSeed = hasGraduationData(seedGraduation);

  const investingSpan = getYearSpan(trackRecord?.investing_start_year);

  const notableInvestments = useMemo(() => {
    if (!investor.notable_investments || !Array.isArray(investor.notable_investments)) return null;
    const investments = investor.notable_investments
      .filter((x): x is string => typeof x === 'string' && x.trim().length > 0)
      .map((x) => x.trim())
      .sort((a, b) => a.localeCompare(b));
    return investments.length > 0 ? investments : null;
  }, [investor.notable_investments]);

  const trackRows = useMemo(() => {
    if (!trackMetrics) return [] as Array<{ key: Extract<typeof HIGHLIGHT_KEYS[number], string>; label: string; count: number } | 'fallback'>;
    const rows: Array<{ key: Extract<typeof HIGHLIGHT_KEYS[number], string>; label: string; count: number } | 'fallback'> = [];
    const oneBCount = trackMetrics.buckets.one_b;
    if (oneBCount <= 0) {
      rows.push('fallback');
    } else {
      rows.push({ key: 'one_b', label: '$1B+', count: oneBCount });
    }
    (['ten_b', 'hundred_b', 'ipo'] as const).forEach((key) => {
      const count = trackMetrics.buckets[key];
      if (count > 0) {
        const label = key === 'ten_b' ? '$10B+' : key === 'hundred_b' ? '$100B+' : 'IPO';
        rows.push({ key, label, count });
      }
    });
    return rows;
  }, [trackMetrics]);

  return (
    <div className="space-y-8">
      {/* Track Record */}
      {trackMetrics && trackMetrics.total > 0 ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">
              Track Record from {trackMetrics.total} companies invested{investingSpan ? ` in ${investingSpan} ${investingSpan === 1 ? 'year' : 'years'}` : ''}
            </div>
            <p className="text-xs text-muted-foreground">
              Below shows the current value of companies where {investor.name} invested in.
            </p>
          </div>

          <div className="space-y-3">
            {trackRows.map((row, index) => {
              if (row === 'fallback') {
                return (
                  <p key={`fallback-${index}`} className="text-sm text-muted-foreground">
                    no investment above 1BN valuation
                  </p>
                );
              }

              const count = row.count;
              const percentage = calculatePercentage(count, trackMetrics.total);

              // Cumulative buckets nest, so each row shows only its own
              // subset of the total; summing them as segments of one bar
              // would double-count.
              const width = trackMetrics.total > 0 ? (count / trackMetrics.total) * 100 : 0;

              return (
                <div key={row.key} className="space-y-2">
                  <div className="grid grid-cols-1 items-center gap-1 lg:grid-cols-[minmax(0,200px)_1fr] lg:gap-3">
                    <span className="text-sm font-medium text-muted-foreground">{row.label}</span>
                    <div className="flex min-w-0 items-center gap-3">
                      <div className="flex h-1.5 w-full min-w-0 overflow-hidden rounded-full bg-muted-foreground/30 lg:w-40 lg:shrink-0">
                        <div className={cn('h-full', 'bg-primary')} style={{ width: `${width}%` }} />
                      </div>
                      <span className="shrink-0 whitespace-nowrap text-sm font-medium text-muted-foreground">
                        {count} ({percentage})
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      ) : null}

      {/* Notable Investments, directly below the track record */}
      {notableInvestments ? (
        <section className="space-y-2">
          {/* Flex-wrapped rather than inline: the names are joined by bullets
              with no surrounding whitespace, so as inline text the whole list
              is one unbreakable token and sets a ~450px floor on the card. */}
          <div className="flex flex-wrap items-baseline gap-x-1 text-sm text-foreground">
            <span className="mr-1">Notable Investments:</span>
            {notableInvestments.map((investment, index) => (
              <span key={investment} className="whitespace-nowrap text-muted-foreground">
                {investment}
                {index < notableInvestments.length - 1 ? (
                  <span className="text-muted-foreground/50 ml-1">•</span>
                ) : null}
              </span>
            ))}
          </div>
        </section>
      ) : null}

      {/* Graduation Rates */}
      {showSeed ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Graduation Rates</div>
            <p className="text-xs text-muted-foreground">
              The share of seed-stage entries of {investor.name} that raised a later round. The rate covers the entries whose record could be established; the coverage beside it says how many that is, and entries under two years old are not counted.
            </p>
          </div>
          <div className="space-y-3">
            <GraduationRow label="Seed → Series A" bucket={seedGraduation} />
          </div>
        </section>
      ) : null}
    </div>
  );
}

interface GraduationRowProps {
  label: string;
  bucket: GraduationBucket | null | undefined;
}

function GraduationRow({ label, bucket }: GraduationRowProps) {
  if (!bucket) return null;
  const sampleSize = Number(bucket.sample_size) || 0;
  const censored = Number(bucket.censored) || 0;
  const rate = bucket.rate_percent == null ? null : Number(bucket.rate_percent);
  const hasRate = rate !== null && Number.isFinite(rate) && sampleSize > 0;
  const percentage = !hasRate ? null : rate % 1 === 0 ? `${rate.toFixed(0)}%` : `${rate.toFixed(1)}%`;
  // Coverage: the decided cohort over the entries old enough to be decided.
  // Only stated when the bucket carries its seed entries; the pre-coverage
  // shape says nothing about how much of the seed book the rate covers.
  const seedEntries = Number(bucket.seed_entries);
  const hasCoverage = Number.isFinite(seedEntries) && seedEntries > 0;
  const establishable = hasCoverage ? Math.max(0, seedEntries - censored) : 0;
  const coverage = establishable > 0 ? Math.round((sampleSize / establishable) * 100) : null;
  const detail = !hasCoverage ? null : [
    `${seedEntries} seed ${seedEntries === 1 ? 'entry' : 'entries'}`,
    censored > 0 ? `${censored} too recent` : null,
    coverage !== null ? `${coverage}% coverage` : null,
  ].filter(Boolean).join(' · ');

  return (
    <div className="grid grid-cols-1 items-start gap-1 lg:grid-cols-[minmax(0,200px)_1fr] lg:gap-4">
      <span className="text-sm font-medium text-muted-foreground">{label}</span>
      <div className="flex min-w-0 flex-col gap-1">
        <div className="flex min-w-0 items-center gap-3">
          <Progress value={hasRate ? Math.max(0, Math.min(100, rate)) : 0} className="h-1.5 w-full min-w-0 bg-muted-foreground/30 lg:w-40 lg:shrink-0" />
          <span className="shrink-0 whitespace-nowrap text-sm font-medium text-muted-foreground">
            {hasRate ? `${percentage} of ${sampleSize} established` : 'no established cohort yet'}
          </span>
        </div>
        {detail ? <span className="text-xs text-muted-foreground/80">{detail}</span> : null}
      </div>
    </div>
  );
}

