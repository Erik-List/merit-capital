"use client";

import { Input } from "@/components/ui/input";
import { Search } from "lucide-react";

interface LeaderboardSearchProps {
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
}

export function LeaderboardSearch({ value, onChange, disabled }: LeaderboardSearchProps) {
  return (
    <div className="relative">
      <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
      <Input
        placeholder="Search investors..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="pl-9"
        disabled={disabled}
      />
    </div>
  );
}



