# TelcoX Customer Segmentation

A business systems analyst case study. TelcoX, a fictional telecom company, wants to send each customer promotions that fit how they use their services, and to find the customers most ready to move to a higher plan. This project groups 15,000 customers by behavior with K-means clustering, ranks the groups by upgrade potential, recommends an offer for each, and defines a fair test to prove the approach works.

> TelcoX is fictional and all data is synthetic. It was created by a script in this repository. No real customer information is used.

## Key findings

| Finding | Result |
|---|---|
| Customer segments | Five, built from usage, spending, and promotion behavior |
| Customers who have outgrown their plan | 7,206 (48% of all customers) |
| Best place to start | Heavy Data Users: 99% use more data than their plan allows |
| Stability | At least 99.3% of customers kept their segment in 20 subsample tests |
| Honest caveat | The segments overlap (silhouette score 0.157), so they are a practical way to divide customers, not natural separate groups |

| Segment | Share | Upgrade rank |
|---|---|---|
| Heavy Data Users | 12.3% | 1 |
| Long-Term Voice Users | 8.1% | 2 |
| Deal-Seeking Prepaid Users | 18.3% | 3 |
| Steady Postpaid Households | 34.2% | 4 |
| Light Prepaid Users | 27.0% | 5 |

## Start here

- **Full report (PDF):** [reports/TelcoX_case_study.pdf](reports/TelcoX_case_study.pdf), about 56 pages covering every deliverable.
- **Executive summary (7 slides):** [hosted deck](https://claude.ai/artifact/XnDcURtWjSR2HB4D9DR2Dj). A local copy is in `presentation/telcox_executive_summary.html`.
- **Segment dashboard:** a Next.js app in [dashboard/](dashboard/), built as a static site (see "Run the dashboard" below). The first version is also available as a [hosted page](https://claude.ai/artifact/DvB1ri26T4NPXG9Pvk9Y8Z).
- **Analysis code:** [notebooks/segmentation_analysis.ipynb](notebooks/segmentation_analysis.ipynb), with a plain-language explanation before every step.

## Documents

| # | Document | What it covers |
|---|---|---|
| 01 | [Business Requirements](docs/01_business_requirements.md) | Problem, goals, scope, constraints |
| 02 | [Stakeholder Analysis](docs/02_stakeholder_analysis.md) | Who is affected, what they need, communication plan |
| 03 | [Requirements and User Stories](docs/03_requirements_and_user_stories.md) | Functional and quality requirements, user stories with acceptance criteria |
| 04 | [Data Dictionary](docs/04_data_dictionary.md) | Every field, its meaning, source, and use |
| 05 | [Data Quality and Preparation Report](docs/05_data_quality_and_preparation_report.md) | Problems found and how each was handled |
| 06 | [Segmentation Analysis Summary](docs/06_segmentation_analysis_summary.md) | Plain-language summary of the notebook |
| 07 | [Segment Profiles](docs/07_segment_profiles.md) | One page per segment |
| 08 | [Marketing Recommendations](docs/08_marketing_recommendations.md) | Offer, channel, and timing per segment, plus shop and care guides |
| 09 | [KPI and Measurement Plan](docs/09_kpi_and_measurement_plan.md) | Measures, baselines, fair test, targets, decision rule |
| 10 | Executive summary | Hosted deck (see above) |
| 11 | [Process Flow](docs/11_process_flow.md) | Current and proposed campaign process |
| 12 | [Risk and Limitations Log](docs/12_risk_and_limitations_log.md) | Risks, ratings, and what reduces them |
| 13 | [Implementation and Maintenance Plan](docs/13_implementation_and_maintenance_plan.md) | Phases, roles, and quarterly upkeep |

## Repository structure

```
telcox-customer-segmentation/
├── README.md
├── requirements.txt
├── docs/            documents 01 to 09 and 11 to 13
├── data/            synthetic customer data and analysis outputs
├── notebooks/       segmentation_analysis.ipynb
├── src/             generate_telcox_data.py
├── reports/         TelcoX_case_study.pdf and figures/
├── presentation/    executive summary deck (HTML)
└── dashboard/       segment dashboard (Next.js app)
```

## How to run it

You need Python 3.10 or later. It was tested with Python 3.12.

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate

# 2. Install the packages
pip install -r requirements.txt

# 3. Create the synthetic data (run from the repository root)
python src/generate_telcox_data.py

# 4. Open JupyterLab, then open notebooks/segmentation_analysis.ipynb and choose Run All
jupyter lab
```

The notebook reads `../data/telcox_customers.csv`, so it must stay in the `notebooks` folder. A fixed random seed (42) means the results are the same every time. The names and numbers in the documents belong to this seed.

## Run the dashboard

The dashboard needs Node.js (a current LTS version). It is separate from the Python analysis.

```bash
cd dashboard
npm install
npm run dev          # opens at http://localhost:3000
npm run build        # writes a static site to dashboard/out
```

It reads `dashboard/src/data/segments.json`, which holds segment-level totals only and no customer rows.

## Method in brief

1. **Prepare the data.** Remove repeated records, correct wrong plan records, fill empty fields by clear rules, create five new measures, limit extreme values, and scale every feature.
2. **Choose the number of segments.** Test 2 to 10 groups using the elbow method, silhouette score, and stability. Five was chosen because it meets every requirement.
3. **Build and check the segments.** K-means with five groups, tested on 20 random subsamples.
4. **Profile and rank.** Name each segment, rank by upgrade potential (need, past upgrades, and response to promotions), and test whether six segments would be better.

## Limitations

- The data is synthetic, so the results show the method and do not describe real customers.
- The segments overlap, and the upgrade ranking depends on the chosen weights.
- Whether the recommended offers raise upgrades is only known after the fair test described in document 09.

## Author

Walusungu Nyirenda
