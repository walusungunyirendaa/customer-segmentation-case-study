import { MEASURES } from "@/lib/aggregate";

export default function Filters({ plans, names, on, toggle, account, setAccount, plan, setPlan, measure, setMeasure }) {
  return (
    <div className="filters">
      <label>
        Account type
        <select value={account} onChange={(e) => setAccount(e.target.value)}>
          <option value="all">All</option>
          <option value="prepaid">Prepaid</option>
          <option value="postpaid">Postpaid</option>
        </select>
      </label>
      <label>
        Current plan
        <select value={plan} onChange={(e) => setPlan(e.target.value)}>
          <option value="all">All</option>
          {plans.map((p) => <option key={p} value={p}>{p}</option>)}
        </select>
      </label>
      <label>
        Chart measure
        <select value={measure} onChange={(e) => setMeasure(Number(e.target.value))}>
          {MEASURES.map((m, i) => <option key={m.label} value={i}>{m.label}</option>)}
        </select>
      </label>
      <div>
        <div className="small">Segments</div>
        <div className="chips">
          {names.map((n, i) => (
            <button key={n} className={on[i] ? "chip on" : "chip"} onClick={() => toggle(i)}>
              {i + 1}. {n}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
