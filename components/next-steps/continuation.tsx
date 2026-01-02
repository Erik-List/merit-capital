"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useToast } from "@/hooks/use-toast";
import { RatingDialog } from "@/components/rate/rating-dialog";

// Simple linear scale function (replaces @visx/scale)
function scaleLinear({ domain, range }: { domain: [number, number]; range: [number, number] }) {
  const [domainMin, domainMax] = domain;
  const [rangeMin, rangeMax] = range;
  const domainSpan = domainMax - domainMin;
  const rangeSpan = rangeMax - rangeMin;
  
  return (value: number) => {
    const normalized = (value - domainMin) / domainSpan;
    return rangeMin + normalized * rangeSpan;
  };
}

// Dates are handled in UTC for consistency across clients
const START = new Date("2026-01-01T00:00:00Z"); // 2026 start
const END = new Date("2026-07-01T00:00:00Z");   // July '26
const PREVIEW_LAUNCH = new Date("2026-01-05T00:00:00Z");
const LAUNCH = new Date("2026-05-31T00:00:00Z"); // end of May '26

function RoadmapTimeline() {
  const width = 1024;
  const height = 240;
  const margin = { top: 10, right: 16, bottom: 80, left: 22 };
  const axisY = height - margin.bottom;
  const startMs = START.getTime();
  const endMs = END.getTime();
  const x = scaleLinear({ domain: [startMs, endMs], range: [margin.left, width - margin.right] });

  const ticks = [
    { d: new Date("2026-01-01T00:00:00Z"), label: "2026" },
    { d: new Date("2026-02-01T00:00:00Z"), label: "February" },
    { d: new Date("2026-03-01T00:00:00Z"), label: "March" },
    { d: new Date("2026-07-01T00:00:00Z"), label: "July" },
  ];

  const events = [
    {
      d: PREVIEW_LAUNCH,
      title: "preview launch",
      lines: ["proof of concept by support from ecosystem", "start gathering donations"],
    },
    {
      d: LAUNCH,
      title: "launch",
      lines: [
        "full profile for most venture investors",
        "captable investor scoring capability for founders",
      ],
    },
  ];

  // Additional mid-axis event line at 2026
  const YEAR_2026 = new Date("2026-01-01T00:00:00Z");

  // Duration bars (validation and build-out) similar to screenshot
  const validationStart = PREVIEW_LAUNCH; // Jan 5 launch
  const validationEnd = new Date("2026-02-01T00:00:00Z"); // beginning of February
  const buildOutStart = new Date("2026-02-01T00:00:00Z"); // beginning of February
  const buildOutEnd = LAUNCH; // end of May

  return (
    <svg viewBox={`0 0 ${width} ${height}`} className="w-full h-auto select-none" role="img" aria-label="Merit Capital roadmap timeline">
      <g>
        {/* Axis */}
        <line x1={margin.left} x2={width - margin.right} y1={axisY} y2={axisY} stroke="currentColor" className="text-border" strokeWidth={1} />

        {/* Ticks */}
        {ticks.map((t) => {
          const tx = x(t.d.getTime());
          // Increase stem height for 2026 and July to avoid conflict with events
          const isStartOrEnd = t.label === "2026" || t.label === "July";
          const stemHeight = isStartOrEnd ? 36 : 14;
          // Add upward stem for February matching event marker height
          const hasUpwardStem = t.label === "February";
          const upwardStemTop = axisY - 64;
          return (
            <g key={t.label}>
              {/* Upward stem for February */}
              {hasUpwardStem && (
                <line x1={tx} x2={tx} y1={axisY} y2={upwardStemTop} stroke="currentColor" className="text-border" strokeWidth={1} />
              )}
              {/* Downward stem */}
              <line x1={tx} x2={tx} y1={axisY} y2={axisY + stemHeight} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={tx} y={axisY + stemHeight + 18} textAnchor="middle" className="fill-current text-xs md:text-sm text-muted-foreground">{t.label}</text>
            </g>
          );
        })}

        {/* Event ticks */}
        {(() => {
          const previewX = x(PREVIEW_LAUNCH.getTime());
          const launchX = x(LAUNCH.getTime());
          return (
            <>
              <g>
                <line x1={previewX} x2={previewX} y1={axisY} y2={axisY + 14} stroke="currentColor" className="text-border" strokeWidth={1} />
                <text x={previewX} y={axisY + 32} textAnchor="middle" className="fill-current text-xs md:text-sm text-accent-foreground">Jan 5th</text>
              </g>
              <g>
                <line x1={launchX} x2={launchX} y1={axisY} y2={axisY + 14} stroke="currentColor" className="text-border" strokeWidth={1} />
                <text x={launchX} y={axisY + 32} textAnchor="middle" className="fill-current text-xs md:text-sm text-accent-foreground">~end of May</text>
              </g>
            </>
          );
        })()}

        {/* Duration bars */}
        {(() => {
          const yBar = axisY - 22;
          const barHeight = 2;
          const labelYOffset = -6;
          const vStart = x(validationStart.getTime());
          const vEnd = x(validationEnd.getTime());
          const bStart = x(buildOutStart.getTime());
          const bEnd = x(buildOutEnd.getTime());
          return (
            <>
              {/* validation */}
              <line x1={vStart} x2={vEnd} y1={yBar} y2={yBar} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={(vStart + vEnd) / 2} y={yBar + labelYOffset} textAnchor="middle" className="fill-current text-xs md:text-[12px] text-muted-foreground">validation</text>
              {/* build-out with donations */}
              <line x1={bStart} x2={bEnd} y1={yBar} y2={yBar} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={(bStart + bEnd) / 2} y={yBar + labelYOffset} textAnchor="middle" className="fill-current text-xs md:text-[12px] text-muted-foreground">Merit Capital build out with data for all investors with donations</text>
            </>
          );
        })()}

        {/* Extra event stem at 2026 */}
        {(() => {
          const yx = x(YEAR_2026.getTime());
          const stemTop = axisY
          ;
          return (
            <g>
              <line x1={yx} x2={yx} y1={axisY} y2={stemTop} stroke="currentColor" className="text-border" strokeWidth={1} />
            </g>
          );
        })()}

        {/* Event markers */}
        {events.map((e) => {
          const ex = x(e.d.getTime());
          const stemTop = axisY - 64;
          // Left-align preview launch, center-align launch
          const isPreviewLaunch = e.title === "preview launch";
          const textAnchor = isPreviewLaunch ? "start" : "middle";
          const textX = isPreviewLaunch ? ex - 20 : ex; // Offset left-aligned text away from center
          
          return (
            <g key={e.title}>
              <line x1={ex} x2={ex} y1={axisY} y2={stemTop} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={textX} y={stemTop - 45} textAnchor={textAnchor} className="fill-current text-base md:text-lg font-semibold text-accent-foreground">{e.title}</text>
              <text x={textX} y={stemTop - 25} textAnchor={textAnchor} className="fill-current text-xs text-muted-foreground">{e.lines[0]}</text>
              <text x={textX} y={stemTop - 10} textAnchor={textAnchor} className="fill-current text-xs text-muted-foreground">{e.lines[1]}</text>
            </g>
          );
        })}
      </g>
    </svg>
  );
}

export default function Continuation() {
  const { toast } = useToast();
  const [isRateDialogOpen, setIsRateDialogOpen] = useState(false);

  const handleRateInvestors = () => {
    // Set localStorage to true to prevent auto-show across sessions
    const autoShownKey = 'rate-dialog-auto-shown';
    localStorage.setItem(autoShownKey, 'true');
    setIsRateDialogOpen(true);
  };

  return (
    <section id="continuation" className="py-12">
      <div className="space-y-8">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-4">
          <div className="space-y-4">
            <h2 className="text-3xl font-semibold">We need a critical mass of supporters to establish Merit Capital for the long term.</h2>
            
            {/* Support Now Button */}
            <div className="space-y-2">
              <Button
                variant="support"
                onClick={handleRateInvestors}
              >
                Rate Investors
              </Button>
            </div>

            {/* Combined Text */}
            <p className="text-muted-foreground">
              Your support proves the importance of performance transparency in venture investing, and with a critical mass we establish a transparent venture investor ecosystem and cover costs to keep it independent.
            </p>
          </div>

          <div className="grid gap-6">
            {/* VisX Horizontal Timeline in a glass card */}
            <div className="mt-2">
              <div className="glass border border-input/30 rounded-xl p-6 overflow-hidden">
                <RoadmapTimeline />
              </div>
            </div>
          </div>
        </div>
      </div>

      <RatingDialog 
        open={isRateDialogOpen} 
        onOpenChange={setIsRateDialogOpen} 
      />
    </section>
  );
}


