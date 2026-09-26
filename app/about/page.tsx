import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About | Merit Capital",
  description: "Merit Capital intends to improve venture capital by making the performance of investors as public as their brands.",
};

export default function AboutPage() {
  return (
    // Same light text shadow as the leaderboard masthead: the text sits on
    // the raw background photo.
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <p className="max-w-3xl text-foreground">
        Merit Capital intends to improve venture capital by making the performance of investors as public as their brands.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        Built by{" "}
        <a
          href="https://erik-list.com"
          target="_blank"
          rel="noreferrer"
          className="underline underline-offset-2 hover:text-foreground"
        >
          Erik List
        </a>
        . Message me here:{" "}
        <a href="mailto:erik@meritcapit.al" className="underline underline-offset-2 hover:text-foreground">
          erik@meritcapit.al
        </a>
      </p>
    </div>
  );
}
