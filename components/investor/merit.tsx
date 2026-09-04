"use client";

import { useMemo } from 'react';

import { Progress } from '@/components/ui/progress';
import { cn } from '@/lib/utils';
import { CANONICAL_STAGES, canonicalizeStage } from '@/lib/taxonomy';
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

type GraduationBucket = {
  rate_percent?: number | null;
  sample_size?: number | null;
} | null;

type GraduationRate = {
  pre_seed_to_seed?: GraduationBucket;
  seed_to_series_a?: GraduationBucket;
  series_a_to_series_b?: GraduationBucket;
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

function ensureArray(value: Investor['investment_stage']): string[] {
  if (!value) return [];
  if (Array.isArray(value)) {
    return value
      .map((entry) => (typeof entry === 'string' ? entry : null))
      .filter((entry): entry is string => Boolean(entry));
  }
  if (typeof value === 'string') {
    return [value];
  }
  return [];
}

function calculatePercentage(count: number, total: number): string {
  if (!total || total <= 0 || !count) return '0%';
  const pct = Math.round((count / total) * 1000) / 10;
  const formatted = pct % 1 === 0 ? pct.toFixed(0) : pct.toFixed(1);
  return `${formatted}%`;
}

// The sample size gates rendering: a rate without its cohort must never
// show, so a bucket missing sample_size is treated as absent.
function hasGraduationData(bucket: GraduationBucket | null | undefined): boolean {
  if (!bucket) return false;
  const rate = Number(bucket.rate_percent);
  const sample = Number(bucket.sample_size);
  return Number.isFinite(rate) && rate >= 0 && Number.isFinite(sample) && sample > 0;
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

// Everything from Series A onward, derived from the canonical ordering rather
// than restated, so a new stage in the taxonomy lands on the right side of the
// split automatically.
const SERIES_A_AND_BEYOND = CANONICAL_STAGES.slice(CANONICAL_STAGES.indexOf('Series A'));

export function InvestorMerit({
  investor,
}: InvestorMeritProps) {
  const trackRecord = useMemo(() => normalizeTrackRecord(investor.track_record), [investor.track_record]);
  const trackMetrics = useMemo(() => computeTrackRecordMetrics(trackRecord), [trackRecord]);
  const graduationRate = useMemo(() => normalizeGraduationRate(investor.graduation_rate), [investor.graduation_rate]);
  const stages = useMemo(() => ensureArray(investor.investment_stage), [investor.investment_stage]);

  const canonicalStages = useMemo(
    () => stages.map((stage) => canonicalizeStage(stage)).filter((stage): stage is string => Boolean(stage)),
    [stages],
  );
  const hasPreSeed = canonicalStages.includes('Pre-Seed');
  const hasSeriesAPlus = canonicalStages.some((stage) => SERIES_A_AND_BEYOND.includes(stage));

  const preSeedGraduation = hasPreSeed ? graduationRate?.pre_seed_to_seed : null;
  const seedGraduation = graduationRate?.seed_to_series_a;
  const seriesGraduation = hasSeriesAPlus ? graduationRate?.series_a_to_series_b : null;

  const showPreSeed = hasGraduationData(preSeedGraduation);
  const showSeed = hasGraduationData(seedGraduation);
  const showSeries = hasGraduationData(seriesGraduation);

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
      {(showPreSeed || showSeed || showSeries) ? (
        <section className="space-y-4">
          <div className="space-y-2">
            <div className="text-lg font-semibold">Graduation Rates</div>
            <p className="text-xs text-muted-foreground">
              Graduation rates show the companies that completed an additional investment round after the initial investment of {investor.name}
            </p>
          </div>
          <div className="space-y-3">
            {showPreSeed ? (
              <GraduationRow label="Pre-Seed → Seed" bucket={preSeedGraduation} />
            ) : null}
            {showSeed ? (
              <GraduationRow label="Seed → Series A" bucket={seedGraduation} />
            ) : null}
            {showSeries ? (
              <GraduationRow label="Series A → Series B" bucket={seriesGraduation} />
            ) : null}
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
  const rate = Number(bucket?.rate_percent) || 0;
  const sampleSize = Number(bucket?.sample_size) || 0;
  const percentage = rate % 1 === 0 ? `${rate.toFixed(0)}%` : `${rate.toFixed(1)}%`;

  return (
    <div className="grid grid-cols-1 items-center gap-1 lg:grid-cols-[minmax(0,200px)_1fr] lg:gap-4">
      <span className="text-sm font-medium text-muted-foreground">{label}</span>
      <div className="flex min-w-0 items-center gap-3">
        <Progress value={Math.max(0, Math.min(100, rate))} className="h-1.5 w-full min-w-0 bg-muted-foreground/30 lg:w-40 lg:shrink-0" />
        <span className="shrink-0 whitespace-nowrap text-sm font-medium text-muted-foreground">
          {percentage} of {sampleSize} companies
        </span>
      </div>
    </div>
  );
}

