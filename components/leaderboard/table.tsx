"use client";

import { Table, TableBody } from "@/components/ui/table";
import InvestorRow from "@/components/leaderboard/investor-row";
import type { Database } from "@/types/supabase";
import type { StageState } from "@/components/leaderboard/filters/stage-filter";
import type { GeographyState } from "@/components/leaderboard/filters/geography-filter";
import type { ScopeState } from "@/components/leaderboard/filters/scope-filter";
import type { ViewState } from "@/components/leaderboard/filters/view";
import type { TrackRecordState } from "@/components/leaderboard/track-record-utils";

type Investor = Database["public"]["Tables"]["investors"]["Row"];

interface InvestorsTableProps {
  investors: Investor[];
  loading?: boolean;
  view: ViewState;
  stage: StageState;
  geo: GeographyState;
  scope: ScopeState;
  trackRecord: TrackRecordState;
}

export default function InvestorsTable({ investors, loading, view, stage, geo, scope, trackRecord }: InvestorsTableProps) {
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
            />
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

 