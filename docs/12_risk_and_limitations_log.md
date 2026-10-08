# TelcoX Customer Segmentation: Risk and Limitations Log

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 12 Risk and Limitations Log (optional deliverable) |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 01 Business Requirements, 05 Data Quality and Preparation Report, 09 KPI and Measurement Plan |

---

## 1. Purpose of This Document

This log lists what could go wrong with the project and its results, how likely and how serious each risk is, and what reduces it. It also lists the limits of the work, so that no one reads more into the results than they can support. It builds on the risk table in document 01.

**How to read the ratings.** Likelihood and impact are rated High, Medium, or Low. These are judgments made for this case study, and the project team would review them with stakeholders.

---

## 2. Risk Log

| ID | Risk | Type | Likelihood | Impact | How it is reduced | Owner |
|---|---|---|---|---|---|---|
| R1 | The segments overlap, so customers near the edges may be treated as if they clearly belong to one group. The silhouette score for five segments is low (0.157). | Analysis | High | Medium | Present segments as a practical way to divide customers, not exact labels. Use the need rule so offers go to customers with a clear gap between use and plan. | Business systems analyst |
| R2 | Customer behavior changes and the segments go out of date. Campaigns also change behavior, as when Heavy Data Users upgrade. | Analysis | High | Medium | Refresh every quarter. Watch segment size shifts of more than 5 points and a stability score below 95 percent. | Business systems analyst |
| R3 | The upgrade ranking depends on the chosen weights (50, 25, 25). A different weighting moves Voice Users and Deal-Seekers between ranks 2 and 3. | Analysis | Medium | Medium | Show the ranking under other weights. Agree the weights with marketing and product before the pilot. | Business systems analyst |
| R4 | The test is too small to detect modest improvements. Single segments could only detect lifts of 63 to 130 percent over three months. | Measurement | High | High | Pool Segments 2 to 5 for the formal decision (45 percent detectable lift). Extend to six months if unclear. | Business systems analyst |
| R5 | Offers move customers to plans that are too large, leading to complaints or later downgrades. | Business | Medium | High | Offer the smallest plan that covers the customer's use. Track complaints and disconnections as guardrails. | Marketing |
| R6 | Customers learn to wait for deals, especially Deal-Seeking Prepaid Users. | Business | Medium | Medium | Time-limited offers, no weekly offers, and a limit of one upgrade or cross-sell offer per customer per month. | Marketing |
| R7 | Too many messages cause opt-outs and complaints. | Business | Medium | Medium | Contact limit per customer. Report opt-out and complaint rates in every campaign review. | Marketing |
| R8 | Teams do not adopt the segments, or keep defining high-value customers in their own ways. | Adoption | Medium | High | Short plain-language profiles, shop guides, and a care briefing. Agree one shared definition of a high-value customer at the start. | Marketing lead |
| R9 | Real customer data is messier than the synthetic data, with more gaps, mismatched customer IDs between systems, and inconsistent units. | Data | High | Medium | Run the full quality checks in document 05 on real data first. Add checks for dates, units, and ID matching. | IT and data team |
| R10 | Sensitive personal details are used or exposed. Gender is the only sensitive field in the case-study data. | Privacy | Low | High | Keep personal details out of the analysis and keep gender out of the grouping. Review fields and access with the legal and compliance team. | Legal and compliance |
| R11 | Segment labels are seen by people who should not see them, or are used for purposes other than marketing. | Privacy | Low | Medium | Limit access to the label table and record who uses it and why. | Data team |
| R12 | A recommended channel or service is not available. For example, broadband may not reach some Segment 1 customers. | Business | Medium | Medium | Check availability before making the offer, and screen eligible customers by coverage. | Product and pricing |
| R13 | Cleaning choices, such as limiting values at the 99th percentile and treating empty fields as 0, affect the segments. | Analysis | Medium | Low | The choices are documented. A future check could show how much the segments change under other choices. | Business systems analyst |
| R14 | Results from a three-month test are read as permanent. | Measurement | Medium | Medium | Report the test period with each result and repeat measurement after refreshes. | Business systems analyst |

---

## 3. Limitations

These are not risks to manage. They are limits of what the project has done.

- **The data is synthetic.** The case study shows how the method works and does not describe real customers. The groups in the data were designed, so the match between segments and real customer types has not been tested.
- **No cause and effect has been shown yet.** The segments describe behavior. Whether the offers raise upgrades is only known after the fair test in document 09.
- **Churn is not modelled.** Customers leaving TelcoX is outside the scope. It is only watched as a guardrail.
- **Prices and plans are unchanged.** The project works within existing plans. Whether the plans themselves are right is a separate question for the product and pricing team.
- **Cost data is missing.** Cost per extra upgrade has no baseline until finance supplies campaign costs.
- **Some segment details are incomplete.** Age is not stated for 11 percent of customers, and for 18 percent in Segments 2 and 3.
- **The roaming group in Segment 1 is not a segment of its own.** A six-segment test showed that a group like it would be just under the 5 percent minimum size.

---

## 4. Review Schedule

| When | What |
|---|---|
| Before the pilot | Review R3, R4, R5, R7, R8, and R12 with stakeholders |
| At each campaign review | Check R5, R6, and R7 with the guardrail measures |
| At each quarterly refresh | Review R1, R2, and R13, and update ratings |
| When moving to real data | Review R9, R10, and R11 first |
