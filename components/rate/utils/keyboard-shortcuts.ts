import { useEffect } from "react"

type KeyboardHandler = (key: string) => void

/**
 * Hook to handle keyboard shortcuts for comparison slides
 * 1-4: Select investor at position 1-4
 * Esc: Clear selection (only in selectBest step)
 */
export function useComparisonKeyboardShortcuts(
  step: 'selectBest' | 'selectWorst',
  onSelect: (position: number) => void,
  onClear?: () => void,
  enabled: boolean = true
) {
  useEffect(() => {
    if (!enabled) return

    const handleKeyDown = (e: KeyboardEvent) => {
      // Prevent default if we're handling the key
      if (e.key >= '1' && e.key <= '4') {
        const position = parseInt(e.key) - 1 // Convert to 0-based index
        e.preventDefault()
        onSelect(position)
      } else if (e.key === 'Escape' && step === 'selectBest' && onClear) {
        e.preventDefault()
        onClear()
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => {
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [step, onSelect, onClear, enabled])
}

