# TelcoX Customer Segmentation: KPI and Measurement Plan

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 09 KPI and Measurement Plan |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 01 Business Requirements, 03 Requirements and User Stories, 08 Marketing Recommendations |

---

## 1. Purpose of This Document

This document explains how TelcoX will know whether segment-based marketing works. It defines the measures of success, shows where each one starts today, describes a fair test against the current approach, and sets out the rule for deciding what happens next. It also covers how often the segments should be refreshed. It supports requirements FR17, FR18, and FR20 and user stories US13, US14, and US16.

The BRD left target numbers open and promised they would be set here. Section 6 proposes them.

---

## 2. Goals and the Measures That Track Them

| Business goal (document 01) | Measure that tracks it |
|---|---|
| B1 More customers upgrade to higher plans | Upgrade rate |
| B2 More customers respond to promotions | Response rate |
| B3 Less money spent on offers that do not fit | Cost per extra upgrade |
| B4 Higher ARPU, especially where needs are unmet | ARPU change |
| B5 One shared view of customer groups | Segment use by teams |

---

## 3. The Measures

### 3.1 Main measures

| ID | Measure | Plain meaning | How it is calculated | Source | How often |
|---|---|---|---|---|---|
| K1 | **Upgrade rate** | The share of customers who moved to a higher plan | Customers who upgraded divided by customers in the group | Billing and customer database | Weekly during the campaign, final result at 3 months |
| K2 | **Response rate** | The share of offers that customers accepted | Offers accepted divided by offers sent | Campaign tool | Weekly |
| K3 | **ARPU change** | How much average monthly spend per customer changed | Average monthly spend at the end of the test minus average spend in the month before the campaign. Compared between the targeted and control groups. | Billing | Monthly |
| K4 | **Cost per extra upgrade** | What each additional upgrade cost | Total campaign cost divided by the extra upgrades in the targeted group (its upgrades minus the upgrades the control group would predict) | Finance and campaign tool | At the end of the test |

### 3.2 Supporting measures

| ID | Measure | Plain meaning | How it is calculated |
|---|---|---|---|
| K5 | **Broadband take-up** (Segment 1) | The share of customers offered broadband who added it | Customers who added broadband divided by customers offered |
| K6 | **Plan fit** | Whether targeted customers still use more than their plan allows | Share of targeted customers over their allowance, before and after. It should fall. |
| K7 | **Segment use** | Whether teams actually use the segments | Share of campaigns planned using segments, checked each quarter |
| K8 | **Segment stability** | Whether the segments hold up over time | Share of customers who stay in the same segment at each refresh |

### 3.3 Guardrail measures

These make sure the campaigns do not cause harm. They are compared between the targeted and control groups.

| ID | Measure | How it is calculated |
|---|---|---|
| G1 | Opt-out rate | Customers who opted out of messages divided by customers contacted |
| G2 | Complaint rate | Complaints per 1,000 customers contacted |
| G3 | Disconnection rate | Customers who left TelcoX divided by customers in the group |

---

## 4. Where We Start: Baselines

The baseline is how the current broad approach performs. These figures come from the customer data. In a real project, they would come from the campaign tool and billing records for the last 6 to 24 months.

| Segment | Response rate (offers accepted ÷ sent, last 6 months) | Monthly upgrade rate (upgrades in last 24 months ÷ 24) | Average monthly spend |
|---|---|---|---|
| 1. Steady Postpaid Households | 9.3% | 1.00% | 32.4 |
| 2. Light Prepaid Users | 5.2% | 0.41% | 19.9 |
| 3. Deal-Seeking Prepaid Users | 26.8% | 0.93% | 31.9 |
| 4. Heavy Data Users | 20.3% | 1.40% | 25.0 |
| 5. Long-Term Voice Users | 6.8% | 0.58% | 17.7 |
| **All customers** | **12.6%** | **0.84%** | **26.8** |

- Among customers who have outgrown their plan, the monthly upgrade rate is about 0.88 percent.
- **Cost per extra upgrade has no baseline in the data.** The finance team would supply the current cost of a campaign and its upgrades.
- **Why the response rate differs from document 07.** Document 07 averages each customer's own rate. This table adds up all offers accepted and divides by all offers sent. The two are close (12.5% and 12.6%).

---

## 5. A Fair Test

A fair test compares customers who got the new approach with similar customers who got the usual one. Without it, any change in upgrades could be put down to the season, a price change, or a competitor.

### 5.1 Steps

1. **List the eligible customers** in each segment. For the upgrade campaigns (Segments 2 to 5), these are customers who use more data or call minutes than their plan allows and are not on the top plan. For the Segment 1 broadband campaign, these are customers without home broadband.
2. **Split each list at random into two equal halves.** The split is done inside each segment, so the two halves are alike. A fixed random seed makes the split repeatable.
3. **Targeted group:** receives the segment offer from document 08.
4. **Control group:** receives the usual broad offer, as today.
5. **Lock the lists.** No customer moves between groups once the campaign starts.
6. **Run the campaign for 4 weeks.**
7. **Keep counting upgrades for 8 more weeks.** The total measuring period is 3 months, because customers do not always upgrade the day they receive an offer.
8. **Compare the groups** on every measure in section 3 and apply the decision rule in section 7.

**Why half and half.** The control group still gets an offer, so no customer is left out. An equal split also gives the most sensitive test.

### 5.2 How big a change can the test detect?

Upgrades are rare. The average customer has less than a 1 percent chance of upgrading in a given month, so small groups cannot show small improvements. The table shows the smallest increase over the control group that the test could reliably tell apart from chance, using a standard 5 percent significance level and 80 percent power.

| Group | Eligible customers | Customers per half | Control group's expected upgrade rate over 3 months | Smallest lift the test can detect |
|---|---|---|---|---|
| 4. Heavy Data Users | 1,823 | 911 | 4.1% | 63% |
| 3. Deal-Seeking Prepaid Users | 1,392 | 696 | 2.8% | 89% |
| 5. Long-Term Voice Users | 1,207 | 603 | 1.7% | 123% |
| 2. Light Prepaid Users | 1,364 | 682 | 1.3% | 130% |
| 1. Steady Postpaid Households (plan check-up) | 1,420 | 710 | 2.6% | 92% |
| **Segments 2 to 5 pooled** | **5,786** | **2,893** | **2.6%** | **45%** |

**How to read it.** For Heavy Data Users, the control group would be expected to upgrade at about 4.1 percent. A lift of 63 percent means the targeted group would need to reach about 6.7 percent before the test could call it a real difference.

**What this means for the design**
- **The formal decision uses the pooled result for Segments 2 to 5.** Pooling the four upgrade campaigns gives groups large enough to detect a 45 percent lift over three months.
- **Segment results are shown but treated as directional.** Single segments are too small to detect modest lifts, except possibly Heavy Data Users.
- **A longer test helps.** For the pooled group, the smallest detectable lift falls from 78 percent at one month to 45 percent at three months and 31 percent at six months. If the three-month result is unclear, the test should continue to six months.
- **Response rate is easier to measure than upgrade rate.** Offers are accepted far more often than plans change, so the response rate will give an early reading while the upgrade rate catches up.

---

## 6. Proposed Targets

These are proposals for leadership to confirm. Each is set so that the test can actually detect it.

| Measure | Proposed target |
|---|---|
| Upgrade rate | At least 45% higher than the control group over three months, in the pooled test. For example, from 2.6% to about 3.8%. |
| Response rate | At least 25% higher than the control group's response rate |
| ARPU change | Higher in the targeted group than in the control group |
| Cost per extra upgrade | At or below the break-even level in section 7.2 |
| Broadband take-up (Segment 1) | Significantly higher than the control group. The first test sets the baseline. |
| Guardrails (G1 to G3) | No significant increase compared with the control group |

---

## 7. Decision Rule

### 7.1 When to widen the campaigns

Widen the segment-based campaigns to all customers in the segment if **all** of these are true at the end of the test:

1. The upgrade rate in the targeted group meets the target in section 6, and the difference is statistically significant (5 percent level).
2. The response rate meets its target.
3. ARPU change is higher in the targeted group than in the control group.
4. Cost per extra upgrade is at or below break-even.
5. None of the guardrail measures is significantly worse in the targeted group.

If the upgrade rate is promising but not yet significant, extend the test to six months. If a guardrail is significantly worse, stop and review the offer before continuing.

### 7.2 Break-even cost

An upgrade is worth running if the extra money it brings in over the months the customer stays is more than the cost of getting it.

**Break-even cost per extra upgrade = extra monthly spend after the upgrade × months the customer is expected to stay**

*Example.* Moving from Standard (20) to Plus (35) adds 15 per month. If the customer stays for 12 months, the extra revenue is 180. A cost per extra upgrade below 180 would pay back. The finance team should replace revenue with margin if it is available.

---

## 8. Reporting

| Report | Audience | How often | Content |
|---|---|---|---|
| Campaign dashboard | Marketing | Weekly during the campaign | Response rate, upgrades so far, opt-outs and complaints, targeted against control |
| Test result summary | Leadership, product, marketing | At 3 months (and 6 months if extended) | All measures, target comparison, decision |
| Segment health check | Marketing, data team | Every quarter | Segment sizes, stability, and use of segments in campaigns |

---

## 9. Keeping the Segments Up to Date

**Recommended refresh: every quarter.** Customer behavior changes gradually, and campaigns change it further. For example, Heavy Data Users who upgrade will use less of their allowance and may fit a different segment next time.

**How to refresh.** Rerun the segmentation notebook on the latest data, then compare the new segments with the previous ones in size and profile and check whether the names still fit.

**Signs the segments are out of date**
- Any segment's share of customers has moved by more than 5 percentage points since the last refresh.
- The stability check falls below 95 percent. The current result is at least 99.3 percent.

---

## 10. Requirements Covered

| Requirement | Where |
|---|---|
| FR17 Define the measures of success and how each is calculated | Section 3 |
| FR18 A test comparing targeted customers with a control group | Section 5 |
| FR20 Recommend how often segments should be refreshed | Section 9 |
| US13 Each measure is defined, calculated, and compared with the current approach | Sections 3, 4, and 6 |
| US14 A fair test with groups, selection steps, duration, and decision rule | Sections 5 and 7 |
| US16 Refresh schedule with one sign of being out of date | Section 9 |
