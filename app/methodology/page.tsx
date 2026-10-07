import type { Metadata } from "next";
import type { ReactNode } from "react";
import {
  Archive,
  BookOpen,
  Check,
  FileText,
  Landmark,
  Mail,
  Newspaper,
  UserMinus,
  X,
  type LucideIcon,
} from "lucide-react";
import RequestInvestorRow from "@/components/leaderboard/request-investor-row";

export const metadata: Metadata = {
  title: "Methodology | Merit Capital",
  description:
    "How Merit Capital reconstructs venture investment histories from public sources, documents decisions, and verifies its data.",
};

const repository = "https://github.com/Erik-List/merit-capital";
const contact = "erik@meritcapit.al";
const linkClass = "underline underline-offset-2 hover:text-foreground";
// The same card as the index results. Text inside sits on glass, not on the
// photo, so the page's text shadow stops at the card edge.
const cardClass = "rounded-md border border-input/30 glass [text-shadow:none]";

function ExternalLink({ href, children }: { href: string; children: ReactNode }) {
  return (
    <a href={href} target="_blank" rel="noreferrer" className={linkClass}>
      {children}
    </a>
  );
}

function Section({ id, title, children }: { id: string; title: string; children: ReactNode }) {
  return (
    <section id={id} className="scroll-mt-24 space-y-3">
      <h2 className="text-lg font-medium text-foreground">{title}</h2>
      {children}
    </section>
  );
}

function IconBadge({ icon: Icon }: { icon: LucideIcon }) {
  return (
    <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md border border-input/30 bg-background/10 text-foreground">
      <Icon className="h-4 w-4" aria-hidden="true" />
    </div>
  );
}

const sections = [
  { id: "what-counts", title: "What counts" },
  { id: "sources", title: "Sources" },
  { id: "how-it-is-built", title: "How it is built" },
  { id: "limitations", title: "Limitations" },
  { id: "corrections", title: "Corrections and removals" },
  { id: "requests", title: "Requests and edits" },
];

const counted = [
  "Every company the evidence shows the firm invested in, once per investor",
  "Attributed to the stage of the firm's first investment",
  "Active, acquired, public and closed companies alike",
];

const notCounted = [
  "Personal angel investments by partners",
  "Investments in other funds",
  "Positions first acquired on public markets",
];

const sources: { icon: LucideIcon; name: string; what: string }[] = [
  {
    icon: FileText,
    name: "SEC filings (EDGAR)",
    what: "Form D financing notices, IPO prospectuses and ownership disclosures: funding, holdings and investment history.",
  },
  {
    icon: Landmark,
    name: "Investment adviser disclosures",
    what: "Form ADV filings: firm structure, affiliated advisers, funds and reported assets.",
  },
  {
    icon: Archive,
    name: "Current and archived websites",
    what: "Portfolio pages and Internet Archive snapshots back to 2006, which recover investments no longer listed.",
  },
  {
    icon: Newspaper,
    name: "Announcements and reporting",
    what: "Funding rounds, acquisitions, valuations and closures reported by companies, investors and the press.",
  },
  {
    icon: BookOpen,
    name: "National company registers",
    what: "Shareholder, director and company-status records, where a jurisdiction publishes them.",
  },
];

const steps: { title: string; body: ReactNode }[] = [
  {
    title: "Collect the evidence",
    body: (
      <>
        Archived portfolio pages, SEC filings, Form D bulk data and company registers are pulled per
        investor and kept with the row they support.
      </>
    ),
  },
  {
    title: "Decide membership",
    body: (
      <>
        Every candidate company passes an independent judgment under a shared{" "}
        <ExternalLink href={`${repository}/blob/main/data/collection/COLLECTION.md`}>
          collection playbook
        </ExternalLink>
        . Firm boundaries and exceptions are written down per investor, such as{" "}
        <ExternalLink href={`${repository}/blob/main/data/collection/investors/accel/documentation/decisions.md`}>
          Accel’s decisions
        </ExternalLink>
        .
      </>
    ),
  },
  {
    title: "Classify the outcome",
    body: (
      <>
        Current status, valuation range and seed-to-Series-A graduation are judged per company.
        Source references, classification decisions and excluded records stay in each investor’s
        company records, such as{" "}
        <ExternalLink href={`${repository}/tree/main/data/collection/investors/accel/companies`}>
          Accel’s
        </ExternalLink>
        .
      </>
    ),
  },
  {
    title: "Verify and publish",
    body: (
      <>
        Checks look for duplicates, conflicting classifications and missing evidence before a book
        goes live. Investor metrics such as track record and graduation rate are computed from the
        company rows, never entered by hand.
      </>
    ),
  },
];

export default function MethodologyPage() {
  return (
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <div className="max-w-3xl space-y-10 text-foreground/85">
        <div className="space-y-4">
          <p className="text-foreground">
            Merit Capital reconstructs each investor’s venture investment history from public
            records. Current and archived portfolio listings, regulatory filings and company
            announcements establish which companies an investor backed and what became of them.
            Nothing is self-reported, and every published row was reviewed by a person.
          </p>
          <nav aria-label="On this page" className="flex flex-wrap gap-2">
            {sections.map((section) => (
              <a
                key={section.id}
                href={`#${section.id}`}
                className="rounded-full border border-input/30 px-2.5 py-1 text-xs text-foreground/85 hover:border-input/60 hover:text-foreground"
              >
                {section.title}
              </a>
            ))}
          </nav>
        </div>

        <Section id="what-counts" title="What counts">
          <div className={`${cardClass} grid gap-6 p-4 sm:grid-cols-2`}>
            <div>
              <h3 className="mb-2 text-sm font-medium text-foreground">Counted</h3>
              <ul className="space-y-2 text-sm">
                {counted.map((item) => (
                  <li key={item} className="flex gap-2">
                    <Check className="mt-0.5 h-4 w-4 shrink-0 text-foreground" aria-hidden="true" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h3 className="mb-2 text-sm font-medium text-foreground">Not counted</h3>
              <ul className="space-y-2 text-sm">
                {notCounted.map((item) => (
                  <li key={item} className="flex gap-2">
                    <X className="mt-0.5 h-4 w-4 shrink-0 text-muted-foreground" aria-hidden="true" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          <p className="text-sm">
            A company whose round or outcome cannot be established is marked undetermined and left
            out of every metric.
          </p>
        </Section>

        <Section id="sources" title="Sources">
          <ul className="grid gap-3 sm:grid-cols-2">
            {sources.map((source) => (
              <li key={source.name} className={`${cardClass} flex gap-3 p-4`}>
                <IconBadge icon={source.icon} />
                <div className="min-w-0">
                  <h3 className="font-medium text-foreground">{source.name}</h3>
                  <p className="mt-1 text-sm">{source.what}</p>
                </div>
              </li>
            ))}
          </ul>
        </Section>

        <Section id="how-it-is-built" title="How it is built">
          <ol className="space-y-0">
            {steps.map((step, index) => (
              <li key={step.title} className="relative flex gap-4 pb-6 last:pb-0">
                {index < steps.length - 1 && (
                  <span
                    className="absolute left-[15px] top-8 h-[calc(100%-2rem)] w-px bg-input/30"
                    aria-hidden="true"
                  />
                )}
                <span
                  className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-input/60 bg-background/10 text-sm font-medium text-foreground [text-shadow:none]"
                  aria-hidden="true"
                >
                  {index + 1}
                </span>
                <div className="min-w-0 pt-1">
                  <h3 className="font-medium text-foreground">{step.title}</h3>
                  <p className="mt-1">{step.body}</p>
                </div>
              </li>
            ))}
          </ol>
          <p>
            <ExternalLink href={`${repository}/tree/main/data/collection/investors`}>
              Browse the documentation and records for every investor →
            </ExternalLink>
          </p>
        </Section>

        <Section id="limitations" title="Limitations">
          <div className={`${cardClass} p-4`}>
            <p className="font-medium text-foreground">Read every number as a lower bound.</p>
            <ul className="mt-3 list-disc space-y-2 pl-5 text-sm">
              <li>
                Public records are incomplete, most of all for undisclosed investments, older
                companies and jurisdictions with thin disclosure. Coverage differs by firm, so it is
                lower for some firms than for others.
              </li>
              <li>Valuations come from the last evidenced event and may be stale.</li>
              <li>
                The index measures observable company outcomes. It does not know entry prices,
                ownership or realised returns, so it cannot establish an investor’s financial
                performance or its contribution to a company’s success.
              </li>
            </ul>
          </div>
        </Section>

        <Section id="corrections" title="Corrections and removals">
          <div className="grid gap-3 sm:grid-cols-2">
            <div className={`${cardClass} flex gap-3 p-4`}>
              <IconBadge icon={Mail} />
              <div className="min-w-0">
                <h3 className="font-medium text-foreground">Wrong number?</h3>
                <p className="mt-1 text-sm">
                  Email{" "}
                  <a href={`mailto:${contact}`} className={linkClass}>
                    {contact}
                  </a>{" "}
                  with the investor, the company and the source. Corrections with a source are
                  applied in weekly batches through November 2026. After that, open an issue in the{" "}
                  <ExternalLink href={`${repository}/issues`}>repository</ExternalLink>.
                </p>
              </div>
            </div>
            <div className={`${cardClass} flex gap-3 p-4`}>
              <IconBadge icon={UserMinus} />
              <div className="min-w-0">
                <h3 className="font-medium text-foreground">Named on a page?</h3>
                <p className="mt-1 text-sm">
                  Names and links of individuals come from public sources. Anyone named can have
                  their name and links removed: email the same address. No reason is needed.
                </p>
              </div>
            </div>
          </div>
        </Section>

        <Section id="requests" title="Requests and edits">
          <p>
            Missing an investor? Request it below. Requests are recorded, and nothing is promised on
            timing.
          </p>
          <RequestInvestorRow variant="page" />
          <p className="text-sm">
            Investors who want their profile changed (description, logo or links) can email the
            change. Profile text is published as the firm states it. Metrics are computed from the
            company records and are not edited by hand.
          </p>
        </Section>
      </div>
    </div>
  );
}
