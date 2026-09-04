"use client";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import type { SortOption } from "@/components/leaderboard/leaderboard";

interface SortDropdownProps {
  value: SortOption;
  onChange: (value: SortOption) => void;
}

export default function SortDropdown({ value, onChange }: SortDropdownProps) {
  return (
    <div className="flex flex-1 lg:justify-end">
      <Select value={value} onValueChange={onChange}>
        <SelectTrigger className="w-full sm:w-[280px]">
          <SelectValue placeholder="Sort by..." />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="track-record-desc">
            Track record descending
          </SelectItem>
          <SelectItem value="graduation-rate-desc">
            Series A graduation rate descending
          </SelectItem>
        </SelectContent>
      </Select>
    </div>
  );
}













