"use client";

import type { ReactNode } from "react";
import { cn } from "@/lib/utils";
import InvestorRow from "@/components/leaderboard/investor-row";
import RequestInvestorRow from "@/components/leaderboard/request-investor-row";
import type { ViewState } from "@/components/leaderboard/filters/view";
import type { InvestorStats, Ranking, StageFilter } from "@/components/leaderboard/list-model";

interface InvestorsTableProps {
  ranking: Ranking | null;
  loading?: boolean;
  failed?: boolean;
  /** The search term; a search with no match offers it as a request. */
  search: string;
  stage: StageFilter;
  view: ViewState;
}

// A pinned divider stays at the top of the scroll region while its rows
// pass beneath it, so the reader always sees which group they are in. On
// md+ the region is the card's inner scroller (top 0); below md the page
// scrolls, so it sits under the nav and the search block, whose measured
// height the leaderboard publishes as --pinned-height. Its blur hides the
// rows passing underneath; see the card below for why that blur can work.
function Divider({ children, pinned = false }: { children: ReactNode; pinned?: boolean }) {
  return (
    <li
      className={cn(
        "border-b border-input/30 bg-black/15 px-3 py-2 text-xs text-foreground last:border-b-0 lg:px-4",
        pinned &&
          "sticky z-10 backdrop-blur-xl max-md:top-[calc(var(--nav-height)+1px+var(--pinned-height,0px))] md:top-0",
      )}
    >
      {children}
    </li>
  );
}

export default function InvestorsTable({ ranking, loading, failed, search, stage, view }: InvestorsTableProps) {
  const row = (stats: InvestorStats) => <InvestorRow key={stats.investor.id} stats={stats} stage={stage} view={view} />;

  const items: ReactNode[] = [];
  if (ranking) {
    // With one ordered list the group needs no heading; with no stage picked
    // each group names the stage its investors invest at most.
    const headed = ranking.groups.length > 1;
    ranking.groups.forEach((group) => {
      if (group.rows.length === 0) return;
      if (headed && group.title) items.push(<Divider key={group.title} pinned>{group.title}</Divider>);
      items.push(...group.rows.map(row));
    });
    // The parts under the ordered list take the same pinned heading as the
    // main-stage groups.
    ranking.tail.forEach((part) => {
      if (part.rows.length === 0) return;
      items.push(<Divider key={part.title} pinned>{part.title}</Divider>);
      items.push(...part.rows.map(row));
    });
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
    //
    // The card's glass blur sits on a ::before layer behind the rows rather
    // than on the card itself: Chrome gives a backdrop-filter element's
    // descendants nothing to blur, so a pinned divider inside a blurred card
    // would show the rows through it unblurred (seen 2026-10-08).
    <div className="relative isolate rounded-md border border-input/30 bg-background/5 min-w-0 before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:rounded-[inherit] before:backdrop-blur-md before:content-[''] md:min-h-0 md:flex-1 md:overflow-hidden">
      <div className="md:h-full md:overflow-y-auto md:glass-scrollbar">
        {failed ? (
          <p className="px-4 py-6 text-sm text-muted-foreground">
            The investor data could not be loaded. Reload to try again.
          </p>
        ) : loading || ranking === null ? null : items.length === 0 ? (
          <RequestInvestorRow search={search} />
        ) : (
          <ul className="text-sm">{items}</ul>
        )}
      </div>
    </div>
  );
}
