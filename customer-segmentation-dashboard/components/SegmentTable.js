import { fmt, pct } from "@/lib/format";

export default function SegmentTable({ groups, names, on, total }) {
  return (
    <section className="card">
      <h2>Segment details</h2>
      <div className="scroll">
        <table>
          <thead>
            <tr>
              <th>Segment</th>
              <th>Customers</th>
              <th>Share</th>
              <th>Data GB</th>
              <th>Call min</th>
              <th>Spend</th>
              <th>Outgrown plan</th>
              <th>Upgraded before</th>
              <th>Response</th>
            </tr>
          </thead>
          <tbody>
            {groups.map((g, i) =>
              on[i] ? (
                <tr key={names[i]}>
                  <td>
                    {i + 1}. {names[i]}
                  </td>
                  <td>{fmt(g.n)}</td>
                  <td>{pct(g.n, total.n)}</td>
                  <td>{g.n ? fmt(g.d / g.n, 1) : "-"}</td>
                  <td>{g.n ? fmt(g.v / g.n) : "-"}</td>
                  <td>{g.n ? fmt(g.s / g.n, 1) : "-"}</td>
                  <td>{pct(g.r, g.n)}</td>
                  <td>{pct(g.u, g.n)}</td>
                  <td>{pct(g.ac, g.rc)}</td>
                </tr>
              ) : null,
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
