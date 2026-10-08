"use client"; // this component uses state, so it runs in the browser

import { useState } from "react";
import data from "@/data/segments.json";
import { aggregate, sumSelected, MEASURES } from "@/lib/aggregate";
import Filters from "./Filters";
import KpiCards from "./KpiCards";
import SegmentBars from "./SegmentBars";
import SegmentTable from "./SegmentTable";

export default function Dashboard() {
  const [account, setAccount] = useState("all");
  const [plan, setPlan] = useState("all");
  const [measure, setMeasure] = useState(4);
  const [on, setOn] = useState([true, true, true, true, true]);

  const groups = aggregate(data.rows, { account, plan });
  const total = sumSelected(groups, on);
  const toggle = (i) => setOn(on.map((v, k) => (k === i ? !v : v)));

  return (
    <main className="wrap">
      <h1>TelcoX Segment Dashboard</h1>
      <p className="sub">
        Explore the five customer segments. Fictional company, synthetic data,
        segment-level figures only.
      </p>
      <Filters
        plans={data.plans}
        names={data.segmentNames}
        on={on}
        toggle={toggle}
        account={account}
        setAccount={setAccount}
        plan={plan}
        setPlan={setPlan}
        measure={measure}
        setMeasure={setMeasure}
      />
      <KpiCards total={total} />
      <SegmentBars
        groups={groups}
        names={data.segmentNames}
        on={on}
        measure={MEASURES[measure]}
      />
      <SegmentTable
        groups={groups}
        names={data.segmentNames}
        on={on}
        total={total}
      />
      <p className="foot">
        Plans: Basic 5 GB and 100 minutes, Standard 15 GB and 300 minutes, Plus
        40 GB and 600 minutes, Premium 100 GB and 1,000 minutes. &quot;Outgrown
        plan&quot; means over the data or call allowance and not on the top
        plan. Segment names and figures match documents 07 and 08.
      </p>
    </main>
  );
}
