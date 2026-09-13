"use client";

import { Table, TableBody } from "@/components/ui/table";
import InvestorRow from "@/components/leaderboard/investor-row";
import type { Database } from "@/types/supabase";
import type { StageState } from "@/components/leaderboard/filters/stage-filter";
import type { GeographyState } from "@/components/leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/leaderboard/filters/scope-filter";
import type { ViewState } from "@/components/leaderboard/filters/view";

type Investor = Database["public"]["Tables"]["investors"]["Row"];

interface InvestorsTableProps {
  investors: Investor[];
  loading?: boolean;
  view: ViewState;
  stage: StageState;
  geo: GeographyState;
  scope: ScopeState;
}

export default function InvestorsTable({ investors, loading, view, stage, geo, scope }: InvestorsTableProps) {
  return (
    // On md+ the page itself is viewport-bound, so this card is the results
    // scroll region: it takes the leftover height of the column flexbox, and
    // scrolls on an inner wrapper so rows cannot bleed past the rounded
    // corners. Below md every `md:` rule drops out and the card grows with
    // the document.
    <div className="rounded-md border border-input/30 glass min-w-0 md:min-h-0 md:flex-1 md:overflow-hidden">
      <div className="md:h-full md:overflow-y-auto md:glass-scrollbar">
        <Table className="min-w-full">
          <TableBody>
            {loading ? null : investors.map((inv) => (
              <InvestorRow
                key={inv.id}
                investor={inv}
                view={view}
                stage={stage}
                geo={geo}
                scope={scope}
              />
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}

 