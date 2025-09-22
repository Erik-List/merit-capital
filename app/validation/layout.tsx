import type { ReactNode } from "react";
import Image from "next/image";

export default function ValidationLayout({ children }: { children: ReactNode }) {
  return (
    <>
      {/* Fixed, route-scoped background behind everything */}
      <div aria-hidden className="fixed inset-0 z-0 pointer-events-none select-none">
        <Image
          src="/backgrounds/validation/bg-validation-lake-mountains-3840x2160.jpg"
          alt=""
          priority
          unoptimized
          fill
          sizes="100vw"
          className="object-cover"
          quality={100}
        />
      </div>

      {/* Foreground content */}
      <div className="relative z-10">
        {children}
      </div>
    </>
  );
}


