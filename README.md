
# Neuro Longevity Analysis: Predicting Biological Brain Age

An end-to-end neuroinformatics and SQL analytics pipeline designed to evaluate cognitive trajectory and biological brain age from structural MRI datasets. By comparing chronological age against predicted biological brain age, this framework quantifies neurodegenerative risk using the **Brain Age Gap Index (BAGI)**.

---

## 📌 Project Overview

* **Objective:** Quantify cognitive decline and accelerated brain aging through structural volume analytics.
* **Core Metric:** **Brain Age Gap Index (BAGI)** ($\text{BAGI} = \text{Predicted Brain Age} - \text{Chronological Age}$).
  * $\text{BAGI} > 0$: Accelerated brain aging (elevated risk profile).
  * $\text{BAGI} \le 0$: Healthy/resilient brain aging trajectory.
* **Stack:** Python (Pandas, Seaborn, Matplotlib), SQL (Schema DDL, Feature Extraction, Group Aggregations), Git/GitHub.

---

## 📁 Repository Structure

```text
neuro-longevity-analysis/
├── assets/                             # Output visualizations
│   ├── bagi_distribution_boxplot.png
│   └── brain_age_scatter.png
├── queries/                            # SQL analytical queries
│   ├── 02_feature_extraction.sql
│   └── 03_brain_age_gap_analysis.sql
├── schema/                             # Database initialization scripts
│   └── 01_schema_setup.sql
├── db_analysis.py                      # Core Python pipeline & visualization generator
├── .gitignore
└── README.md                           # Project documentation
