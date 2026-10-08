import { fmt, pct } from "@/lib/format";

export default function KpiCards({ total: t }) {
  const cards = [
    ["Customers", fmt(t.n)],
    ["Avg data per month", t.n ? `${fmt(t.d / t.n, 1)} GB` : "-"],
    ["Avg spend per month", t.n ? fmt(t.s / t.n, 1) : "-"],
    ["Outgrown their plan", pct(t.r, t.n)],
    ["Promotion response", pct(t.ac, t.rc)],
  ];
  return (
    <div className="kpis">
      {cards.map(([label, value]) => (
        <div className="card" key={label}>
          <div className="num">{value}</div>
          <div className="small">{label}</div>
        </div>
      ))}
    </div>
  );
}
