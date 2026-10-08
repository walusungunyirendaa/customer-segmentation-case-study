const EMPTY = { n: 0, d: 0, v: 0, s: 0, od: 0, ov: 0, r: 0, u: 0, ac: 0, rc: 0 };

export function aggregate(rows, { account, plan }) {
  const groups = Array.from({ length: 5 }, () => ({ ...EMPTY }));
  for (const x of rows) {
    if (account === "prepaid" && !x.prepaid) continue;
    if (account === "postpaid" && x.prepaid) continue;
    if (plan !== "all" && x.plan !== plan) continue;
    const g = groups[x.segment - 1];
    g.n += x.customers; g.d += x.dataSum; g.v += x.voiceSum; g.s += x.spendSum;
    g.od += x.overData; g.ov += x.overVoice; g.r += x.outgrown;
    g.u += x.upgraded; g.ac += x.accepted; g.rc += x.received;
  }
  return groups;
}

export function sumSelected(groups, on) {
  const total = { ...EMPTY };
  groups.forEach((g, i) => {
    if (on[i]) for (const k in total) total[k] += g[k];
  });
  return total;
}

export const MEASURES = [
  { label: "Customers", get: (g) => g.n, decimals: 0 },
  { label: "Average data per month (GB)", get: (g) => g.d / g.n, decimals: 1 },
  { label: "Average call minutes per month", get: (g) => g.v / g.n, decimals: 0 },
  { label: "Average monthly spend", get: (g) => g.s / g.n, decimals: 1 },
  { label: "Outgrown their plan (%)", get: (g) => (100 * g.r) / g.n, decimals: 1 },
  { label: "Over data allowance (%)", get: (g) => (100 * g.od) / g.n, decimals: 1 },
  { label: "Over call allowance (%)", get: (g) => (100 * g.ov) / g.n, decimals: 1 },
  { label: "Upgraded in last 24 months (%)", get: (g) => (100 * g.u) / g.n, decimals: 1 },
  { label: "Promotion response rate (%)", get: (g) => (g.rc ? (100 * g.ac) / g.rc : 0), decimals: 1 },
];
