import Image from "next/image";
import { Badge as UIBadge } from "@/components/ui/badge";

type Props = {
  geography: string;
  stage?: string; // omit when stage-agnostic
  percentile: number; // 10 => Top 10%
  half: "H1" | "H2";
  year: number;
  brandIconSrc?: string; // default "/icon.svg"
};

export default function BadgeAward({
  geography,
  stage,
  percentile,
  half,
  year,
  brandIconSrc = "/icon.svg",
}: Props) {
  return (
    <div className="relative w-52">
      {/* Shield container */}
      <div className="mx-auto w-52 h-64 rounded-b-[2.5rem] rounded-t-[1.25rem] border border-input/30 glass shadow-sm flex flex-col items-center px-4 pt-10 pb-4">
        {/* Brand icon small on top */}
        <div className="absolute top-2 left-1/2 -translate-x-1/2 rounded-full border border-input/30 glass ic p-1.5 shadow">
          <Image src={brandIconSrc} alt="Merit Capital" width={22} height={22} />
        </div>

        {/* Performance */}
        <div className="mt-2 text-center">
          <div className="text-sm text-muted-foreground">Performance</div>
          <div className="text-2xl font-bold">Top {Math.round(percentile)}%</div>
        </div>

        {/* Geography highlight */}
        <div className="mt-4 w-full rounded-md px-3 py-2 text-center text-sm font-medium bg-primary/10 text-primary">
          {geography}
        </div>

        {/* Stage highlight (optional) */}
        {stage ? (
          <div className="mt-2 w-full rounded-md px-3 py-1.5 text-center text-xs font-medium bg-primary/10 text-foreground/80">
            {stage}
          </div>
        ) : null}

        {/* Period chip */}
        <div className="mt-auto">
          <UIBadge variant="outline" className="text-[10px] tracking-wide">
            {half} {year}
          </UIBadge>
        </div>
      </div>
    </div>
  );
}


