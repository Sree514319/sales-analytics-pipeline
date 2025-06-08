import pandas as pd
import os

# File paths
raw_path = "data/raw/SampleSuperstore.csv"
processed_path = "data/processed/cleaned_superstore.csv"

# Load and clean data
df = pd.read_csv(raw_path, encoding='latin1')  # FIXED: added encoding
df.dropna(inplace=True)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Save processed data
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print("✅ Data cleaned and saved to:", processed_path)
