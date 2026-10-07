import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Why | Merit Capital",
  description: "Merit Capital makes performance transparent so founders and VCs can make decisions on merit.",
};

export default function WhyPage() {
  return (
    <div className="container mx-auto py-6 [text-shadow:0_1px_2px_rgb(0_0_0/0.5)]">
      <p className="max-w-3xl text-foreground">
        Investor brands are public. Performance is private. That
        encourages founders to choose buzz over better terms and real help, and
        VCs to build media instead of supporting founders.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        Merit Capital makes performance transparent so both can make decisions on
        merit.
      </p>
      <p className="mt-4 max-w-3xl text-foreground/85">
        It is a public dataset of venture capital performance accessible on the
        web and through an{" "}
        <Link href="/api-reference" className="underline underline-offset-2 hover:text-foreground">
          API
        </Link>
        , without authentication.
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
