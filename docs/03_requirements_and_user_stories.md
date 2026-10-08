# TelcoX Customer Segmentation: Requirements and User Stories

| | |
|---|---|
| **Project name** | TelcoX Customer Segmentation |
| **Document** | 03 Requirements and User Stories |
| **Prepared by** | Walusungu Nyirenda |
| **Role** | Business Systems Analyst (case study) |
| **Related documents** | 01 Business Requirements, 02 Stakeholder Analysis |

---

## 1. Purpose of This Document

The Business Requirements Document explains what TelcoX wants. This document explains what the project must do to deliver it. It turns each business need into specific requirements and user stories that can be checked one by one.

Each item has an ID, a priority, and a link back to the business requirement it supports.

---

## 2. How to Read This Document

### Priority levels

| Priority | Meaning |
|---|---|
| **Must have** | The project fails without it. |
| **Should have** | Important, but the project still works without it. |
| **Could have** | Useful extra, done only if time allows. |

### ID labels

| Label | Meaning |
|---|---|
| BR | Business requirement (from document 01) |
| FR | Functional requirement (what the project must do) |
| NFR | Quality requirement (how well it must be done) |
| US | User story (a need written from the user's point of view) |

---

## 3. Functional Requirements

### 3.1 Data preparation

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR1 | Combine data from billing, the customer database, network usage records, and the campaign tool, using the customer ID. | BR1, BR7 | Must have |
| FR2 | Check the data for missing values, duplicate records, and unusual values, and record what was found. | BR7 | Must have |
| FR3 | Decide and document how each data problem was handled (for example, removed, filled in, or kept). | BR7 | Must have |
| FR4 | Create customer measures from the raw data, such as average monthly data use, calls per month, top-up frequency, average top-up amount, and months as a customer. | BR1 | Must have |
| FR5 | Put all measures on a similar scale so that no single measure has more weight than the others. | BR1 | Must have |

### 3.2 Segmentation

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR6 | Test different numbers of segments and choose the best number using the elbow method and silhouette score. Explain the choice in simple words. | BR1 | Must have |
| FR7 | Run K-means clustering and place every customer in exactly one segment. | BR1 | Must have |
| FR8 | Run the model again with different starting points to check that the segments stay mostly the same. | BR1 | Should have |

### 3.3 Segment profiles and upgrade potential

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR9 | Describe each segment by size, typical usage, typical spending, and main demographics. | BR2 | Must have |
| FR10 | Give each segment a short, plain name and a description of two to three sentences. | BR2 | Must have |
| FR11 | Estimate the upgrade potential of each segment, using signs such as usage above the current plan limit and past upgrade behavior. Rank segments from highest to lowest potential. | BR3 | Must have |

### 3.4 Marketing actions

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR12 | Recommend an offer, a channel, and a timing for each segment. | BR4 | Must have |
| FR13 | Confirm that each recommended channel is one TelcoX already uses. | BR5 | Must have |
| FR14 | Provide a one-page guide for each segment that sales and retail staff can use. | BR5 | Should have |

### 3.5 Privacy

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR15 | Remove direct personal details (such as names and phone numbers) from the analysis data. | BR6 | Must have |
| FR16 | Use only the data fields that are needed, and list why each one is needed. | BR6 | Must have |

### 3.6 Measurement and reporting

| ID | Requirement | Linked to | Priority |
|---|---|---|---|
| FR17 | Define the measures of success (response rate, upgrade rate, ARPU change, cost per upgrade) and how each one is calculated. | BR8 | Must have |
| FR18 | Describe a test that compares targeted customers with a control group that receives the usual offer. | BR8 | Must have |
| FR19 | Present the findings in a short summary deck for non-technical readers. | BR2, BR8 | Must have |
| FR20 | Recommend how often segments should be refreshed. | BR9 | Could have |
| FR21 | Build a simple dashboard that shows segments with filters. | BR5 | Could have |

---

## 4. Quality Requirements

| ID | Requirement | How it will be checked | Priority |
|---|---|---|---|
| NFR1 | **Plain language.** All documents and segment descriptions must be understandable to a reader with no data background. | A non-technical reader can explain each segment in one sentence after reading. | Must have |
| NFR2 | **Repeatable results.** The notebook must give the same results each time it is run. | Run the notebook from start to finish twice and compare the segment sizes. | Must have |
| NFR3 | **Clear segments.** The number of segments must be small enough for marketing to act on. | The final model has between 4 and 6 segments. | Must have |
| NFR4 | **Meaningful segment size.** No segment should be too small to target. | Each segment holds at least 5 percent of customers. | Should have |
| NFR5 | **Documented data.** Every field used must be described in the data dictionary. | Each field in the notebook appears in document 04. | Must have |
| NFR6 | **Readable code.** The notebook must have short explanations before each step. | Each section starts with a plain description of what it does. | Should have |

---

## 5. User Stories

Each story follows this format: *As a [role], I want [need], so that [benefit].* The acceptance criteria are the checks that show the story is done.

### Epic A: Data preparation

**US1. Combined customer data** | Must have | Linked to FR1, FR4, FR5
*As an IT and data analyst, I want customer data from all sources joined into one table, so that every customer can be analyzed from a single view.*

Acceptance criteria:
- [ ] One row exists for each customer.
- [ ] Billing, usage, transaction, and demographic fields all appear in the table.
- [ ] The number of customers before and after joining is recorded.

**US2. Data quality findings** | Must have | Linked to FR2, FR3
*As a data team lead, I want a clear record of data problems and how they were fixed, so that I can trust the results.*

Acceptance criteria:
- [ ] Missing values are counted for each field.
- [ ] Duplicate records and unusual values are listed.
- [ ] Each fix is explained in one sentence.

### Epic B: Segmentation

**US3. Clear customer groups** | Must have | Linked to FR6, FR7
*As a marketing manager, I want customers placed into a small number of distinct groups, so that I can plan different campaigns for each group.*

Acceptance criteria:
- [ ] Every customer belongs to exactly one segment.
- [ ] The final model has between 4 and 6 segments.
- [ ] The reason for the chosen number is explained in simple words.

**US4. Trustworthy segments** | Should have | Linked to FR8, NFR2
*As a product manager, I want to know the segments are stable, so that I do not base plans on groups that change each time the analysis is run.*

Acceptance criteria:
- [ ] The model is run at least three times with different starting points.
- [ ] Segment sizes are compared across the runs.
- [ ] Any large differences are explained.

### Epic C: Segment profiles

**US5. Easy-to-understand segments** | Must have | Linked to FR9, FR10
*As a sales and retail agent, I want each segment to have a short name and description, so that I can quickly recognize which customers may suit an upgrade.*

Acceptance criteria:
- [ ] Each segment has a name of five words or fewer.
- [ ] Each segment has a description of two to three sentences.
- [ ] Descriptions use everyday words, with no technical terms.

**US6. Segment detail for marketing** | Must have | Linked to FR9
*As a marketing manager, I want to see the size, usage, spending, and demographics of each segment, so that I can understand who these customers are.*

Acceptance criteria:
- [ ] A profile table shows each segment side by side.
- [ ] Each profile shows the share of total customers.
- [ ] Each profile shows at least three usage or spending measures.

### Epic D: Upgrade potential

**US7. Upgrade ranking** | Must have | Linked to FR11
*As a leadership member, I want segments ranked by how ready they are to upgrade, so that budget goes to the groups most likely to respond.*

Acceptance criteria:
- [ ] Segments are ranked from highest to lowest upgrade potential.
- [ ] The signs used to judge potential are listed.
- [ ] The top-ranked segments are named in the summary deck.

**US8. Plan fit** | Should have | Linked to FR11
*As a product manager, I want to see which segments use more than their current plan allows, so that I can see where plans do not match real needs.*

Acceptance criteria:
- [ ] For each segment, the share of customers above their plan limits is shown.
- [ ] The segments with the largest gap are highlighted.

### Epic E: Marketing actions

**US9. Tailored offers** | Must have | Linked to FR12, FR13
*As a marketing manager, I want a suggested offer, channel, and timing for each segment, so that I can launch campaigns without starting from scratch.*

Acceptance criteria:
- [ ] Every segment has one offer, one channel, and one timing.
- [ ] Each recommendation explains in one sentence why it suits the segment.
- [ ] Every channel is one that TelcoX already uses.

**US10. Retail guide** | Should have | Linked to FR14
*As a retail agent, I want a one-page guide for each segment, so that I can make the right offer during a customer visit.*

Acceptance criteria:
- [ ] Each guide fits on one page.
- [ ] Each guide includes the segment description, a suggested offer, and one example conversation starter.

**US11. Customer care readiness** | Could have | Linked to FR12
*As a customer care agent, I want to know what questions each segment is likely to ask about an offer, so that I can answer quickly.*

Acceptance criteria:
- [ ] Each segment has at least two likely questions listed.

### Epic F: Privacy

**US12. Safe use of data** | Must have | Linked to FR15, FR16
*As a legal and compliance officer, I want only the needed data used and personal details removed, so that customer privacy is protected.*

Acceptance criteria:
- [ ] The analysis data contains no names, phone numbers, or addresses.
- [ ] Every data field used has a written reason.
- [ ] Sensitive fields are either left out or marked as sensitive with a reason for use.

### Epic G: Measurement

**US13. Measures of success** | Must have | Linked to FR17
*As a leadership member, I want clear measures of success, so that I can judge whether segmentation is worth continuing.*

Acceptance criteria:
- [ ] Response rate, upgrade rate, ARPU change, and cost per upgrade are each defined.
- [ ] Each definition includes how it is calculated.
- [ ] Each measure is compared against the current broad approach.

**US14. Fair test** | Must have | Linked to FR18
*As a marketing manager, I want a test that compares targeted offers with the usual offers, so that I can prove the new approach works.*

Acceptance criteria:
- [ ] The test has a targeted group and a control group.
- [ ] Group selection is described in simple steps.
- [ ] The test duration and the decision rule are stated.

**US15. Executive summary** | Must have | Linked to FR19
*As a leadership member, I want a short summary of the problem, findings, and recommendations, so that I can make a decision in a few minutes.*

Acceptance criteria:
- [ ] The deck is ten slides or fewer.
- [ ] It covers the problem, the segments, the ranking, the recommendations, and the next steps.
- [ ] It contains no technical terms without a short explanation.

**US16. Refresh plan** | Could have | Linked to FR20
*As a data team lead, I want to know how often segments should be updated, so that they stay accurate as customer behavior changes.*

Acceptance criteria:
- [ ] A refresh schedule is recommended with a reason.
- [ ] One sign that the segments are out of date is described.

---

## 6. Traceability

This table shows that every business requirement is covered by at least one functional requirement and one user story.

| Business requirement | Functional requirements | User stories |
|---|---|---|
| BR1 Group customers by behavior | FR1, FR4 to FR8 | US1, US3, US4 |
| BR2 Clear names and descriptions | FR9, FR10, FR19 | US5, US6, US15 |
| BR3 Show upgrade potential | FR11 | US7, US8 |
| BR4 Offer, channel, and timing | FR12 | US9, US11 |
| BR5 Easy for teams to use | FR13, FR14, FR21 | US9, US10 |
| BR6 Data privacy | FR15, FR16 | US12 |
| BR7 Explain data handling | FR1 to FR3 | US2 |
| BR8 Measurement plan | FR17 to FR19 | US13, US14, US15 |
| BR9 Review schedule | FR20 | US16 |

---

## 7. Project Completion Checklist

The project is complete when:

- [ ] All Must have requirements are met.
- [ ] All acceptance criteria for Must have user stories are checked off.
- [ ] Every business requirement appears in the traceability table.
- [ ] The notebook runs from start to finish and gives the same segments each time.
- [ ] The summary deck has been read by a non-technical person who could explain the segments back.
