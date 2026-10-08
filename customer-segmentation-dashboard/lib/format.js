export function fmt(value, decimals = 0) {
  return value.toLocaleString("en-US", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

export function pct(part, whole, decimals = 1) {
  return whole ? `${fmt((100 * part) / whole, decimals)}%` : "-";
}
