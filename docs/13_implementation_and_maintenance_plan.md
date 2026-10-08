# TelcoX Customer Segmentation: Implementation and Maintenance Plan

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 13 Implementation and Maintenance Plan (optional deliverable) |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 08 Marketing Recommendations, 09 KPI and Measurement Plan, 11 Process Flow, 12 Risk and Limitations Log |

---

## 1. Purpose of This Document

This document explains how TelcoX would move from the analysis to running segment-based campaigns, and how the segments would be kept accurate afterwards. It supports requirement BR5 (segments are easy to reach and use) and BR9 (a review schedule). The timings are an indicative plan for a project of this size.

---

## 2. Plan at a Glance

| Phase | What happens | Indicative length | Result |
|---|---|---|---|
| 0. Approval | Confirm targets, privacy approach, and the open questions in section 6 | 2 weeks | Agreed scope and targets |
| 1. Data and segments | Combine the real data, run the quality checks, build and review the segments | 4 weeks | Segments agreed with stakeholders |
| 2. Preparation | Load segment labels into the campaign tool, brief shops and customer care, set up reporting | 2 weeks | Campaign ready to launch |
| 3. Pilot | Run the fair test: 4 weeks of campaign, then 8 weeks of follow-up | 12 weeks | Test results |
| 4. Decision | Apply the decision rule from document 09 | 1 week | Widen, extend, or stop |
| 5. Rollout | Widen campaigns in the order set in document 08 | About 8 weeks | Segment campaigns running |
| 6. Maintain | Refresh segments every quarter and review results | Ongoing | Up-to-date segments |

---

## 3. Phase Details

### Phase 0. Approval
- Leadership confirms the proposed targets in document 09.
- Legal and compliance review the data fields and who may see segment labels.
- Marketing and product agree the weights for the upgrade ranking and the incentive amounts.
- The team agrees one shared definition of a high-value customer.

### Phase 1. Data and segments
- The IT and data team join billing, customer database, network, and campaign data using the customer ID.
- Run the checks from document 05 on the real data and record what is found.
- Rerun the segmentation notebook. Check whether the number of segments and the segment profiles still make sense. The five segments and names in this case study belong to the synthetic data and may change.
- Review the profiles with marketing, sales, and product before anything is used.

### Phase 2. Preparation
- Create a segment table with one row per customer.
- Load the table into the campaign tool.
- Brief shop staff and customer care using the guides in document 08.
- Build the weekly campaign report from document 09.

### Phase 3. Pilot
- Follow the fair test steps in document 09: eligible list, random split inside each segment, targeted and control groups, locked lists.
- Run the campaign for four weeks, then keep counting upgrades for eight more weeks.
- Report weekly on response, opt-outs, and complaints.

### Phase 4. Decision
- Apply the decision rule. Widen if all conditions are met. Extend to six months if the upgrade result is promising but unclear. Stop and review the offer if a guardrail is worse.

### Phase 5. Rollout
- Widen in this order: Heavy Data Users, then Deal-Seeking Prepaid Users and Long-Term Voice Users, then Steady Postpaid Households and Light Prepaid Users.
- Keep the contact limit of one upgrade or cross-sell offer per customer per month.

---

## 4. The Segment Table

The campaign tool needs a simple table. Each row describes one customer.

| Field | Meaning |
|---|---|
| customer_id | The customer's ID |
| segment | Segment number |
| segment_name | Plain name of the segment |
| outgrown_plan | Yes if the customer uses more data or calls than the plan allows and is not on the top plan |
| recommended_plan | The smallest plan that covers the customer's use |
| offer_code | The offer for this segment (from document 08) |
| test_group | Targeted or control, during the pilot |

The table holds no names, phone numbers, or other personal details. It is refreshed with each quarterly update.

---

## 5. Roles

| Role | Responsibility |
|---|---|
| Business systems analyst | Runs the segmentation, builds the segment table, reports results |
| IT and data team | Provides and combines the data, loads the table into the campaign tool |
| Marketing | Plans and runs campaigns, owns the offers |
| Product and pricing | Agrees incentives, checks plan and service availability |
| Sales and retail, customer care | Use the guides and report customer feedback |
| Legal and compliance | Approves data use and access |
| Leadership | Approves targets and the final decision |

---

## 6. Questions to Settle Before Starting

| Question | Why it matters | Who answers |
|---|---|---|
| Can TelcoX load a segment label for each customer into the campaign tool? | The pilot cannot run without it. | IT and data team |
| Is home broadband available to the customers in Segment 1 who do not have it? | The Segment 1 offer depends on it. | Product and pricing |
| What are the incentive amounts for each offer? | Needed for the campaigns and for break-even costs. | Product and pricing, finance |
| What does a campaign cost today? | Needed for the cost per extra upgrade baseline. | Finance |
| Which customer details may be used? | Needed before the real data is analyzed. | Legal and compliance |

---

## 7. Maintenance

| Task | How often | Owner |
|---|---|---|
| Refresh the segments and compare with the last version | Every quarter | Business systems analyst |
| Check segment sizes and stability against the warning signs in document 09 | Every quarter | Business systems analyst |
| Check whether segment names and profiles still fit | Every quarter | Business systems analyst, marketing |
| Review the risk log | Every quarter | Project team |
| Check that campaigns use the segments | Every quarter | Marketing lead |
| Review the data fields and access rights | Every year, or when fields change | Legal and compliance |

**Handing over.** When the work moves from the analyst to the data team, hand over the notebook, the data dictionary, the segment table definition, and the quarterly checklist above. The notebook is built to run again from start to finish and gives the same results with the same data (requirement NFR2).

---

## 8. Checkpoints

| When | Check |
|---|---|
| End of Phase 0 | Targets, weights, and privacy approach approved |
| End of Phase 1 | Stakeholders can explain each segment in one sentence (requirement NFR1) |
| End of Phase 2 | Segment table loaded, and front-line staff briefed |
| End of Phase 3 | Test finished with locked lists and complete data |
| End of Phase 4 | Decision recorded with the reasons |
| Each quarter | Refresh completed and warning signs checked |
