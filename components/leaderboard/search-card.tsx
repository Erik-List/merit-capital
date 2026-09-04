"use client";

import { useEffect, useState, useRef } from "react";
import { Input } from "@/components/ui/input";
import { Search } from "lucide-react";

interface SearchCardProps {
  value: string;
  onChange: (v: string) => void;
}

// Debounce delay in milliseconds - adjust this value to change debounce timing
const DEBOUNCE_DELAY_MS = 300;

export default function SearchCard({ value, onChange }: SearchCardProps) {
  const [localValue, setLocalValue] = useState(value);
  const onChangeRef = useRef(onChange);

  // Keep onChange ref up to date
  useEffect(() => {
    onChangeRef.current = onChange;
  }, [onChange]);

  // Sync local value with prop value when it changes externally (e.g., from URL)
  useEffect(() => {
    setLocalValue(value);
  }, [value]);

  // Debounce the onChange callback
  useEffect(() => {
    const timer = setTimeout(() => {
      onChangeRef.current(localValue);
    }, DEBOUNCE_DELAY_MS);

    return () => clearTimeout(timer);
  }, [localValue]);

  // The input is its own bordered glass surface, so wrapping it in a second
  // bordered card just drew two nested outlines. One surface, one border.
  return (
    <div className="relative">
      <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
      <Input
        placeholder="Search investors..."
        value={localValue}
        onChange={(e) => setLocalValue(e.target.value)}
        type="text"
        className="border-input/50 pl-9"
      />
    </div>
  );
}

 