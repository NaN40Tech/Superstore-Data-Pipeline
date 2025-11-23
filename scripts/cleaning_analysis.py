import pandas as pd
import numpy as np
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import RAW_DATA_FILE, CLEANED_DATA_FILE

# =============================
# 1. LOAD DATASET
# =============================
df = pd.read_csv(RAW_DATA_FILE, encoding="latin-1")

print("=== 5 Data Teratas ===")
print(df.head(), "\n")

print("=== Info Dataset ===")
print(df.info(), "\n")

print("=== Jumlah Missing Values ===")
print(df.isnull().sum(), "\n")

print("=== Jumlah Duplikasi ===")
print(df.duplicated().sum(), "\n")


# =============================
# 2. CLEANING
# =============================

# Hapus duplikasi
df = df.drop_duplicates()

# Format tanggal
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Hapus missing values kecil (jika ada)
df = df.dropna()

# Buat kolom baru
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Profit Ratio"] = df["Profit"] / df["Sales"]


# =============================
# 3. EDA (Exploratory)
# =============================
print("=== Total Sales per Tahun ===")
print(df.groupby("Year")["Sales"].sum(), "\n")

print("=== Top 10 Produk Terlaris (Quantity) ===")
print(df.groupby("Product Name")["Quantity"].sum().nlargest(10), "\n")

print("=== Profit per Kategori ===")
print(df.groupby("Category")["Profit"].sum(), "\n")

print("=== Negara dengan Sales Tertinggi ===")
print(df.groupby("Country")["Sales"].sum().nlargest(10), "\n")


# =============================
# 4. EXPORT DATA BERSIH
# =============================
df.to_csv(CLEANED_DATA_FILE, index=False)

print("=== DONE! File cleaned_superstore.csv berhasil dibuat ===")
