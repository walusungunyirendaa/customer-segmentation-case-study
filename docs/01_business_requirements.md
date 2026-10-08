# TelcoX Customer Segmentation: Business Requirements Document

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 01 Business Requirements Document (BRD) |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |

> **Note on this case study.** TelcoX is a fictional company. All data used in this project is public or synthetic. No real customer information is used.

---

## 1. Purpose of This Document

This document explains what TelcoX wants to achieve with customer segmentation, why it matters, and what the project must deliver. It is the starting point for all other project documents. It is written so that business and technical readers can both understand it.

---

## 2. Background

TelcoX is a mid-sized telecom company. It sells mobile voice, SMS, mobile data, and home broadband to several million customers. Customers are on either prepaid plans (pay before use) or postpaid plans (pay after use).

TelcoX operates in one country and reaches customers through retail shops, a mobile app, and a self-service channel such as USSD.

The telecom market is very competitive. Customers can switch to another provider easily, and competitors often run strong promotions.

Today, TelcoX marketing mostly sends the same offers to almost everyone. This approach has three problems:

- Response to campaigns is low.
- Promotion spending is high.
- Many customers get offers that do not match how they use their phone or internet.

---

## 3. Business Problem

TelcoX wants to target different groups of customers with promotions and services that suit them. It especially wants to find the groups most likely to upgrade or switch to a higher-tier plan.

At the moment:

- Average revenue per user (ARPU) has not grown. ARPU is the average amount each customer pays per month.
- Many customers stay on basic plans even though their usage suggests a bigger plan would suit them better.
- TelcoX has no data-based customer segmentation. Groups are defined only by plan type or how long someone has been a customer.
- Marketing, sales, and product teams each use a different meaning for "high-value customer."

### Key questions to answer

1. What different groups of customers exist, based on how they actually use TelcoX services?
2. Which groups are most likely to upgrade to a higher-tier plan?
3. What offers and services suit each group?

---

## 4. Project Goals

### Business goals

| # | Goal |
|---|---|
| B1 | Increase the number of customers who upgrade to higher-tier plans. |
| B2 | Improve how many customers respond to promotions. |
| B3 | Reduce money spent on offers that do not suit the customer. |
| B4 | Grow ARPU, especially in groups with unmet needs. |
| B5 | Give all teams one shared view of customer groups. |

### Analysis goals

| # | Goal |
|---|---|
| A1 | Find a small number of clear customer segments. |
| A2 | Describe each segment using demographics, behavior, and upgrade potential. |
| A3 | Turn each segment into a recommended marketing action. |

---

## 5. Scope

### In scope

- Collecting and cleaning customer data (demographics, usage, and transactions).
- Grouping customers into segments using K-means clustering.
- Describing each segment in plain business terms.
- Estimating which segments are most ready to upgrade.
- Recommending an offer, channel, and timing for each segment.
- Defining how success will be measured.

### Out of scope

- Building or changing TelcoX's live campaign or billing systems.
- Running real marketing campaigns.
- Setting new prices or designing new plans.
- Predicting customer churn (customers leaving) as a separate model.

Churn prediction is left out to keep the project focused on upgrade potential. It could be a future extension.

---

## 6. Stakeholders

| Stakeholder | What they need |
|---|---|
| Marketing | Clear groups they can target, and campaign guidance. |
| Product and pricing | To know if current plans match real customer usage. |
| Sales and retail | Simple segment descriptions that shop staff can use. |
| Customer care | To understand common problems for each segment. |
| IT and data teams | A clear list of data needed and how results will be used. |
| Leadership | Proof that the work improves upgrades, ARPU, and campaign returns. |

A fuller version of this table is in the next document, 02 Stakeholder Analysis.

---

## 7. Available Data

TelcoX holds three main types of customer data.

| Data type | Examples |
|---|---|
| **Demographic** | Age group, gender, location (city or rural, region), account type (prepaid or postpaid), time as a customer, how they signed up. |
| **Usage** | Monthly call minutes, SMS count, mobile data used, share of off-peak use, roaming use, home broadband use. |
| **Transaction** | How often and how much they top up, bill payments, bundle purchases, past plan changes, past promotion responses, late payments. |

The data sits in separate systems: billing, the customer database (CRM), network records, and the campaign tool. They share a customer ID but have not been combined, and data quality differs between them.

Some demographic details are missing for prepaid customers.

---

## 8. Business Requirements

These describe what the business needs from this project. Detailed user stories will follow in document 03.

| ID | Requirement | Priority |
|---|---|---|
| BR1 | The project must group customers into segments based on usage and behavior. | High |
| BR2 | Each segment must have a clear name and description that non-technical staff can understand. | High |
| BR3 | The project must show which segments are most likely to upgrade. | High |
| BR4 | Each segment must come with a suggested offer, channel, and timing. | High |
| BR5 | Segments must be easy for marketing and sales to reach and use. | High |
| BR6 | The project must follow data privacy rules and handle sensitive data with care. | High |
| BR7 | The project must explain how missing or unusual data was handled. | Medium |
| BR8 | The project must include a plan to measure success. | Medium |
| BR9 | The project should suggest how often segments should be reviewed. | Low |

---

## 9. Constraints and Risks

### Constraints

- **Privacy:** Customer data must be handled under data protection rules. Sensitive details should be used carefully.
- **Data quality:** Missing values, errors, and unusual cases (such as very heavy business users) must be handled before analysis.
- **Simplicity:** Results must be clear to people who are not data experts.
- **Usefulness:** A segment is only valuable if TelcoX can reach it with a different offer through an existing channel.

### Risks

| Risk | Possible effect | How to reduce it |
|---|---|---|
| Poor or missing data | Segments may be unreliable. | Check data early and record how problems were fixed. |
| Too many segments | Marketing cannot act on all of them. | Aim for a small number that are clearly different. |
| Segments are hard to explain | Teams will not use them. | Give each segment a simple name and short description. |
| Customer behavior changes | Segments become out of date. | Plan regular reviews. |
| Privacy concerns | Legal and trust problems. | Avoid sensitive details and keep data protected. |

---

## 10. Success Measures

| Measure | What it tells us |
|---|---|
| Promotion response rate by segment | Whether targeted offers work better than broad ones. |
| Upgrade rate among targeted customers | Whether segments help find customers ready to upgrade. |
| Change in ARPU | Whether revenue per customer grows. |
| Marketing cost per upgrade | Whether spending is more efficient. |
| Team use of segments | Whether marketing and sales actually use the segments. |

Target numbers are not set yet. They will be defined in document 09, the KPI and Measurement Plan.

---

## 11. Expected Deliverables

1. This Business Requirements Document
2. Stakeholder Analysis
3. Requirements and User Stories
4. Data Dictionary
5. Data Quality and Preparation Report
6. Segmentation Analysis (notebook)
7. Segment Profiles
8. Marketing Recommendations
9. KPI and Measurement Plan
10. Executive Summary Presentation

---

## 12. Approach in Brief

1. Collect and combine customer data.
2. Clean the data and create useful measures, such as average monthly data use.
3. Use K-means clustering to find groups of customers with similar behavior.
4. Describe and name each group.
5. Recommend a marketing action for each group.
6. Define how results will be measured.

K-means is a method that sorts customers into groups so that people in the same group behave alike and people in different groups behave differently. The groups come from the data itself, not from labels set in advance.

---

## 13. Approval

| Name | Role | Date | Status |
|---|---|---|---|
| | Marketing lead | | Pending |
| | Product lead | | Pending |
| | Data team lead | | Pending |

Approvals are shown as placeholders to demonstrate a normal BRD process.
