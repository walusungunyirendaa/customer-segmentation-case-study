# TelcoX Customer Segmentation: Data Dictionary

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 04 Data Dictionary |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 01 Business Requirements, 03 Requirements and User Stories |

---

## 1. Purpose of This Document

This document lists every data field used in the project. For each field it explains what the field means, what values to expect, where the data comes from, and how it will be used. Anyone reading the analysis can use this document to understand the data without asking questions.

It supports requirement FR16 (list why each field is needed) and quality requirement NFR5 (every field is documented).

---

## 2. About the Dataset

| Item | Description |
|---|---|
| **Dataset name** | TelcoX customer table |
| **Type** | Synthetic (created by the script `src/generate_telcox_data.py` with a fixed random seed of 42, not real customer data) |
| **Size** | 15,000 customers (15,060 rows, because a few records are repeated on purpose) |
| **One row means** | One customer |
| **Time period** | A snapshot at the end of one month. Usage and spending are averages of the last three months. |
| **Currency** | All amounts are in "currency units" so the case study is not tied to one country. |
| **Source systems** | Customer database (CRM), billing, network usage records, campaign tool |

All customers are linked by one customer ID. The ID is made up and does not point to any real person.

---

## 3. Plan Tiers

Each customer is on one of four plans. These are used to work out whether a customer is using more than their plan allows.

| Plan | Monthly price | Data allowance (GB) | Voice allowance (minutes) |
|---|---|---|---|
| Basic | 10 | 5 | 100 |
| Standard | 20 | 15 | 300 |
| Plus | 35 | 40 | 600 |
| Premium | 55 | 100 | 1,000 |

---

## 4. Field List

### 4.1 Identifier

| Field | Meaning | Type | Example values | Source | Used for |
|---|---|---|---|---|---|
| customer_id | A made-up code that identifies one customer. | Text | TX000001 | CRM | Joining tables only |

### 4.2 Demographic fields

| Field | Meaning | Type | Example values | Source | Used for | Sensitive |
|---|---|---|---|---|---|---|
| age_group | The customer's age band. | Category | 18-24, 25-34, 35-44, 45-54, 55+ | CRM | Profiling | No |
| gender | The customer's gender as recorded. | Category | Female, Male, Not stated | CRM | Fairness check only | Yes |
| area_type | Whether the customer lives in a city or a rural area. | Category | Urban, Rural | CRM | Profiling | No |
| region | The part of the country where the customer lives. | Category | North, South, East, West, Central | CRM | Profiling | No |
| registration_channel | How the customer first signed up. | Category | Retail shop, Mobile app, Self-service, Reseller | CRM | Profiling | No |

### 4.3 Account fields

| Field | Meaning | Type | Example values | Source | Used for | Sensitive |
|---|---|---|---|---|---|---|
| account_type | Whether the customer pays before use or after use. | Category | Prepaid, Postpaid | CRM | Segmentation | No |
| tenure_months | Number of months as a TelcoX customer. | Whole number | 1 to 120 | CRM | Segmentation | No |
| current_plan | The plan the customer is on now. | Category | Basic, Standard, Plus, Premium | Billing | Segmentation | No |
| plan_price | Monthly price of the current plan. | Number | 10, 20, 35, 55 | Billing | Working out ratios | No |
| plan_data_gb | Monthly data allowance of the current plan. | Number | 5, 15, 40, 100 | Billing | Working out ratios | No |
| plan_voice_min | Monthly voice allowance of the current plan. | Whole number | 100, 300, 600, 1000 | Billing | Working out ratios | No |
| has_home_broadband | Whether the customer also has a home broadband service. | Yes or No | Yes, No | Billing | Segmentation | No |

### 4.4 Usage fields

All usage fields are monthly averages over the last three months.

| Field | Meaning | Type | Example values | Source | Used for |
|---|---|---|---|---|---|
| avg_data_gb | Mobile data used per month, in gigabytes. | Number | 0.2 to 120 | Network records | Segmentation |
| avg_voice_min | Call minutes used per month. | Number | 0 to 1,500 | Network records | Segmentation |
| avg_sms | Text messages sent per month. | Whole number | 0 to 500 | Network records | Segmentation |
| offpeak_share | Share of usage that happens at off-peak times (night and weekends). 0 means none, 1 means all. | Number | 0.00 to 1.00 | Network records | Segmentation |
| roaming_days_3m | Number of days the customer used the service abroad in the last three months. | Whole number | 0 to 90 | Network records | Segmentation |
| broadband_gb | Home broadband data used per month. Empty if the customer has no broadband. | Number | 20 to 800 | Network records | Segmentation |
| months_over_data_limit | Number of the last three months in which data use went above the plan allowance. | Whole number | 0 to 3 | Network records | Segmentation |

### 4.5 Transaction fields

| Field | Meaning | Type | Example values | Source | Used for |
|---|---|---|---|---|---|
| avg_monthly_spend | Average amount the customer pays per month. | Number | 2 to 120 | Billing | Segmentation |
| topups_per_month | How many times the customer tops up each month. Empty for postpaid customers. | Number | 0.5 to 12 | Billing | Segmentation |
| avg_topup_amount | Average value of one top-up. Empty for postpaid customers. | Number | 1 to 50 | Billing | Segmentation |
| bundle_purchases_3m | Number of extra bundles bought in the last three months. | Whole number | 0 to 15 | Billing | Segmentation |
| late_payments_6m | Number of late bill payments in the last six months. Empty for prepaid customers. | Whole number | 0 to 6 | Billing | Profiling |

### 4.6 Plan change and campaign fields

| Field | Meaning | Type | Example values | Source | Used for |
|---|---|---|---|---|---|
| upgrades_24m | Number of times the customer moved to a higher plan in the last 24 months. | Whole number | 0 to 3 | CRM | Upgrade potential |
| months_since_last_upgrade | Months since the last upgrade. Empty if the customer never upgraded. | Whole number | 1 to 24 | CRM | Upgrade potential |
| promos_received_6m | Number of promotions sent to the customer in the last six months. | Whole number | 0 to 12 | Campaign tool | Segmentation |
| promos_accepted_6m | Number of those promotions the customer accepted. | Whole number | 0 to 12 | Campaign tool | Segmentation |

---

## 5. Measures Created From the Fields

Some of the most useful measures are not in the raw data. They are worked out from the fields above during data preparation (requirement FR4).

| Measure | How it is worked out | What it tells us |
|---|---|---|
| data_use_ratio | avg_data_gb divided by plan_data_gb | How much of the data allowance the customer uses. A value above 1 means the customer goes over the limit. |
| voice_use_ratio | avg_voice_min divided by plan_voice_min | How much of the voice allowance the customer uses. |
| topup_value_per_month | topups_per_month multiplied by avg_topup_amount | Total top-up spending per month for prepaid customers. |
| promo_response_rate | promos_accepted_6m divided by promos_received_6m | How often the customer says yes to offers. Empty if no promotions were received. |
| has_upgraded | 1 if upgrades_24m is above 0, otherwise 0 | Whether the customer has upgraded before. |

---

## 6. Which Fields Are Used Where

To keep the segments based on behavior, the analysis separates fields into four groups.

| Group | Fields | Role |
|---|---|---|
| **Used to create segments** | Usage fields, transaction fields (except late payments), account type, tenure, home broadband use (`broadband_gb`, with 0 for no broadband), the measures in section 5, promos received, and promo response rate | These decide which customers are grouped together. |
| **Used to describe segments** | Age group, area type, region, registration channel, current plan, late payments | Checked after the segments are made, to explain who is in each group. |
| **Used for upgrade potential** | data_use_ratio, voice_use_ratio, months_over_data_limit, upgrades_24m, months_since_last_upgrade, promo_response_rate | Combined to rank segments by how ready they are to upgrade. |
| **Not used in the analysis** | customer_id (only for joining), gender (only for a fairness check after segments are made) | Kept out so segments do not depend on personal traits. |

---

## 7. Expected Data Quality Issues

The dataset is built to include the kinds of problems found in real data, so that the preparation work in requirement FR2 is meaningful.

| Field or issue | What to expect | Planned handling |
|---|---|---|
| age_group | Missing for a share of prepaid customers. | Keep as a "Not stated" group, because removing these customers would lose a large part of the prepaid base. |
| gender | Some records marked "Not stated". | Keep as a separate value. |
| topups_per_month, avg_topup_amount | Empty for postpaid customers by design. | Not an error. Handle by account type. |
| late_payments_6m | Empty for prepaid customers by design. | Not an error. Handle by account type. |
| broadband_gb | Empty for customers without broadband by design. | Fill with 0 for analysis. |
| avg_data_gb, avg_voice_min | A small number of very high values (heavy business users). | Review them, then decide whether to keep, cap, or analyze separately. |
| Duplicate rows | A few repeated customer records. | Remove duplicates and record how many were removed. |
| Inconsistent values | A few records where the plan allowance does not match the plan name. | Correct using the plan table in section 3. |

---

## 8. Privacy Notes

- The dataset contains no names, phone numbers, addresses, or national ID numbers.
- Every customer ID is made up.
- Gender is the only sensitive field. It is not used to create segments.
- Because the data is synthetic, no real person can be identified from it. In a real project, the same fields would still need approval from the legal and compliance team (see US12).

