"use client";

import { Button } from "@/components/ui/button";
import { useToast } from "@/hooks/use-toast";

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
const START = new Date("2025-10-01T00:00:00Z"); // Q4 '25 start
const END = new Date("2026-07-01T00:00:00Z");   // July '26
const PREVIEW_LAUNCH = new Date("2025-11-21T00:00:00Z");
const LAUNCH = new Date("2026-05-15T00:00:00Z"); // mid Q2 '26

function RoadmapTimeline() {
  const width = 1024;
  const height = 180;
  const margin = { top: 40, right: 16, bottom: 40, left: 22 };
  const axisY = height - margin.bottom;
  const startMs = START.getTime();
  const endMs = END.getTime();
  const x = scaleLinear({ domain: [startMs, endMs], range: [margin.left, width - margin.right] });

  const ticks = [
    { d: new Date("2025-10-01T00:00:00Z"), label: "Q4 ’25" },
    { d: new Date("2026-01-01T00:00:00Z"), label: "2026" },
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
  const validationStart = PREVIEW_LAUNCH; // around mid-late Nov
  const validationEnd = new Date("2026-01-01T00:00:00Z");
  const buildOutStart = new Date("2026-01-01T00:00:00Z");
  const buildOutEnd = LAUNCH;

  return (
    <svg viewBox={`0 0 ${width} ${height}`} className="w-full h-auto select-none" role="img" aria-label="Merit Capital roadmap timeline">
      <g>
        {/* Axis */}
        <line x1={margin.left} x2={width - margin.right} y1={axisY} y2={axisY} stroke="currentColor" className="text-border" strokeWidth={1} />

        {/* Ticks */}
        {ticks.map((t) => {
          const tx = x(t.d.getTime());
          return (
            <g key={t.label}>
              <line x1={tx} x2={tx} y1={axisY} y2={axisY + 14} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={tx} y={axisY + 32} textAnchor="middle" className="fill-current text-xs md:text-sm text-muted-foreground">{t.label}</text>
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
                <text x={previewX} y={axisY + 32} textAnchor="middle" className="fill-current text-xs md:text-sm text-accent-foreground">Nov 21st</text>
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
          const stemTop = axisY - 40;
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
          return (
            <g key={e.title}>
              <line x1={ex} x2={ex} y1={axisY} y2={stemTop} stroke="currentColor" className="text-border" strokeWidth={1} />
              <text x={ex} y={stemTop - 45} textAnchor="middle" className="fill-current text-base md:text-lg font-semibold text-accent-foreground">{e.title}</text>
              <text x={ex} y={stemTop - 25} textAnchor="middle" className="fill-current text-xs text-muted-foreground">{e.lines[0]}</text>
              <text x={ex} y={stemTop - 10} textAnchor="middle" className="fill-current text-xs text-muted-foreground">{e.lines[1]}</text>
            </g>
          );
        })}
      </g>
    </svg>
  );
}

export default function Continuation() {
  const { toast } = useToast();

  return (
    <section id="continuation" className="py-12">
      <div className="space-y-8">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-4">
          <div className="space-y-3">
            <h2 className="text-3xl font-semibold">We need a critical mass of supporters to establish Merit Capital for the long term.</h2>
            <p className="text-muted-foreground">
              With a critical mass we prove a transparent venture investor ecosystem is important and cover costs to keep it independent.
            </p>
          </div>

            {/* CTA */}
            <div className="pt-2">
              <div className="flex flex-col md:flex-row md:items-center md:justify-start gap-2">
                <Button
                  size="lg"
                  onClick={() =>
                    toast({
                      title: "Support now",
                      description: "CTA flow coming soon. Your support proves the importance of performance transparency.",
                    })
                  }
                >
                  Support now
                </Button>
                <div className="text-sm text-muted-foreground">Your support proves the importance of performance transparency in venture investing.</div>
              </div>
            </div>

          <div className="grid gap-6">
            {/* VisX Horizontal Timeline in a glass card */}
            <div className="mt-2">
              <div className="glass border border-input/30 rounded-xl p-6">
                <RoadmapTimeline />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}


