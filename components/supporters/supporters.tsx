"use client";

import { useMemo, useState } from "react";
import ValidatingSupportersList from "@/components/support/ValidatingSupportersList";
import supportersData from "@/data/supporters.json";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible";

type Acknowledgement = { id: string; full_name: string; contribution?: string | null; prominent?: boolean };
type Validation = { id: string; full_name: string; organization?: string | null; role?: string | null; prominent?: boolean };

export default function Supporters() {
  const acknowledgements = useMemo(() => {
    const list = (supportersData as any).acknowledgements as Acknowledgement[];
    return Array.isArray(list) ? list : [];
  }, []);

  const validations = useMemo(() => {
    const list = (supportersData as any).validations as Validation[];
    return Array.isArray(list) ? list : [];
  }, []);

  return (
    <section id="supporters" className="py-12">
      <div className="space-y-10">
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-8">
          {/* Heading like Economics */}
          <div className="space-y-4">
            <h2 className="text-3xl md:text-4xl font-semibold tracking-tight">
              The Venture Ecosystem is behind Merit Capital.
            </h2>
          <div className="space-y-2" />
          </div>

          {/* Validating supporters */}
          <Card className="glass border border-input/30">
          <CardHeader className="pb-2 space-y-0">
              <CardTitle className="text-lg">Supporters</CardTitle>
            <CardDescription className="mt-1">Individuals who opted in with their email to support Merit Capital</CardDescription>
          </CardHeader>
            <CardContent>
              <ValidatingSupportersList items={validations} defaultCount={10} />
            </CardContent>
          </Card>

          <InlineAcknowledgements acknowledgements={acknowledgements} />
        </div>
      </div>
    </section>
  );
}

function InlineAcknowledgements({ acknowledgements }: { acknowledgements: { id: string; full_name: string; contribution?: string | null }[] }) {
  const [open, setOpen] = useState(false);
  return (
    <Collapsible open={open} onOpenChange={setOpen}>
      <CollapsibleTrigger asChild>
        <button className="text-sm text-muted-foreground underline">
          {open ? "Close early supporters" : "See early supporters"}
        </button>
      </CollapsibleTrigger>
      <CollapsibleContent className="mt-3">
        {(() => {
          // Split combined names like "Tom Amthauer & Karim Riese" into individual entries
          const names: string[] = acknowledgements.flatMap((p) =>
            p.full_name.includes("&") ? p.full_name.split("&").map((s) => s.trim()) : [p.full_name]
          );
          // Optional mapping to social links; replace '#' with real profiles
          const links: Record<string, string> = {
            "Linus Wetzig": "https://www.linkedin.com/in/linuswetzig/",
            "Tom Amthauer": "https://www.linkedin.com/in/tom-amthauer-284a84226/",
            "Karim Riese": "https://www.linkedin.com/in/karim-riese-6a4690230/",
            "Lukas Esch": "https://www.linkedin.com/in/lukas-esch/",
          };
          return (
            <p className="text-sm">
              {names.map((name, idx) => (
                <span key={`${name}-${idx}`}>
                  <a
                    href={links[name] || "#"}
                    target="_blank"
                    rel="noopener noreferrer"
                    className=""
                  >
                    {name}
                  </a>
                  {idx < names.length - 1 ? ", " : ""}
                </span>
              ))}
            </p>
          );
        })()}
      </CollapsibleContent>
    </Collapsible>
  );
}


