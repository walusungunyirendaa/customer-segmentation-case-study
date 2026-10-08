"""
TelcoX synthetic customer data generator
========================================

Creates a fictional customer table for the TelcoX customer segmentation
case study. No real customer data is used.

What the script does, in plain steps:
    1. Gives each customer a hidden "behavior type" (for example, a heavy
       data user or a light basic user). Types are mixed, so customers do
       not fall into perfectly separate boxes.
    2. Creates every field listed in the data dictionary (document 04),
       using the hidden type to shape the values, plus random noise.
    3. Adds the data problems described in section 7 of the data
       dictionary: missing values, a few extreme users, duplicate rows,
       and a few inconsistent plan records.
    4. Saves the table as a CSV file.

The hidden behavior type is NOT saved in the main file, so the analysis
stays a fair test. It can be saved to a separate file with --save-truth,
to be opened only after the clustering is finished.

How to run:
    python src/generate_telcox_data.py
    python src/generate_telcox_data.py --n 15000 --seed 42 --outdir data

The same seed always gives the same data.
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


GROUPS = [
    "light_basic",        
    "voice_focused",      
    "data_streamers",     
    "home_bundlers",      
    "premium_business",   
    "deal_seekers",      
]

SHARES = [0.30, 0.15, 0.20, 0.12, 0.08, 0.15]       

PREPAID_PROB = [0.75, 0.35, 0.55, 0.05, 0.05, 0.95]
TENURE_MEAN = [30, 60, 20, 55, 50, 18]               
BROADBAND_PROB = [0.05, 0.10, 0.15, 0.95, 0.35, 0.05]
URBAN_PROB = [0.50, 0.45, 0.75, 0.60, 0.80, 0.50]

DATA_GB_MEAN = [2.0, 3.0, 28.0, 12.0, 22.0, 7.0]     
VOICE_MIN_MEAN = [70, 650, 150, 280, 500, 130]
SMS_MEAN = [40, 60, 120, 80, 50, 150]
OFFPEAK_MEAN = [0.30, 0.25, 0.55, 0.45, 0.20, 0.40]  
ROAMING_PROB = [0.02, 0.03, 0.05, 0.08, 0.55, 0.02]
ROAMING_DAYS_MEAN = [3, 3, 4, 4, 9, 3]

BUNDLES_3M_MEAN = [0.3, 0.5, 3.5, 1.0, 1.0, 6.0]
TOPUPS_PER_MONTH_MEAN = [1.5, 2.0, 3.0, 1.5, 2.0, 6.0]
LATE_PAYMENTS_MEAN = [0.8, 0.3, 0.6, 0.2, 0.1, 0.5]
UPGRADES_MEAN = [0.05, 0.10, 0.35, 0.25, 0.50, 0.15]
PROMO_ACCEPT_PROB = [0.03, 0.06, 0.22, 0.10, 0.08, 0.30]

PLAN_LABELS = ["Basic", "Standard", "Plus", "Premium"]
PLAN_PROBS = [
    [0.70, 0.25, 0.04, 0.01],
    [0.30, 0.50, 0.17, 0.03],
    [0.35, 0.40, 0.20, 0.05],
    [0.05, 0.35, 0.45, 0.15],
    [0.01, 0.09, 0.35, 0.55],
    [0.55, 0.35, 0.09, 0.01],
]

AGE_LABELS = ["18-24", "25-34", "35-44", "45-54", "55+"]
AGE_PROBS = [
    [0.15, 0.25, 0.22, 0.18, 0.20],
    [0.03, 0.10, 0.20, 0.27, 0.40],
    [0.40, 0.35, 0.15, 0.07, 0.03],
    [0.04, 0.20, 0.36, 0.28, 0.12],
    [0.02, 0.18, 0.33, 0.30, 0.17],
    [0.30, 0.35, 0.20, 0.10, 0.05],
]

CHANNEL_LABELS = ["Retail shop", "Mobile app", "Self-service", "Reseller"]
CHANNEL_PROBS = [
    [0.40, 0.15, 0.15, 0.30],
    [0.55, 0.10, 0.15, 0.20],
    [0.15, 0.50, 0.25, 0.10],
    [0.50, 0.20, 0.20, 0.10],
    [0.45, 0.35, 0.15, 0.05],
    [0.20, 0.20, 0.20, 0.40],
]

REGION_LABELS = ["North", "South", "East", "West", "Central"]
REGION_PROBS = [0.18, 0.22, 0.17, 0.20, 0.23]

PLAN_TABLE = {
    "Basic":    {"price": 10, "data_gb": 5,   "voice_min": 100},
    "Standard": {"price": 20, "data_gb": 15,  "voice_min": 300},
    "Plus":     {"price": 35, "data_gb": 40,  "voice_min": 600},
    "Premium":  {"price": 55, "data_gb": 100, "voice_min": 1000},
}

OUTLIER_RATE = 0.006          
WRONG_ALLOWANCE_RATE = 0.003  
DUPLICATE_RATE = 0.004        
MISSING_AGE_PREPAID = 0.18
MISSING_AGE_POSTPAID = 0.03
GENDER_NOT_STATED = 0.04



def blend(weights, values):
    return weights @ np.asarray(values, dtype=float)


def lognormal_around(rng, mean, sigma):
    mean = np.asarray(mean, dtype=float)
    return rng.lognormal(np.log(mean) - sigma ** 2 / 2, sigma)


def pick_category(rng, probs, labels):
    cumulative = probs.cumsum(axis=1)
    draws = rng.random((len(probs), 1))
    index = np.minimum((draws > cumulative).sum(axis=1), len(labels) - 1)
    return np.asarray(labels)[index]



def generate(n, seed):
    rng = np.random.default_rng(seed)
    k = len(GROUPS)

    primary = rng.choice(k, size=n, p=SHARES)
    secondary = rng.integers(0, k, size=n)
    mix = rng.beta(1.2, 6.0, size=n)  
    w = np.zeros((n, k))
    w[np.arange(n), primary] += 1 - mix
    w[np.arange(n), secondary] += mix

    is_prepaid = rng.random(n) < blend(w, PREPAID_PROB)
    account_type = np.where(is_prepaid, "Prepaid", "Postpaid")
    tenure = np.clip(
        np.round(rng.gamma(2.0, blend(w, TENURE_MEAN) / 2.0)), 1, 120
    ).astype(int)
    current_plan = pick_category(rng, w @ np.array(PLAN_PROBS), PLAN_LABELS)
    plan_price = np.array([PLAN_TABLE[p]["price"] for p in current_plan])
    plan_data = np.array([PLAN_TABLE[p]["data_gb"] for p in current_plan])
    plan_voice = np.array([PLAN_TABLE[p]["voice_min"] for p in current_plan])
    has_broadband = rng.random(n) < blend(w, BROADBAND_PROB)

    is_outlier = rng.random(n) < OUTLIER_RATE

    data_mean = blend(w, DATA_GB_MEAN) * np.where(
        is_outlier, rng.uniform(3, 4, n), 1.0
    )
    customer_data = lognormal_around(rng, data_mean, 0.45)
    monthly_data = customer_data[:, None] * lognormal_around(
        rng, np.ones((n, 3)), 0.25
    )
    monthly_data = np.clip(monthly_data, 0.05, 120)
    avg_data = monthly_data.mean(axis=1)
    months_over_limit = (monthly_data > plan_data[:, None]).sum(axis=1)

    voice_mean = blend(w, VOICE_MIN_MEAN) * np.where(
        is_outlier, rng.uniform(2, 3, n), 1.0
    )
    avg_voice = np.clip(lognormal_around(rng, voice_mean, 0.5), 0, 1500)

    avg_sms = np.clip(
        rng.poisson(lognormal_around(rng, blend(w, SMS_MEAN), 0.5)), 0, 500
    )

    offpeak_mean = blend(w, OFFPEAK_MEAN)
    concentration = 12.0
    offpeak = rng.beta(offpeak_mean * concentration,
                       (1 - offpeak_mean) * concentration)

    roams = rng.random(n) < blend(w, ROAMING_PROB)
    roaming_days = np.where(
        roams,
        np.clip(1 + rng.poisson(blend(w, ROAMING_DAYS_MEAN)), 1, 90),
        0,
    )

    broadband_gb = np.where(
        has_broadband,
        np.clip(lognormal_around(rng, np.full(n, 120.0), 0.5), 20, 800),
        np.nan,
    )

    bundles = np.clip(rng.poisson(blend(w, BUNDLES_3M_MEAN)), 0, 15)

    spend = (
        plan_price * lognormal_around(rng, np.ones(n), 0.15)
        + bundles / 3 * 5
        + months_over_limit / 3 * 6
    )
    spend = np.clip(spend, 2, 120)

    topups = np.clip(
        lognormal_around(rng, blend(w, TOPUPS_PER_MONTH_MEAN), 0.4), 0.5, 12
    )
    topup_amount = np.clip(
        spend / topups * lognormal_around(rng, np.ones(n), 0.1), 1, 50
    )
    topups = np.where(is_prepaid, topups, np.nan)
    topup_amount = np.where(is_prepaid, topup_amount, np.nan)

    late_payments = np.where(
        is_prepaid,
        np.nan,
        np.clip(rng.poisson(blend(w, LATE_PAYMENTS_MEAN)), 0, 6),
    )

    upgrades = np.clip(rng.poisson(blend(w, UPGRADES_MEAN)), 0, 3)
    months_since_upgrade = np.where(
        upgrades > 0, rng.integers(1, 25, size=n), np.nan
    )

    promos_received = np.clip(rng.poisson(5, size=n), 0, 12)
    promos_accepted = rng.binomial(promos_received,
                                   blend(w, PROMO_ACCEPT_PROB))

    age_group = pick_category(rng, w @ np.array(AGE_PROBS), AGE_LABELS)
    missing_age_rate = np.where(is_prepaid, MISSING_AGE_PREPAID,
                                MISSING_AGE_POSTPAID)
    age_group = np.where(rng.random(n) < missing_age_rate, None, age_group)

    gender = rng.choice(["Female", "Male"], size=n)
    gender = np.where(rng.random(n) < GENDER_NOT_STATED, "Not stated", gender)

    area_type = np.where(rng.random(n) < blend(w, URBAN_PROB),
                         "Urban", "Rural")
    region = rng.choice(REGION_LABELS, size=n, p=REGION_PROBS)
    channel = pick_category(rng, w @ np.array(CHANNEL_PROBS), CHANNEL_LABELS)

    df = pd.DataFrame({
        "customer_id": [f"TX{i:06d}" for i in range(1, n + 1)],
        "age_group": age_group,
        "gender": gender,
        "area_type": area_type,
        "region": region,
        "registration_channel": channel,
        "account_type": account_type,
        "tenure_months": tenure,
        "current_plan": current_plan,
        "plan_price": plan_price,
        "plan_data_gb": plan_data,
        "plan_voice_min": plan_voice,
        "has_home_broadband": np.where(has_broadband, "Yes", "No"),
        "avg_data_gb": avg_data.round(2),
        "avg_voice_min": avg_voice.round(1),
        "avg_sms": avg_sms,
        "offpeak_share": offpeak.round(2),
        "roaming_days_3m": roaming_days,
        "broadband_gb": np.round(broadband_gb, 1),
        "months_over_data_limit": months_over_limit,
        "avg_monthly_spend": spend.round(2),
        "topups_per_month": np.round(topups, 1),
        "avg_topup_amount": np.round(topup_amount, 2),
        "bundle_purchases_3m": bundles,
        "late_payments_6m": late_payments,
        "upgrades_24m": upgrades,
        "months_since_last_upgrade": months_since_upgrade,
        "promos_received_6m": promos_received,
        "promos_accepted_6m": promos_accepted,
    })

   
    for col in ["late_payments_6m", "months_since_last_upgrade"]:
        df[col] = df[col].astype("Int64")

    truth = pd.DataFrame({
        "customer_id": df["customer_id"],
        "hidden_group": np.asarray(GROUPS)[primary],
    })

    
    wrong = rng.random(n) < WRONG_ALLOWANCE_RATE
    allowed = np.array([5, 15, 40, 100])
    df.loc[wrong, "plan_data_gb"] = rng.choice(allowed, size=wrong.sum())

    n_dup = int(round(n * DUPLICATE_RATE))
    duplicates = df.sample(n=n_dup, random_state=seed)
    df = pd.concat([df, duplicates], ignore_index=True)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    return df, truth



def main():
    parser = argparse.ArgumentParser(description="Generate TelcoX data")
    parser.add_argument("--n", type=int, default=15000,
                        help="number of customers (default 15000)")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--outdir", default="data",
                        help="folder for the CSV file (default data)")
    parser.add_argument("--save-truth", action="store_true",
                        help="also save the hidden behavior types")
    args = parser.parse_args()

    df, truth = generate(args.n, args.seed)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir / "telcox_customers.csv", index=False)
    print(f"Saved {len(df)} rows to {outdir / 'telcox_customers.csv'}")

    if args.save_truth:
        truth.to_csv(outdir / "telcox_hidden_groups.csv", index=False)
        print("Saved hidden groups. Open only after the clustering is done.")


if __name__ == "__main__":
    main()
