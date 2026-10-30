
import os
import urllib.parse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Database Connection Parameters
DB_USER = "root"
DB_PASS = urllib.parse.quote_plus("Sharks199!")  # Safely encodes special characters
DB_HOST = "127.0.0.1"  # Using 127.0.0.1 forces TCP/IP instead of socket connection
DB_PORT = "3306"
DB_NAME = "neuro_longevity"
# Create SQLAlchemy Engine
connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# 2. Fetch Query Data from MySQL
query = """
SELECT 
    p.subject_id,
    p.chronological_age_at_scan AS chronological_age,
    p.predicted_brain_age,
    p.bagi_score,
    p.risk_category,
    s.cognitive_status,
    s.mmse_score
FROM brain_age_predictions p
JOIN subjects s ON p.subject_id = s.subject_id;
"""

print("Connecting to MySQL database...")
df = pd.read_sql(query, engine)
print("Data successfully loaded!")
print(df.head())

# 3. Create Asset Directory for Visualizations
os.makedirs("assets", exist_ok=True)

# Set Seaborn Style
sns.set_theme(style="whitegrid")

# Visualization 1: Chronological vs. Predicted Brain Age
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="chronological_age",
    y="predicted_brain_age",
    hue="cognitive_status",
    style="cognitive_status",
    s=100
)
# Add 1:1 line representing normal aging
min_val = min(df["chronological_age"].min(), df["predicted_brain_age"].min()) - 5
max_val = max(df["chronological_age"].max(), df["predicted_brain_age"].max()) + 5
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label="Baseline Normal Aging (1:1)")

plt.title("Chronological Age vs. Predicted Brain Age", fontsize=14, fontweight="bold")
plt.xlabel("Chronological Age at Scan (Years)", fontsize=11)
plt.ylabel("Predicted Brain Age (Years)", fontsize=11)
plt.legend(title="Cognitive Status")
plt.tight_layout()
plt.savefig("assets/brain_age_scatter.png", dpi=300)
plt.close()

# Visualization 2: BAGI Score Distribution Across Cognitive Groups
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x="cognitive_status",
    y="bagi_score",
    hue="cognitive_status",
    palette="Set2",
    legend=False
)
plt.axhline(0, color="gray", linestyle="--", linewidth=1, label="Zero Gap Baseline")
plt.title("Brain Age Gap Index (BAGI) Distribution by Cognitive Group", fontsize=14, fontweight="bold")
plt.xlabel("Cognitive Diagnostic Status", fontsize=11)
plt.ylabel("BAGI Score (Predicted - Chronological Age)", fontsize=11)
plt.tight_layout()
plt.savefig("assets/bagi_distribution_boxplot.png", dpi=300)
plt.close()

print("Visualizations successfully created and saved in the 'assets/' folder!")