import { pageMetadata } from "@/lib/page-metadata";

export const metadata = pageMetadata({
  title: "Why",
  description:
    "Investor brands are public, performance is private. Why that is, and why most of what would answer the question is already public.",
  path: "/why",
});

export default function WhyPage() {
  return (
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <p className="max-w-3xl text-foreground">
        Every listed company reports its results. Every public-market fund manager has a
        track record you can look up. Venture capital has neither.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">What is public about a venture investor:</p>
      <ul className="mt-2 max-w-3xl list-disc space-y-1 pl-5 text-foreground/85">
        <li>the brand</li>
        <li>the partners’ posts</li>
        <li>the logos on the website</li>
        <li>the companies they like to talk about</li>
      </ul>
      <p className="mt-4 max-w-3xl text-foreground/85">What is private:</p>
      <ul className="mt-2 max-w-3xl list-disc space-y-1 pl-5 text-foreground/85">
        <li>which companies they invested in, all of them</li>
        <li>what became of those companies</li>
        <li>how often a seed company they backed made it to a Series A</li>
      </ul>
      <p className="mt-4 max-w-3xl text-foreground/85">
        The asymmetry is structural. Funds report to their LPs, the companies are private,
        nobody owes the public a number. But it has a side effect: when performance is
        invisible, reputation is the only signal. Founders pick the loud fund over the better
        terms and the real help. Funds build audiences instead of supporting companies. Both
        sides are acting rationally on the only information they have.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        Yet most of what would answer the question is already public. Portfolio pages are
        archived back to 2006. Funding rounds are filed with the SEC. Company registers list
        shareholders and directors. Nobody had put it together, because putting it together
        is a year of unpaid work with no obvious owner.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        <a
          href="https://substack.com/@eriklist/note/c-77780472"
          target="_blank"
          rel="noreferrer"
          className="underline underline-offset-2 hover:text-foreground"
        >
          Brain Dump #1
        </a>
        , in November 2024, asked for exactly this and ended with “someone with spare cash
        (and good lawyers), please build this.” Nobody did. It turned out neither is needed.
        The fund returns #1 wanted are still private; what became of the companies is the
        closest public thing to them. So I built that.
      </p>
      <p className="mt-4 max-w-3xl text-foreground">
        Merit Capital is a venture capital performance index: how the invested companies of
        50 of the most well-known venture investors turned out, stage by stage.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        To get in touch, message me on{" "}
        <a
          href="https://www.linkedin.com/in/erik-list1/"
          target="_blank"
          rel="noreferrer"
          className="underline underline-offset-2 hover:text-foreground"
        >
          LinkedIn
        </a>{" "}
        or{" "}
        <a
          href="https://x.com/ErikList_"
          target="_blank"
          rel="noreferrer"
          className="underline underline-offset-2 hover:text-foreground"
        >
          X
        </a>
        , or email erik@meritcapit.al.
      </p>
    </div>
  );
}
