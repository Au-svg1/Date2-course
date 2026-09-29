"""Minimal starter: load and inspect the unchanged challenge data."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "data" / 'indicator_catalog.csv'

data = pd.read_csv(DATA_PATH)
print(f"Loaded {len(data):,} rows from {DATA_PATH.name}")
print("Columns:", data.columns.tolist())
print(data.head())

# Begin your team-designed analysis below. Do not overwrite files in data/.
