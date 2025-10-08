"use client";

import { Card } from "@/components/ui/card";

type Acknowledgement = {
  id: string;
  full_name: string;
  contribution?: string | null;
  prominent?: boolean;
};

export function AcknowledgementsList({ items }: { items: Acknowledgement[] }) {
  const sorted = [...items].sort((a, b) => Number(b.prominent) - Number(a.prominent));

  return (
    <div className="space-y-4">
      <ul className="space-y-2">
        {sorted.map((p) => (
          <li key={p.id}>
            <Card className="glass border border-input/30 p-3">
              <div className="flex items-start gap-3">
                <div>
                  <div className="font-medium">{p.full_name}</div>
                  {p.contribution ? (
                    <div className="text-sm text-muted-foreground">{p.contribution}</div>
                  ) : null}
                </div>
              </div>
            </Card>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AcknowledgementsList;


