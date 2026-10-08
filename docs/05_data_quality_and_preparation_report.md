# TelcoX Customer Segmentation: Data Quality and Preparation Report

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 05 Data Quality and Preparation Report |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 03 Requirements and User Stories, 04 Data Dictionary, Segmentation Analysis notebook (Stage 1) |

---

## 1. Purpose of This Document

This report explains what was wrong with the TelcoX customer data, how each problem was handled, and how the data was prepared for grouping customers. It supports requirements FR2 to FR5 and user story US2. Every number in this report comes from Stage 1 of the segmentation notebook, so anyone can rerun the notebook and check it.

---

## 2. Summary

| Item | Result |
|---|---|
| Rows received | 15,060 |
| Customers after cleaning | 15,000 |
| Repeated customer records removed | 60 (0.4 percent) |
| Records with a wrong plan allowance, corrected | 33 |
| Customers with a missing age | 1,649 (11.0 percent) |
| Customers with gender marked "Not stated" | 616 (4.1 percent) |
| Fields that are empty by design | 5 |
| Customers who received no promotions | 91 |
| Customers with at least one extreme value limited | 1,484 (10 percent) |
| Features considered for grouping | 21 |
| Features used for grouping | 19 |

**In short:** the data was in good shape. The problems were small and easy to fix, apart from the missing ages, which are mostly in prepaid customers. No customers were removed except exact repeats.

---

## 3. Joining the Data Sources

The data dictionary lists four source systems: billing, the customer database, network usage records, and the campaign tool. In a real project, these would be joined using the customer ID, and the number of customers before and after joining would be recorded.

In this case study the data is synthetic, and the generator already produces one table with fields from all four sources. So no join was needed. The one check that applies is the row count: the table had 15,060 rows and 15,000 customers once repeated records were removed.

---

## 4. Problems Found and How They Were Handled

### 4.1 Overview

| # | Problem | How many | How it was handled | Reason |
|---|---|---|---|---|
| 1 | Repeated customer records | 60 | Kept the first record, removed the rest | Each customer should count once. |
| 2 | Plan allowance does not match the plan name | 33 | Replaced with the allowance from the plan table | The plan name is the more reliable field. |
| 3 | Age not recorded | 1,649 | Labelled "Not stated" | Removing them would lose a large part of the prepaid base. |
| 4 | Broadband data empty (no broadband) | 11,711 | Set to 0 | These customers use no home broadband data. |
| 5 | Top-up fields empty (postpaid) | 7,146 | Set to 0 | Postpaid customers do not top up. |
| 6 | Promo response rate empty (no promotions received) | 91 | Left empty in the clean table. Set to 0 only in the copy used for grouping. | A response rate cannot be worked out without promotions. |
| 7 | Very large values in usage and spending | 1,484 customers | Limited in the grouping copy only (see section 5.3) | A few very heavy users would otherwise pull the groups towards themselves. |

### 4.2 Missing values

Six fields contain empty cells. Five of them are empty for a good reason. Only the age field is a real gap.

| Field | Empty cells | Share of customers | Reason | Action |
|---|---|---|---|---|
| months_since_last_upgrade | 12,354 | 82.4% | Customer never upgraded | Left empty. Used only to describe segments. |
| broadband_gb | 11,711 | 78.1% | No home broadband | Set to 0 |
| late_payments_6m | 7,854 | 52.4% | Prepaid customers have no bills | Left empty. Used only to describe segments. |
| topups_per_month | 7,146 | 47.6% | Postpaid customers do not top up | Set to 0 |
| avg_topup_amount | 7,146 | 47.6% | Postpaid customers do not top up | Set to 0 |
| age_group | 1,649 | 11.0% | Age was not recorded | Labelled "Not stated" |

**About the missing ages.** The gap is not even across customer types. Age is missing for 18.3 percent of prepaid customers but only 3.0 percent of postpaid customers. This matches how real telecom data often looks, because prepaid customers can sign up with less information. Age is not used to build the segments, so the gap does not affect how customers are grouped. It only affects how well the age of each segment can be described, and the "Not stated" group is shown openly in the profiles.

**About gender.** 616 customers (4.1 percent) have gender marked "Not stated". This is stored as a value, not as an empty cell. Gender is used only for a fairness check after the segments are made.

### 4.3 Repeated records and wrong plan records

- **Repeated records.** 60 customer IDs appeared twice. The extra copies were removed.
- **Wrong plan allowances.** In 33 records, the data or call allowance did not match the plan name. For example, a Basic plan customer showing the allowance of a Plus plan. All three plan fields (price, data allowance, call allowance) were checked against the plan table, and the plan name was treated as correct.

### 4.4 Extreme values

Usage is heavily skewed. Most customers use little, and a small group uses many times more than a typical customer.

| Field | Typical customer (median) | 99th percentile | Largest value |
|---|---|---|---|
| Mobile data per month (GB) | 6.9 | 54.3 | 119.4 |
| Call minutes per month | 167.7 | 1,190.7 | 1,500.0 |
| Texts per month | 64.0 | 298.4 | 500.0 |
| Home broadband data (GB) | 107.2 | 336.9 | 777.3 |

These figures are from the file before cleaning. The largest values are far from the typical customer, for example 119 GB of mobile data against a median of 7 GB. They are plausible, such as business users, so the rows were kept. The limit was applied only to the copy of the data used for grouping.

---

## 5. How the Data Was Prepared for Grouping

### 5.1 New measures

Five measures were worked out from existing fields (requirement FR4), plus two Yes or No fields turned into 1 or 0.

| Measure | How it is worked out |
|---|---|
| data_use_ratio | Mobile data used divided by the data allowance |
| voice_use_ratio | Call minutes used divided by the call allowance |
| topup_value_per_month | Top-ups per month multiplied by average top-up amount |
| promo_response_rate | Promotions accepted divided by promotions received |
| has_upgraded | 1 if the customer upgraded in the last 24 months, otherwise 0 |
| is_prepaid | 1 if the account is prepaid, otherwise 0 |
| has_broadband | 1 if the customer has home broadband, otherwise 0 |

### 5.2 Choosing the features

Only behavior fields were used to build the segments. Age, area, region, sign-up channel, current plan, and gender were left out, so the groups come from behavior. They are used afterwards to describe the segments. This gave 21 candidate features.

**Removing repeated information.** If two features move together almost perfectly, the grouping method counts the same information twice. Three pairs had a correlation above 0.8.

| Pair | Correlation | Decision | Reason |
|---|---|---|---|
| broadband_gb and has_broadband | 0.88 | Dropped has_broadband | Broadband use is 0 when there is no broadband, so it already shows who has it. |
| promo_response_rate and promos_accepted_6m | 0.85 | Dropped promos_accepted_6m | The response rate already contains the number accepted. |
| is_prepaid and topup_value_per_month | 0.81 | Kept both | Top-up value is 0 for every postpaid customer, which explains the link. Among prepaid customers it also shows spending size. |

The final list has 19 features.

### 5.3 Limiting extreme values

For 12 heavy-tailed fields (usage, spending, top-ups, bundles, roaming, broadband, and the two use ratios), any value above the 99th percentile was set to the 99th percentile value. This was done on a separate copy, so the clean table and the segment profiles keep the real values.

- Between 103 and 150 values were limited in each of the 12 fields.
- In total, 1,484 customers (10 percent) had at least one value limited. Almost all of them had only one or two.

### 5.4 Scaling

Call minutes run into the hundreds, while a Yes or No flag is only 0 or 1. The grouping method measures distance, so large numbers would dominate. Every feature was scaled to an average of 0 and a spread of 1 (requirement FR5). The notebook checks this by printing the mean and spread of every scaled feature.

---

## 6. Privacy Check

- The dataset contains no names, phone numbers, addresses, or national ID numbers (requirement FR15).
- Customer IDs are made up.
- Every field used has a written purpose in the data dictionary (requirement FR16).
- Gender is the only sensitive field. It is kept out of the segmentation and used only for a fairness check.

---

## 7. Limits of This Review

- **The data is synthetic.** The problems were added on purpose by the data generator, so they are tidier than real problems. Real data would need more checks, such as impossible dates, customer IDs that do not match between systems, and values entered in different units.
- **Some choices affect the results.** The main ones are limiting values at the 99th percentile, setting empty broadband and top-up fields to 0, and treating missing ages as a "Not stated" group. They are reasonable and explained, but other choices would give slightly different segments.
- **No test of other choices.** We did not test how much the segments change if these choices are made differently. This could be a future improvement.

---

## 8. Requirements Covered

| Requirement | Status |
|---|---|
| FR1 Combine the data sources | Not needed, because the synthetic table is already combined (section 3) |
| FR2 Check data quality | Done (section 4) |
| FR3 Document how each problem was handled | Done (section 4) |
| FR4 Create customer measures | Done (section 5.1) |
| FR5 Put measures on a similar scale | Done (section 5.4) |
| FR15 Remove direct personal details | Done (section 6) |
| FR16 Give a reason for each field used | Done (section 6 and document 04) |
