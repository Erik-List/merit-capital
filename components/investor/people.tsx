'use client';

import type { Database } from '@/types/supabase';
import { Linkedin } from 'lucide-react';
import { SearchableList } from './searchable-list';

type Investor = Database['public']['Tables']['investors']['Row'];

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
      position: null,
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
      : (typeof record.role === 'string' && record.role.trim() ? record.role.trim() : null);

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

// lucide-react deprecated brand glyphs, so the X mark is a local path.
function XMarkIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" className={className} aria-hidden="true">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
    </svg>
  );
}

function SocialIconLink({
  href,
  label,
  children,
}: {
  href: string;
  label: string;
  children: React.ReactNode;
}) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noreferrer noopener"
      aria-label={label}
      className="text-muted-foreground transition-colors hover:text-foreground"
    >
      {children}
    </a>
  );
}

export function People({ investor }: PeopleProps) {
  const rawIndividuals = investor.individuals ?? null;
  const individuals: IndividualEntry[] = Array.isArray(rawIndividuals)
    ? rawIndividuals
        .map(normalizeIndividual)
        .filter((individual): individual is IndividualEntry => Boolean(individual))
    : [];

  if (!individuals.length) {
    return null;
  }

  return (
    <SearchableList
      title="People"
      items={individuals}
      searchText={(individual) => `${individual.name} ${individual.position ?? ''}`}
      searchPlaceholder="Search people"
      renderItem={(individual, index) => {
        const name = toTitleCase(individual.name);
        const position = individual.position ? toTitleCase(individual.position) : null;
        const linkedinUrl = individual.socials?.linkedin_url;
        const xUrl = individual.socials?.x_url;

        return (
          <li key={`${individual.name}-${index}`} className="space-y-1">
            <div className="flex items-center justify-between gap-3">
              <span className="text-sm">{name}</span>
              {linkedinUrl || xUrl ? (
                <span className="flex shrink-0 items-center gap-2">
                  {linkedinUrl ? (
                    <SocialIconLink href={linkedinUrl} label={`${name} on LinkedIn`}>
                      <Linkedin className="h-3.5 w-3.5" />
                    </SocialIconLink>
                  ) : null}
                  {xUrl ? (
                    <SocialIconLink href={xUrl} label={`${name} on X`}>
                      <XMarkIcon className="h-3 w-3" />
                    </SocialIconLink>
                  ) : null}
                </span>
              ) : null}
            </div>
            {position ? <p className="text-xs text-muted-foreground">{position}</p> : null}
          </li>
        );
      }}
    />
  );
}
