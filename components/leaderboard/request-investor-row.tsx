"use client";

import { useEffect, useState, type FormEvent } from "react";
import { Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { INVESTOR_NAME_MAX } from "@/lib/investor-requests";

type Status = "idle" | "sending" | "sent" | "failed";

interface RequestInvestorRowProps {
  /** The search term the name starts from. Empty on a page without a search. */
  search?: string;
  /**
   * `row` is the index's empty state: one horizontal row inside the results
   * card. `page` is a self-contained card for text pages such as the
   * methodology, with the form under the heading instead of beside it.
   */
  variant?: "row" | "page";
}

/**
 * Asks for an investor to be added to the index. In the index it is shown
 * where a search finds no investor; the name starts as the search term and
 * follows it until the visitor edits the field.
 */
export default function RequestInvestorRow({ search = "", variant = "row" }: RequestInvestorRowProps) {
  const [email, setEmail] = useState("");
  const [editedName, setEditedName] = useState<string | null>(null);
  const [website, setWebsite] = useState("");
  const [status, setStatus] = useState<Status>("idle");
  const name = editedName ?? search.trim().slice(0, INVESTOR_NAME_MAX);
  const page = variant === "page";

  // A new search is a new request: the form comes back with the new term.
  useEffect(() => {
    setEditedName(null);
    setStatus("idle");
  }, [search]);

  const send = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setStatus("sending");
    try {
      const response = await fetch("/request-investor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, investor: name, website }),
      });
      if (!response.ok) throw new Error(`request-investor answered ${response.status}`);
      setStatus("sent");
    } catch (e) {
      // eslint-disable-next-line no-console
      console.error("Failed to send the investor request", e);
      setStatus("failed");
    }
  };

  const heading = (
    <div className="flex min-w-0 items-center gap-3">
      <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border border-dashed border-input/60 text-muted-foreground lg:h-12 lg:w-12">
        <Plus className="h-4 w-4" aria-hidden="true" />
      </div>
      <div className="min-w-0">
        <div className="text-base font-medium lg:text-lg">Request an Investor</div>
        <div className="mt-0.5 text-xs text-muted-foreground lg:text-sm">Get an investor added to the index</div>
      </div>
    </div>
  );

  const body =
    status === "sent" ? (
      <p className={page ? "text-sm text-foreground" : "text-sm text-foreground lg:text-right"} role="status">
        Request sent. We will look into {name}.
      </p>
    ) : (
      <form onSubmit={send} className={page ? "flex flex-col gap-1.5" : "flex flex-col gap-1.5 lg:items-end"}>
        {/* On a page the card may be half-width, so the inputs stack. */}
        <div className={page ? "flex flex-col gap-2" : "flex flex-col gap-2 sm:flex-row"}>
          <Input
            type="email"
            required
            maxLength={254}
            autoComplete="email"
            placeholder="Your email"
            aria-label="Your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className={page ? "border-input/50" : "border-input/50 sm:w-52"}
          />
          <Input
            type="text"
            required
            maxLength={INVESTOR_NAME_MAX}
            placeholder="Investor name"
            aria-label="Investor name"
            value={name}
            onChange={(e) => setEditedName(e.target.value)}
            className={page ? "border-input/50" : "border-input/50 sm:w-52"}
          />
          {/* Hidden from people; only a script fills it. */}
          <input
            type="text"
            name="website"
            tabIndex={-1}
            autoComplete="off"
            aria-hidden="true"
            value={website}
            onChange={(e) => setWebsite(e.target.value)}
            className="hidden"
          />
          <Button type="submit" disabled={status === "sending"} className="shrink-0">
            {status === "sending" ? "Sending…" : "Send"}
          </Button>
        </div>
        <p className="text-[11px] text-muted-foreground" role={status === "failed" ? "alert" : undefined}>
          {status === "failed"
            ? "The request could not be sent. Try again."
            : "The investor name becomes public, your email does not."}
        </p>
      </form>
    );

  if (page) {
    // Same card as the index results, so the form reads as the same thing
    // on a text page. The page's text shadow stops at the card edge.
    return (
      <div className="rounded-md border border-input/30 glass px-4 py-4 [text-shadow:none]">
        <div className="flex flex-col gap-4">
          {heading}
          {body}
        </div>
      </div>
    );
  }

  return (
    <div className="px-3 py-3 lg:flex lg:min-h-24 lg:items-center lg:px-4">
      <div className="flex w-full flex-col gap-3 lg:flex-row lg:items-center lg:justify-between lg:gap-6">
        {heading}
        {body}
      </div>
    </div>
  );
}
