"use client";

import {
  Dialog,
  DialogContent,
  DialogTitle,
} from "@/components/ui/dialog";
import RatingSection from "@/components/rate/rating-section";

interface RatingDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export function RatingDialog({ open, onOpenChange }: RatingDialogProps) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-6xl max-h-[90vh] overflow-y-auto p-0 glass-scrollbar">
        <DialogTitle className="sr-only">Rate Investors</DialogTitle>
        <div className="p-8">
          <RatingSection />
        </div>
      </DialogContent>
    </Dialog>
  );
}
