"use client";

import type { ReactNode } from "react";
import InvestorRow from "@/components/leaderboard/investor-row";
import type { ViewState } from "@/components/leaderboard/filters/view";
import type { InvestorStats, Ranking, StageFilter } from "@/components/leaderboard/list-model";

interface InvestorsTableProps {
  ranking: Ranking | null;
  loading?: boolean;
  failed?: boolean;
  stage: StageFilter;
  view: ViewState;
}

function Divider({ children }: { children: ReactNode }) {
  return (
    <li className="border-b border-input/30 bg-black/15 px-3 py-2 text-xs text-muted-foreground last:border-b-0 lg:px-4">
      {children}
    </li>
  );
}

export default function InvestorsTable({ ranking, loading, failed, stage, view }: InvestorsTableProps) {
  const row = (stats: InvestorStats) => <InvestorRow key={stats.investor.id} stats={stats} stage={stage} view={view} />;

  const items: ReactNode[] = [];
  if (ranking) {
    // With one ordered list the group needs no heading; with no stage picked
    // each group names the stage its investors invest at most.
    const headed = ranking.groups.length > 1;
    ranking.groups.forEach((group) => {
      if (group.rows.length === 0) return;
      if (headed && group.title) items.push(<Divider key={group.title}>{group.title}</Divider>);
      items.push(...group.rows.map(row));
    });
    if (ranking.rest.length > 0) {
      items.push(<Divider key="rest">{ranking.restTitle}</Divider>);
      items.push(...ranking.rest.map(row));
    }
    if (ranking.gone.length > 0) {
      items.push(
        <Divider key="gone">
          {ranking.gone.length} {ranking.gone.length === 1 ? "investor has" : "investors have"} {ranking.goneTitle}:{" "}
          {ranking.gone.map((stats) => stats.investor.name).join(", ")}
        </Divider>,
      );
    }
  }

  return (
    // On md+ the page itself is viewport-bound, so this card is the results
    // scroll region: it takes the leftover height of the column flexbox, and
    // scrolls on an inner wrapper so rows cannot bleed past the rounded
    // corners. Below md every `md:` rule drops out and the card grows with
    // the document.
    <div className="rounded-md border border-input/30 glass min-w-0 md:min-h-0 md:flex-1 md:overflow-hidden">
      <div className="md:h-full md:overflow-y-auto md:glass-scrollbar">
        {failed ? (
          <p className="px-4 py-6 text-sm text-muted-foreground">
            The investor data could not be loaded. Reload to try again.
          </p>
        ) : loading || ranking === null ? null : items.length === 0 ? (
          <p className="px-4 py-6 text-sm text-muted-foreground">No investor matches the search.</p>
        ) : (
          <ul className="text-sm">{items}</ul>
        )}
      </div>
    </div>
  );
}
