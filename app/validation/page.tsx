import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Ranked Capital | Meritocratizing the VC Investment Landscape",
  description: "Founders score the investors on their cap table.",
};

import LandingPage from "@/app/validation/components/LandingPage";

export default function ValidationPage() {
  return <LandingPage />;
} 