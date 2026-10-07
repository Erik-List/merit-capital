import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About | Merit Capital",
  description: "Built by Erik List. Get in touch on LinkedIn, X, or by email.",
};

export default function AboutPage() {
  return (
    // Same light text shadow as the leaderboard masthead: the text sits on
    // the raw background photo.
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <p className="max-w-3xl text-foreground">
        Built by{" "}
        <a
          href="https://erik-list.com"
          target="_blank"
          rel="noreferrer"
          className="underline underline-offset-2 hover:text-foreground"
        >
          Erik List
        </a>
        . Message me on{" "}
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
