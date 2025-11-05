import type { Database } from '@/types/supabase';
import Link from 'next/link';

type Investor = Database['public']['Views']['InvestorView']['Row'];

interface PeopleProps {
  investor: Investor;
}

type IndividualEntry = {
  name: string;
  position?: string | null;
  socials?: {
    linkedin_url?: string | null;
    x_url?: string | null;
  } | null;
};

function toTitleCase(value: string): string {
  return value
    .split(' ')
    .map((chunk) => chunk.charAt(0).toUpperCase() + chunk.slice(1))
    .join(' ');
}

function normalizeIndividual(entry: unknown): IndividualEntry | null {
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
      position: 'Partner',
      socials: {
        linkedin_url: null,
        x_url: null,
      },
    } satisfies IndividualEntry;
  }

  if (typeof entry === 'object') {
    const record = entry as Record<string, unknown>;
    const name = typeof record.name === 'string' ? record.name.trim() : '';
    if (!name) {
      return null;
    }

    const position = typeof record.position === 'string' && record.position.trim() 
      ? record.position.trim() 
      : (typeof record.role === 'string' && record.role.trim() ? record.role.trim() : 'Partner');
    
    const socialsObj = typeof record.socials === 'object' && record.socials !== null
      ? record.socials as Record<string, unknown>
      : {};
    
    const linkedin = typeof socialsObj.linkedin_url === 'string' && socialsObj.linkedin_url.trim()
      ? socialsObj.linkedin_url.trim()
      : (typeof record.linkedin_url === 'string' && record.linkedin_url.trim()
          ? record.linkedin_url.trim()
          : null);
    
    const xUrl = typeof socialsObj.x_url === 'string' && socialsObj.x_url.trim()
      ? socialsObj.x_url.trim()
      : null;

    return {
      name,
      position,
      socials: {
        linkedin_url: linkedin,
        x_url: xUrl,
      },
    } satisfies IndividualEntry;
  }

  return null;
}

export function People({ investor }: PeopleProps) {
  const rawIndividuals = investor.individual ?? null;
  const individuals: IndividualEntry[] = Array.isArray(rawIndividuals)
    ? rawIndividuals
        .map(normalizeIndividual)
        .filter((individual): individual is IndividualEntry => Boolean(individual))
    : [];

  if (!individuals.length) {
    return null;
  }

  return (
    <section className="glass border border-input/30 rounded-xl p-5 space-y-4">
      <header>
        <h3 className="text-lg font-medium">People</h3>
      </header>

      <ul className="space-y-4">
        {individuals.map((individual, index) => {
          const name = toTitleCase(individual.name);
          const position = individual.position ? toTitleCase(individual.position) : '—';
          const linkedinUrl = individual.socials?.linkedin_url;
          const content = linkedinUrl ? (
            <Link
              href={linkedinUrl}
              target="_blank"
              rel="noreferrer noopener"
              className="text-sm underline-offset-4 hover:underline"
            >
              {name}
            </Link>
          ) : (
            <span className="text-sm underline-offset-4">
              {name}
            </span>
          );

          return (
            <li key={`${individual.name}-${index}`} className="space-y-1">
              {content}
              <p className="text-xs text-muted-foreground">{position}</p>
            </li>
          );
        })}
      </ul>
    </section>
  );
}


