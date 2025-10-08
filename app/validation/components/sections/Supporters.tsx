"use client";

import { useMemo } from "react";
import AcknowledgementsList from "@/components/support/AcknowledgementsList";
import ValidatingSupportersList from "@/components/support/ValidatingSupportersList";
import supportersData from "@/data/supporters.json";
import { motion } from "framer-motion";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Info } from "lucide-react";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
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
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true, margin: "-100px" }}
        className="space-y-10"
      >
        <div className="glass border border-input/30 rounded-3xl shadow-lg p-8 space-y-8">
          {/* Heading like Economics */}
          <div className="space-y-4">
            <h2 className="text-3xl md:text-4xl font-semibold tracking-tight">
              We have support from the venture ecosystem.
            </h2>
            <div className="space-y-2">

              {/* Inline dropdown sub-HL for Acknowledgements */}
              <Collapsible>
                <CollapsibleTrigger asChild>
                  <button className="text-sm md:text-base text-muted-foreground underline">Show early supporters</button>
                </CollapsibleTrigger>
                <CollapsibleContent className="mt-3">
                  <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
                    {acknowledgements.map((p) => (
                      <Card key={p.id} className="glass border border-input/30 p-3">
                        <div className="flex flex-col">
                          <span className="font-medium">{p.full_name}</span>
                          {p.contribution ? (
                            <span className="text-sm text-muted-foreground">{p.contribution}</span>
                          ) : null}
                        </div>
                      </Card>
                    ))}
                  </div>
                </CollapsibleContent>
              </Collapsible>
            </div>
          </div>

          {/* Validating supporters */}
          <Card className="glass border border-input/30">
            <CardHeader className="pb-2">
              <CardTitle className="text-lg">Validating supporters</CardTitle>
              <CardDescription>
                Individuals who have declared support for Merit Capital
                <TooltipProvider>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <span className="inline-flex align-middle ml-2 text-muted-foreground">
                        <Info className="h-4 w-4" />
                      </span>
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>Supporters completed the validation flow.</p>
                    </TooltipContent>
                  </Tooltip>
                </TooltipProvider>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ValidatingSupportersList items={validations} defaultCount={10} />
            </CardContent>
          </Card>
        </div>
      </motion.div>
    </section>
  );
}