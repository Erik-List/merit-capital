import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Methodology | Merit Capital",
  description:
    "How Merit Capital reconstructs venture investment histories from public sources, documents decisions, and verifies its data.",
};

const repository = "https://github.com/Erik-List/merit-capital";
const linkClass = "underline underline-offset-2 hover:text-foreground";

export default function MethodologyPage() {
  return (
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <div className="max-w-3xl space-y-4 text-foreground/85">
        <p className="text-foreground">
          Merit Capital reconstructs each investor’s venture investment history
          from publicly available information. Current and archived portfolio
          listings, regulatory filings, and company announcements help establish
          which companies an investor backed and what happened to them.
        </p>
        <p>
          Each company counts once per investor, attributed to the stage of the
          firm’s first investment. The index includes active, acquired, public,
          and closed companies. Personal angel investments, investments in other
          funds, and positions first acquired on public markets are excluded.
        </p>
        <div>
          <p>Sources include:</p>
          <ul className="mt-2 list-disc space-y-2 pl-5">
            <li>
              <strong className="font-medium text-foreground">SEC filings through EDGAR:</strong>{" "}
              financing notices (Form D), IPO prospectuses, and ownership
              disclosures provide evidence of funding, holdings, and investment
              history.
            </li>
            <li>
              <strong className="font-medium text-foreground">Investment adviser disclosures:</strong>{" "}
              Form ADV filings establish firm structure, affiliated advisers,
              funds, and reported assets.
            </li>
            <li>
              <strong className="font-medium text-foreground">Current and archived websites:</strong>{" "}
              portfolio pages and Internet Archive snapshots recover investments
              no longer listed on an investor’s website.
            </li>
            <li>
              <strong className="font-medium text-foreground">Announcements and reporting:</strong>{" "}
              funding rounds, acquisitions, valuations, and closures reported by
              companies, investors, and the press.
            </li>
            <li>
              <strong className="font-medium text-foreground">National company registers:</strong>{" "}
              shareholder, director, and company-status records, where available.
            </li>
          </ul>
        </div>
        <p>
          Automated collection and agent-assisted research follow a shared{" "}
          <a
            href={`${repository}/blob/main/data/collection/COLLECTION.md`}
            target="_blank"
            rel="noreferrer"
            className={linkClass}
          >
            collection playbook
          </a>
          . Investor-specific decisions, such as{" "}
          <a
            href={`${repository}/blob/main/data/collection/investors/accel/documentation/decisions.md`}
            target="_blank"
            rel="noreferrer"
            className={linkClass}
          >
            Accel’s
          </a>
          , document firm boundaries and exceptions. Source references,
          classification decisions, and excluded records are retained in each
          investor’s company records, such as{" "}
          <a
            href={`${repository}/tree/main/data/collection/investors/accel/companies`}
            target="_blank"
            rel="noreferrer"
            className={linkClass}
          >
            Accel’s company records
          </a>
          . Verification checks look for duplicates, conflicting classifications,
          and missing evidence.
        </p>
        <p>
          <a
            href={`${repository}/tree/main/data/collection/investors`}
            target="_blank"
            rel="noreferrer"
            className={linkClass}
          >
            Browse the documentation and records for every investor →
          </a>
        </p>
        <p>
          Public records are incomplete, especially for undisclosed investments,
          older companies, and jurisdictions with limited disclosures. Valuations
          may be stale. The index measures observable company outcomes; it cannot
          establish an investor’s financial returns or contribution to a company’s
          success.
        </p>
        <p>
          To suggest a correction or contribute a missing source, email Erik at
          erik@meritcapit.al with the investor, company, and supporting evidence.
        </p>
      </div>
    </div>
  );
}
