import Image from "next/image";

type Props = {
  brandIconSrc?: string; // default "/icon.svg"
  name: string; // fixed label text e.g., "Venture Investor"
  score: number; // x.x out of 10
  half: "H1" | "H2";
  year: number;
  percentile: number; // top x%
};

export default function ScoreLine({
  brandIconSrc = "/icon.svg",
  name,
  score,
  half,
  year,
  percentile,
}: Props) {
  return (
    <div className="space-y-1">
      <div className="flex items-center gap-1">
        <Image src={brandIconSrc} alt="Merit Capital" width={25} height={25} />
        <span className="text-md text-muted-foreground">{name}</span>
        <span className="ml-auto text-sm font-semibold">{score.toFixed(1)}/10</span>
      </div>
      <div className="inline-flex items-center gap-2 text-xs text-muted-foreground">
        <span className="inline-flex items-center rounded-full border px-2 py-0.5 bg-muted/60">
          Top {Math.round(percentile)}% in {half} {year}
        </span>
      </div>
    </div>
  );
}


