/**
 * Formats an investment value from integer to readable format
 * Example: 1000000 -> $1M, 500000 -> $500K
 * @param value - The investment value in integer (e.g., 1000000)
 * @returns Formatted string (e.g., "$1M")
 */
export function formatInvestmentValue(value: number | null | undefined): string {
  if (value === null || value === undefined) return '-';
  
  // Handle billions
  if (value >= 1000000000) {
    const billions = value / 1000000000;
    return `$${billions % 1 === 0 ? billions : billions.toFixed(1)}B`;
  }
  
  // Handle millions
  if (value >= 1000000) {
    const millions = value / 1000000;
    return `$${millions % 1 === 0 ? millions : millions.toFixed(1)}M`;
  }
  
  // Handle thousands
  if (value >= 1000) {
    const thousands = value / 1000;
    return `$${thousands % 1 === 0 ? thousands : thousands.toFixed(1)}K`;
  }
  
  // Handle values less than 1000
  return `$${value}`;
}

/**
 * Formats an investment range from lower and upper limits
 * @param lower - Lower limit of investment in integer
 * @param upper - Upper limit of investment in integer
 * @returns Formatted string (e.g., "$100K – $5M")
 */
export function formatInvestmentRange(lower: number | null | undefined, upper: number | null | undefined): string {
  if ((lower === null || lower === undefined) && (upper === null || upper === undefined)) {
    return '-';
  }
  
  const lowerFormatted = formatInvestmentValue(lower);
  const upperFormatted = formatInvestmentValue(upper);
  
  if (lower === null || lower === undefined) return `Up to ${upperFormatted}`;
  if (upper === null || upper === undefined) return `From ${lowerFormatted}`;
  
  return `${lowerFormatted} – ${upperFormatted}`;
}

/**
 * Formats the standard investment amount
 * @param amount - Standard investment amount in integer
 * @returns Formatted string (e.g., "Standard: $500K")
 */
export function formatStandardInvestment(amount: number | null | undefined): string {
  if (amount === null || amount === undefined) return '';
  
  const formattedAmount = formatInvestmentValue(amount);
  return `Standard: ${formattedAmount}`;
} 