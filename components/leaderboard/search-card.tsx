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

  return (
    <div className="rounded-md border border-input/30 glass p-3">
      <div className="relative">
        <Input
          placeholder="Search investors..."
          value={localValue}
          onChange={(e) => setLocalValue(e.target.value)}
          type="text"
        />
      </div>
    </div>
  );
}

 