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

// "CTO at Stripe" carries a position; a bare company name does not.
function extractPosition(text: string): string | null {
  if (!text.includes(' at ')) {
    return null;
  }
  const [position] = text.split(' at ');
  const trimmed = position?.trim();
  return trimmed ? trimmed : null;
}

function normalizeCurrentAffiliations(rawCurrent: unknown): CurrentAffiliation[] {
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
        return {
          name,
          position: null,
          start_year: null,
          type: resolveAffiliationType(name),
        };
      }

      if (typeof entry === 'object') {
        const record = entry as Record<string, unknown>;
        const name = typeof record.name === 'string' ? record.name.trim() : '';
        if (!name) {
          return null;
        }

        const positionRaw = typeof record.position === 'string' ? record.position.trim() : '';
        const resolvedType = (typeof record.type === 'string'
          ? record.type
          : resolveAffiliationType(name)) as AffiliationType;

        return {
          name,
          position: positionRaw || null,
          start_year: coerceNumber(record.start_year),
          type: resolvedType,
        };
      }

      return null;
    })
    .filter((item): item is CurrentAffiliation => item !== null);
}

function normalizePastAffiliations(rawPast: unknown): PastAffiliation[] {
  if (!rawPast) {
    return [];
  }

  const entries = Array.isArray(rawPast) ? rawPast : [rawPast];

  return entries
    .map((entry): PastAffiliation | null => {
      if (!entry) {
        return null;
      }

      if (typeof entry === 'string') {
        const name = entry.trim();
        if (!name) {
          return null;
        }

        return {
          name,
          position: extractPosition(name),
          start_year: null,
          end_year: null,
          type: resolveAffiliationType(name),
        };
      }

      if (typeof entry === 'object') {
        const record = entry as Record<string, unknown>;
        const name = typeof record.name === 'string' ? record.name.trim() : '';
        if (!name) {
          return null;
        }

        const positionRaw = typeof record.position === 'string' ? record.position.trim() : '';
        const typeRaw = typeof record.type === 'string' ? record.type : resolveAffiliationType(name);

        return {
          name,
          position: positionRaw || extractPosition(name),
          start_year: coerceNumber(record.start_year),
          end_year: coerceNumber(record.end_year),
          type: typeRaw as AffiliationType,
        };
      }

      return null;
    })
    .filter((item): item is PastAffiliation => item !== null);
}

function normalizeAffiliations(rawAffiliation: unknown): NormalizedAffiliations {
  if (!rawAffiliation || typeof rawAffiliation !== 'object') {
    return { current: [], past: [] };
  }

  const record = rawAffiliation as Record<string, unknown>;
  const current = normalizeCurrentAffiliations(record.current);
  const past = normalizePastAffiliations(record.past);

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

function formatYearRange(startYear: number | null | undefined, endYear: number | null | undefined): string | null {
  const hasStart = Boolean(startYear && Number.isFinite(startYear));
  const hasEnd = Boolean(endYear && Number.isFinite(endYear));
  if (!hasStart && !hasEnd) {
    return null;
  }
  return `${hasStart ? startYear : '—'} - ${hasEnd ? endYear : '—'}`;
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
  const { current, past } = useMemo(
    () => normalizeAffiliations(investor.affiliation),
    [investor.affiliation],
  );

  const sortedPast = useMemo(() => sortPastAffiliations(past), [past]);

  const [showPast, setShowPast] = useState(false);

  if (!current.length && !past.length) {
    return null;
  }

  return (
    <section className="glass border border-input/30 rounded-xl p-5 space-y-5">
      <header>
        <h3 className="text-lg font-medium">Affiliations</h3>
      </header>

      <div className="space-y-4">
        {current.map((affiliation, index) => {
          const sinceText = formatSinceYears(affiliation.start_year);
          const detailParts = [affiliation.position, sinceText].filter(
            (part): part is string => Boolean(part),
          );

          return (
            <div key={`${affiliation.name}-${index}`} className="space-y-1">
              <p className="text-sm text-foreground">{affiliation.name}</p>
              {detailParts.length > 0 ? (
                <p className="text-xs text-muted-foreground">
                  {detailParts.map((part, partIndex) => (
                    <span key={part}>
                      {partIndex > 0 && <span className="mx-1 text-muted-foreground/60">•</span>}
                      {part}
                    </span>
                  ))}
                </p>
              ) : null}
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
              {sortedPast.map((affiliation, index) => {
                const yearRange = formatYearRange(affiliation.start_year, affiliation.end_year);
                const detailParts = [affiliation.position, yearRange].filter(
                  (part): part is string => Boolean(part),
                );

                return (
                  <li key={`${affiliation.name}-${index}`} className="space-y-1">
                    <p className="text-sm text-foreground">{affiliation.name}</p>
                    {detailParts.length > 0 ? (
                      <p className="text-xs text-muted-foreground">
                        {detailParts.map((part, partIndex) => (
                          <span key={part}>
                            {partIndex > 0 && <span className="mx-1 text-muted-foreground/60">•</span>}
                            {part}
                          </span>
                        ))}
                      </p>
                    ) : null}
                  </li>
                );
              })}
            </ul>
          ) : null}
        </div>
      ) : null}
    </section>
  );
}
