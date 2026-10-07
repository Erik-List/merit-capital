import { Progress } from '@/components/ui/progress';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

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

interface GraduationRatesProps {
  investor: Investor;
}

function normalizeGraduationRate(rate: Investor['graduation_rate']): GraduationRate {
  if (!rate || typeof rate !== 'object' || Array.isArray(rate)) {
    return null;
  }
  return rate as GraduationRate;
}

// The seed entries gate rendering: the section shows whenever the investor
// has a seed book, even when nothing in it could be established yet (the row
// then says so instead of showing a rate). A bucket without seed_entries is
// the pre-coverage shape and renders only with a non-empty cohort.
export function hasGraduationData(rate: Investor['graduation_rate']): boolean {
  const bucket = normalizeGraduationRate(rate)?.seed_to_series_a;
  if (!bucket) return false;
  const seedEntries = Number(bucket.seed_entries);
  if (Number.isFinite(seedEntries) && seedEntries > 0) return true;
  const sample = Number(bucket.sample_size);
  return Number.isFinite(sample) && sample > 0;
}

// A server component: the page calls hasGraduationData before rendering it,
// which a client module could not offer.
export function GraduationRates({ investor }: GraduationRatesProps) {
  const seedGraduation = normalizeGraduationRate(investor.graduation_rate)?.seed_to_series_a;

  if (!hasGraduationData(investor.graduation_rate)) return null;

  return (
    <section className="space-y-4">
      <div className="space-y-2">
        <div className="text-lg font-semibold">Seed Graduation Rate</div>
        <p className="text-xs text-muted-foreground">
          The share of seed-stage entries of {investor.name} that raised a later round. The rate covers the entries whose record could be established; the coverage beside it says how many that is, and entries under two years old are not counted.
        </p>
      </div>
      <div className="space-y-3">
        <GraduationRow label="Seed → Series A" bucket={seedGraduation} />
      </div>
    </section>
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

