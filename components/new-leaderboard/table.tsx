"use client";

import { Table, TableBody } from "@/components/ui/table";
import InvestorRow from "@/components/new-leaderboard/investor-row";
import type { Database } from "@/types/supabase";
import type { StageState } from "@/components/new-leaderboard/filters/stage-filter";
import type { GeographyState } from "@/components/new-leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/new-leaderboard/filters/scope-filter";
import type { ViewState } from "@/components/new-leaderboard/filters/view";
import type { TrackRecordState } from "@/components/new-leaderboard/track-record-utils";
import type { FounderScoreFilterState } from "@/components/new-leaderboard/filters/founder-score-filter-types";

type Investor = Database["public"]["Views"]["InvestorView"]["Row"];

interface InvestorsTableProps {
  investors: Investor[];
  loading?: boolean;
  view: ViewState;
  stage: StageState;
  geo: GeographyState;
  scope: ScopeState;
  trackRecord: TrackRecordState;
  founder: FounderScoreFilterState;
}

export default function InvestorsTable({ investors, loading, view, stage, geo, scope, trackRecord, founder }: InvestorsTableProps) {
  return (
    <div className="rounded-md border border-input/30 glass min-w-0">
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
              trackRecord={trackRecord}
              founder={founder}
            />
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

 