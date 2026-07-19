"use client";

import { useMemo, useState } from 'react';
import type { Database } from '@/types/supabase';

type Investor = Database['public']['Tables']['investors']['Row'];

interface AffiliationsProps {
  investor: Investor;
}

type AffiliationType = 'Angel' | 'Institution' | 'Other';

type CurrentAffiliation = {
  name: string;
  position?: string | null;
  start_year?: number | null;
  type?: AffiliationType;
};

type PastAffiliation = {
  name: string;
  position?: string | null;
  start_year?: number | null;
  end_year?: number | null;
  type?: AffiliationType;
};

type NormalizedAffiliations = {
  current: CurrentAffiliation[];
  past: PastAffiliation[];
};

function resolveAffiliationType(name: string): AffiliationType {
  const normalized = name.toLowerCase();
  if (normalized.includes('angel')) {
    return 'Angel';
  }
  if (normalized.includes('fund') || normalized.includes('ventures') || normalized.includes('capital')) {
    return 'Institution';
  }
  return 'Other';
}

function coerceNumber(value: unknown): number | null {
  if (typeof value === 'number' && Number.isFinite(value)) {
    return value;
  }
  if (typeof value === 'string') {
    const parsed = Number.parseInt(value, 10);
    return Number.isFinite(parsed) ? parsed : null;
  }
  return null;
}

function extractPosition(text: string): string | null {
  const [position] = text.split(' at ');
  return position?.trim() ?? null;
}

function normalizeCurrentAffiliations(
  rawCurrent: unknown,
  fallbackStartYear: number | null,
): CurrentAffiliation[] {
  if (!rawCurrent) {
    return [];
  }

  const base = Array.isArray(rawCurrent) ? rawCurrent : [rawCurrent];

  return base
    .map((entry): CurrentAffiliation | null => {
      if (!entry) {
        return null;
      }

      if (typeof entry === 'string') {
        const name = entry.trim();
        if (!name) {
          return null;
        }
        const type = resolveAffiliationType(name);
        const position = type === 'Angel' ? 'Angel' : 'Partner';
        return {
          name,
          position,
          start_year: fallbackStartYear,
          type,
        };
      }

      if (typeof entry === 'object') {
        const record = entry as Record<string, unknown>;
        const name = typeof record.name === 'string' ? record.name.trim() : '';
        if (!name) {
          return null;
        }

        const type = resolveAffiliationType(name);
        const positionRaw = typeof record.position === 'string' ? record.position.trim() : null;
        const startYear = coerceNumber(record.start_year) ?? fallbackStartYear;
        const resolvedType = (typeof record.type === 'string' ? record.type : type) as AffiliationType;

        return {
          name,
          position: positionRaw ?? (resolvedType === 'Angel' ? 'Angel' : 'Partner'),
          start_year: startYear,
          type: resolvedType,
        };
      }

      return null;
    })
    .filter((item): item is CurrentAffiliation => item !== null);
}

function normalizePastAffiliations(
  rawPast: unknown,
  fallbackStartYear: number | null,
): PastAffiliation[] {
  if (!rawPast) {
    return [];
  }

  const entries = Array.isArray(rawPast) ? rawPast : [rawPast];

  return entries
    .map((entry, index): PastAffiliation | null => {
      if (!entry) {
        return null;
      }

      if (typeof entry === 'string') {
        const name = entry.trim();
        if (!name) {
          return null;
        }

        const position = extractPosition(name) ?? 'Operator';
        const type = resolveAffiliationType(name);
        const startOffset = index * 2 + 2;
        const startYear = fallbackStartYear ? Math.max(fallbackStartYear - startOffset, 1995) : null;
        const endYear = startYear ? startYear + 1 : null;

        return {
          name,
          position,
          start_year: startYear,
          end_year: endYear,
          type,
        };
      }

      if (typeof entry === 'object') {
        const record = entry as Record<string, unknown>;
        const name = typeof record.name === 'string' ? record.name.trim() : '';
        if (!name) {
          return null;
        }

        const position = typeof record.position === 'string' ? record.position.trim() : extractPosition(name) ?? 'Operator';
        const startYear = coerceNumber(record.start_year) ?? fallbackStartYear;
        const endYear = coerceNumber(record.end_year);
        const typeRaw = typeof record.type === 'string' ? record.type : resolveAffiliationType(name);

        return {
          name,
          position,
          start_year: startYear,
          end_year: endYear,
          type: typeRaw as AffiliationType,
        };
      }

      return null;
    })
    .filter((item): item is PastAffiliation => item !== null);
}

function normalizeAffiliations(
  rawAffiliation: unknown,
  fallbackStartYear: number | null,
): NormalizedAffiliations {
  if (!rawAffiliation || typeof rawAffiliation !== 'object') {
    return { current: [], past: [] };
  }

  const record = rawAffiliation as Record<string, unknown>;
  const current = normalizeCurrentAffiliations(record.current, fallbackStartYear);
  const past = normalizePastAffiliations(record.past, fallbackStartYear);

  return { current, past };
}

function formatSinceYears(startYear: number | null | undefined): string | null {
  if (!startYear || !Number.isFinite(startYear)) {
    return null;
  }
  const currentYear = new Date().getFullYear();
  const delta = Math.max(currentYear - startYear, 0);
  if (delta <= 0) {
    return `Since ${currentYear}`;
  }
  return `Since ${delta} year${delta === 1 ? '' : 's'}`;
}

function formatYearRange(startYear: number | null | undefined, endYear: number | null | undefined): string {
  const start = startYear && Number.isFinite(startYear) ? startYear : '—';
  const end = endYear && Number.isFinite(endYear) ? endYear : '—';
  return `${start} - ${end}`;
}

function sortPastAffiliations(past: PastAffiliation[]): PastAffiliation[] {
  return [...past].sort((a, b) => {
    const endA = typeof a.end_year === 'number' ? a.end_year : -Infinity;
    const endB = typeof b.end_year === 'number' ? b.end_year : -Infinity;
    if (endA === endB) {
      const startA = typeof a.start_year === 'number' ? a.start_year : -Infinity;
      const startB = typeof b.start_year === 'number' ? b.start_year : -Infinity;
      return startB - startA;
    }
    return endB - endA;
  });
}

export function Affiliations({ investor }: AffiliationsProps) {
  const investingStartYear = useMemo(() => {
    const trackRecord = investor.track_record as Record<string, unknown> | null;
    if (trackRecord && typeof trackRecord === 'object' && 'investing_start_year' in trackRecord) {
      return coerceNumber((trackRecord as Record<string, unknown>).investing_start_year);
    }
    return coerceNumber(investor.created_at);
  }, [investor.created_at, investor.track_record]);

  const { current, past } = useMemo(
    () => normalizeAffiliations(investor.affiliation, investingStartYear),
    [investor.affiliation, investingStartYear],
  );

  const [showPast, setShowPast] = useState(false);

  if (!current.length && !past.length) {
    return null;
  }

  const sortedPast = useMemo(() => sortPastAffiliations(past), [past]);

  return (
    <section className="glass border border-input/30 rounded-xl p-5 space-y-5">
      <header>
        <h3 className="text-lg font-medium">Affiliations</h3>
      </header>

      <div className="space-y-4">
        {current.map((affiliation, index) => {
          const sinceText = formatSinceYears(affiliation.start_year);
          const isAngel = affiliation.type === 'Angel';
          const position = affiliation.position ?? (isAngel ? 'Angel' : 'Partner');

          return (
            <div key={`${affiliation.name}-${index}`} className="space-y-1">
              <p className="text-sm text-foreground">{affiliation.name}</p>
              <p className="text-xs text-muted-foreground">
                {isAngel ? (
                  sinceText ?? 'Since —'
                ) : (
                  <>
                    {position}
                    <span className="mx-1 text-muted-foreground/60">•</span>
                    {sinceText ?? 'Since —'}
                  </>
                )}
              </p>
            </div>
          );
        })}
      </div>

      {sortedPast.length > 0 ? (
        <div className="space-y-3">
          <button
            type="button"
            onClick={() => setShowPast((value) => !value)}
            className="text-sm underline-offset-4 hover:underline"
          >
            {showPast ? 'Hide past affiliations' : 'See past affiliations'}
          </button>

          {showPast ? (
            <ul className="space-y-3">
              {sortedPast.map((affiliation, index) => (
                <li key={`${affiliation.name}-${index}`} className="space-y-1">
                  <p className="text-sm text-foreground">{affiliation.name}</p>
                  <p className="text-xs text-muted-foreground">
                    {affiliation.position ?? '—'}
                    <span className="mx-1 text-muted-foreground/60">•</span>
                    {formatYearRange(affiliation.start_year, affiliation.end_year)}
                  </p>
                </li>
              ))}
            </ul>
          ) : null}
        </div>
      ) : null}
    </section>
  );
}


