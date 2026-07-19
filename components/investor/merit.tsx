"use client";

import { useMemo } from 'react';

import { Progress } from '@/components/ui/progress';
import { cn } from '@/lib/utils';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Views']['investors']['Row'];

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
  rate?: number | null;
  companies?: string[] | null;
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

function hasGraduationData(bucket: GraduationBucket | null | undefined): boolean {
  if (!bucket) return false;
  const rate = Number(bucket.rate);
  const hasRate = Number.isFinite(rate) && rate >= 0;
  const count = Array.isArray(bucket.companies) ? bucket.companies.length : 0;
  return hasRate || count > 0;
}

type MilestoneKey = 'one_b' | 'ten_b' | 'hundred_b' | 'ipo' | 'rest';

interface TrackRecordMetrics {
  total: number;
  buckets: Record<Extract<MilestoneKey, 'one_b' | 'ten_b' | 'hundred_b' | 'ipo'>, number>;
  rest: number;
}

function computeTrackRecordMetrics(trackRecord: TrackRecord): TrackRecordMetrics | null {
  if (!trackRecord) return null;
  const total = Number(trackRecord.total_companies_invested) || 0;
  const oneB = Number(trackRecord.one_b_companies?.amount) || 0;
  const tenB = Number(trackRecord.ten_b_companies?.amount) || 0;
  const hundredB = Number(trackRecord.hundred_b_companies?.amount) || 0;
  const ipo = Number(trackRecord.ipo_companies?.amount) || 0;
  const consumed = oneB + tenB + hundredB + ipo;
  const rest = Math.max(0, total - consumed);
  return {
    total,
    buckets: {
      one_b: oneB,
      ten_b: tenB,
      hundred_b: hundredB,
      ipo,
    },
    rest,
  };
}

function getYearSpan(startYear?: number | null): number | null {
  if (!startYear || !Number.isFinite(startYear)) return null;
  const currentYear = new Date().getFullYear();
  const span = currentYear - startYear;
  return span > 0 ? span : 1;
}

const SERIES_A_AND_BEYOND = [
  'Series A',
  'Series B',
  'Series C',
  'Series D',
  'Series E',
  'Series F',
  'Series G',
  'Series H',
  'Series I',
  'Series J',
  'Growth',
  'Late Stage',
];

export function InvestorMerit({
  investor,
}: InvestorMeritProps) {
  const trackRecord = useMemo(() => normalizeTrackRecord(investor.track_record), [investor.track_record]);
  const trackMetrics = useMemo(() => computeTrackRecordMetrics(trackRecord), [trackRecord]);
  const graduationRate = useMemo(() => normalizeGraduationRate(investor.graduation_rate), [investor.graduation_rate]);
  const stages = useMemo(() => ensureArray(investor.investment_stage), [investor.investment_stage]);

  const hasPreSeed = stages.map((stage) => stage.toLowerCase()).some((stage) => stage === 'pre-seed' || stage === 'preseed' || stage === 'pre seed');
  const hasSeriesAPlus = stages.some((stage) => SERIES_A_AND_BEYOND.includes(stage));

  const preSeedGraduation = hasPreSeed ? graduationRate?.pre_seed_to_seed : null;
  const seedGraduation = graduationRate?.seed_to_series_a;
  const seriesGraduation = hasSeriesAPlus ? graduationRate?.series_a_to_series_b : null;

  const showPreSeed = hasGraduationData(preSeedGraduation);
  const showSeed = hasGraduationData(seedGraduation);
  const showSeries = hasGraduationData(seriesGraduation);

  const investingSpan = getYearSpan(trackRecord?.investing_start_year);

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

              const segments: Array<{ key: MilestoneKey; label: string; count: number; className: string }> = [
                { key: 'one_b' as MilestoneKey, label: '$1B+', count: trackMetrics.buckets.one_b, className: row.key === 'one_b' ? 'bg-primary' : 'bg-primary/30' },
                { key: 'ten_b' as MilestoneKey, label: '$10B+', count: trackMetrics.buckets.ten_b, className: row.key === 'ten_b' ? 'bg-primary' : 'bg-primary/30' },
                { key: 'hundred_b' as MilestoneKey, label: '$100B+', count: trackMetrics.buckets.hundred_b, className: row.key === 'hundred_b' ? 'bg-primary' : 'bg-primary/30' },
                { key: 'ipo' as MilestoneKey, label: 'IPO', count: trackMetrics.buckets.ipo, className: row.key === 'ipo' ? 'bg-primary' : 'bg-primary/30' },
                { key: 'rest' as MilestoneKey, label: 'Other', count: trackMetrics.rest, className: 'bg-muted' },
              ].filter((segment) => segment.count > 0);

              return (
                <div key={row.key} className="space-y-2">
                  <div className="grid grid-cols-[200px_1fr] items-center gap-3">
                    <span className="text-sm font-medium text-muted-foreground">{row.label}</span>
                    <div className="flex items-center gap-3">
                      <div className="flex h-1.5 w-40 shrink-0 overflow-hidden rounded-full bg-muted">
                        {segments.map((segment) => {
                          const width = trackMetrics.total > 0 ? (segment.count / trackMetrics.total) * 100 : 0;
                          return (
                            <div
                              key={`${row.key}-${segment.key}`}
                              className={cn('h-full', segment.className)}
                              style={{ width: `${width}%` }}
                            />
                          );
                        })}
                      </div>
                      <span className="text-sm font-medium text-muted-foreground">
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
  const rate = Number(bucket?.rate) || 0;
  const companies = Array.isArray(bucket?.companies) ? bucket?.companies?.length ?? 0 : 0;
  const percentage = rate > 0 ? `${Math.round(rate)}%` : '0%';

  return (
    <div className="grid grid-cols-[200px_1fr] items-center gap-4">
      <span className="text-sm font-medium text-muted-foreground">{label}</span>
      <div className="flex items-center gap-3">
        <Progress value={Math.max(0, Math.min(100, rate))} className="h-1.5 w-40 shrink-0" />
        <span className="text-sm font-medium text-muted-foreground">
          {companies ?? 0} ({percentage})
        </span>
      </div>
    </div>
  );
}

