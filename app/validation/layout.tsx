import type { ReactNode } from "react";
import ValidationBackgroundShell from "@/app/validation/components/ValidationBackgroundShell";

// Toggle this flag to enable/disable validation backgrounds
const ENABLE_VALIDATION_BACKGROUND = true;

export default function ValidationLayout({ children }: { children: ReactNode }) {
  return (
    <ValidationBackgroundShell enabled={ENABLE_VALIDATION_BACKGROUND}>
      {children}
    </ValidationBackgroundShell>
  );
}


