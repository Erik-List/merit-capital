import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Merit Capital",
  description: "Discover the real merit of investors.",
};

import LandingPage from "@/app/validation/components/LandingPage";

export default function ValidationPage() {
  return <LandingPage />;
} 