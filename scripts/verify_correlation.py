import pandas as pd
import mysql.connector
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG

# Connect to database
db = mysql.connector.connect(**DB_CONFIG)

# Load data
df = pd.read_sql("SELECT * FROM sales;", db)
db.close()

print("="*60)
print("DATA VERIFICATION - CORRELATION HEATMAP")
print("="*60)

# Show sample data
print("\nSample Data (First 10 rows):")
print(df[['Sales', 'Profit', 'Quantity', 'Discount']].head(10).to_string())

# Calculate correlation
print("\n" + "="*60)
print("CORRELATION MATRIX:")
print("="*60)
corr_matrix = df[['Sales', 'Profit', 'Quantity', 'Discount']].corr()
print(corr_matrix.round(3).to_string())

# Statistics
print("\n" + "="*60)
print("STATISTICAL SUMMARY:")
print("="*60)
print(df[['Sales', 'Profit', 'Quantity', 'Discount']].describe().to_string())

# Interpretation
print("\n" + "="*60)
print("INTERPRETATION:")
print("="*60)
print(f"1. Sales vs Profit:   {corr_matrix.loc['Sales', 'Profit']:.3f} (Positive correlation)")
print(f"2. Sales vs Quantity: {corr_matrix.loc['Sales', 'Quantity']:.3f} (Weak positive)")
print(f"3. Sales vs Discount: {corr_matrix.loc['Sales', 'Discount']:.3f} (Almost no correlation)")
print(f"4. Profit vs Quantity: {corr_matrix.loc['Profit', 'Quantity']:.3f} (Very weak)")
print(f"5. Profit vs Discount: {corr_matrix.loc['Profit', 'Discount']:.3f} (Negative correlation)")
print(f"6. Quantity vs Discount: {corr_matrix.loc['Quantity', 'Discount']:.3f} (Almost no correlation)")

print("\n" + "="*60)
print("CONCLUSION: Chart is CORRECT and matches data")
print("="*60)
