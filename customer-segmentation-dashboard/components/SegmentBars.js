import { fmt } from "@/lib/format";

export default function SegmentBars({ groups, names, on, measure }) {
  const values = groups.map((g, i) => (on[i] && g.n ? measure.get(g) : null));
  const max = Math.max(...values.map((v) => v || 0)) || 1;
  return (
    <section className="card spaced">
      <h2>{measure.label} by segment</h2>
      {groups.map((g, i) =>
        on[i] ? (
          <div className="row" key={names[i]}>
            <span>
              {i + 1}. {names[i]}
            </span>
            <div className="track">
              <div
                className="bar"
                style={{ width: `${values[i] ? (100 * values[i]) / max : 0}%` }}
              />
            </div>
            <span className="val">
              {values[i] === null ? "none" : fmt(values[i], measure.decimals)}
            </span>
          </div>
        ) : null,
      )}
    </section>
  );
}
