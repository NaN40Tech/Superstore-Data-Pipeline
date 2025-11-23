import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG, CHARTS_DIR

warnings.filterwarnings('ignore')

# Set professional color scheme
plt.style.use('seaborn-v0_8-whitegrid')

# Soft pastel color palette
SOFT_BLUE = '#6B9BD1'        # Soft blue
SOFT_TEAL = '#7AB8B8'        # Soft teal
SOFT_LAVENDER = '#9B89B3'    # Soft lavender
SOFT_CORAL = '#D4928C'       # Soft coral

# Soft palette for multiple items
SOFT_PALETTE = ['#6B9BD1', '#7AB8B8', '#9B89B3', '#D4928C', '#87BBA2', 
                '#B4A5A5', '#90A9B7', '#A8BABD', '#C9B6B6', '#8FA8A4']

# -----------------------------
# 1. Koneksi ke MySQL
# -----------------------------
db = mysql.connector.connect(**DB_CONFIG)

# -----------------------------
# 2. Ambil data dari MySQL
# -----------------------------
query = "SELECT * FROM sales;"
df = pd.read_sql(query, db)
db.close()

print(f"Total data loaded: {len(df):,} rows\n")

# -----------------------------
# 2.1 Transform Data
# -----------------------------
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Year_Month'] = df['Order_Date'].dt.to_period('M')

# -----------------------------
# 3. Professional Visualizations
# -----------------------------

# 3.1 Sales Trend Over Time (Line Chart)
print("Creating: Sales Trend Over Time...")
monthly_sales = df.groupby('Year_Month')['Sales'].sum().reset_index()
# Convert to datetime and format as "Jan 2014", "Feb 2014", etc.
monthly_sales['Year_Month_Str'] = pd.to_datetime(monthly_sales['Year_Month'].astype(str)).dt.strftime('%b %Y')

fig, ax = plt.subplots(figsize=(14, 6), facecolor='white')
ax.plot(range(len(monthly_sales)), monthly_sales['Sales'], marker='o', linewidth=2.5, 
        markersize=5, color=SOFT_BLUE, markerfacecolor='white', 
        markeredgewidth=2, markeredgecolor=SOFT_BLUE)
ax.fill_between(range(len(monthly_sales)), monthly_sales['Sales'], alpha=0.15, color=SOFT_BLUE)
ax.set_title('Sales Trend Over Time (Monthly)', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xlabel('Time Period', fontsize=12, fontweight='500', color='#34495E')
ax.set_ylabel('Total Sales ($)', fontsize=12, fontweight='500', color='#34495E')
ax.set_xticks(range(0, len(monthly_sales), 3))
ax.set_xticklabels(monthly_sales['Year_Month_Str'][::3], rotation=45, ha='right')
ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "sales_trend_monthly.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.2 Sales per Year (Bar Chart with Values)
print("Creating: Sales per Year...")
sales_per_year = df.groupby('Year')['Sales'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
bars = ax.bar(sales_per_year['Year'], sales_per_year['Sales'], 
              color=SOFT_BLUE, edgecolor='white', linewidth=2, alpha=0.85)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${height/1000:.0f}K',
            ha='center', va='bottom', fontsize=10, fontweight='500', color='#34495E')

ax.set_title('Total Sales per Year', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xlabel('Year', fontsize=12, fontweight='500', color='#34495E')
ax.set_ylabel('Total Sales ($)', fontsize=12, fontweight='500', color='#34495E')
ax.set_xticks(sales_per_year['Year'])
ax.grid(axis='y', alpha=0.2, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "sales_per_year.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.3 Profit per Category (Horizontal Bar)
print("Creating: Profit per Category...")
profit_per_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=True).reset_index()

fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
bars = ax.barh(profit_per_category['Category'], profit_per_category['Profit'], 
               color=[SOFT_TEAL, SOFT_BLUE, SOFT_LAVENDER], 
               edgecolor='white', linewidth=2, alpha=0.85)

# Add value labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f' ${width/1000:.1f}K',
            ha='left', va='center', fontsize=10, fontweight='500', color='#34495E')

ax.set_title('Profit by Category', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xlabel('Total Profit ($)', fontsize=12, fontweight='500', color='#34495E')
ax.set_ylabel('Category', fontsize=12, fontweight='500', color='#34495E')
ax.grid(axis='x', alpha=0.2, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "profit_per_category.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.4 Top 10 Products by Sales (Horizontal Bar)
print("Creating: Top 10 Products...")
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
# Create gradient from dark to light corporate blue
colors_gradient = [plt.cm.Blues(0.5 + i*0.05) for i in range(10)]
bars = ax.barh(range(10), top_products.values, color=colors_gradient, 
               edgecolor='white', linewidth=1.5, alpha=0.9)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, top_products.values)):
    ax.text(val, bar.get_y() + bar.get_height()/2.,
            f' ${val:,.0f}',
            ha='left', va='center', fontsize=9, fontweight='500', color='#34495E')

ax.set_yticks(range(10))
ax.set_yticklabels([name[:40] + '...' if len(name) > 40 else name for name in top_products.index], fontsize=9.5)
ax.set_title('Top 10 Products by Sales', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xlabel('Total Sales ($)', fontsize=12, fontweight='500', color='#34495E')
ax.set_ylabel('Product Name', fontsize=12, fontweight='500', color='#34495E')
ax.grid(axis='x', alpha=0.2, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "top_products.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.5 Sales by Region (Pie Chart)
print("Creating: Sales by Region...")
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
colors_prof = [SOFT_BLUE, SOFT_TEAL, SOFT_LAVENDER, SOFT_CORAL]
wedges, texts, autotexts = ax.pie(sales_by_region.values, labels=sales_by_region.index, 
                                    autopct='%1.1f%%', startangle=90, colors=colors_prof,
                                    explode=[0.02, 0, 0, 0],
                                    textprops={'fontsize': 11, 'fontweight': '500', 'color': '#2C3E50'})

# Style percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('600')

ax.set_title('Sales Distribution by Region', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "sales_by_region.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.6 Sales by Segment (Donut Chart)
print("Creating: Sales by Segment...")
sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
colors_seg = [SOFT_BLUE, SOFT_TEAL, SOFT_LAVENDER]
wedges, texts, autotexts = ax.pie(sales_by_segment.values, labels=sales_by_segment.index,
                                    autopct='%1.1f%%', startangle=90, colors=colors_seg,
                                    pctdistance=0.85, 
                                    textprops={'fontsize': 11, 'fontweight': '500', 'color': '#2C3E50'})

# Create donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('600')

ax.set_title('Sales Distribution by Customer Segment', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "sales_by_segment.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.7 Correlation Heatmap (Enhanced)
print("Creating: Correlation Heatmap...")
fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
correlation_matrix = df[['Sales', 'Profit', 'Quantity', 'Discount']].corr()

sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='Blues', 
            center=0, square=True, linewidths=2, linecolor='white',
            cbar_kws={"shrink": 0.8}, vmin=-1, vmax=1,
            annot_kws={'fontsize': 11, 'fontweight': '500'}, ax=ax)

ax.set_title('Correlation Heatmap - Key Metrics', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xticklabels(ax.get_xticklabels(), fontsize=10, fontweight='500')
ax.set_yticklabels(ax.get_yticklabels(), fontsize=10, fontweight='500', rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "correlation_heatmap.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.8 Top 10 States by Sales (Bar Chart)
print("Creating: Top 10 States by Sales...")
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(12, 8), facecolor='white')
colors_states = [plt.cm.Blues(0.4 + i*0.05) for i in range(10)]
bars = ax.barh(range(10), top_states.values, color=colors_states, 
               edgecolor='white', linewidth=1.5, alpha=0.9)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, top_states.values)):
    ax.text(val, bar.get_y() + bar.get_height()/2.,
            f' ${val/1000:.1f}K',
            ha='left', va='center', fontsize=9, fontweight='500', color='#34495E')

ax.set_yticks(range(10))
ax.set_yticklabels(top_states.index, fontsize=10)
ax.set_title('Top 10 States by Sales', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax.set_xlabel('Total Sales ($)', fontsize=12, fontweight='500', color='#34495E')
ax.set_ylabel('State', fontsize=12, fontweight='500', color='#34495E')
ax.grid(axis='x', alpha=0.2, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "top_states_sales.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# 3.9 Profit Margin by Category (Advanced)
print("Creating: Profit Margin Analysis...")
category_metrics = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum'
}).reset_index()
category_metrics['Profit_Margin'] = (category_metrics['Profit'] / category_metrics['Sales']) * 100

fig, ax1 = plt.subplots(figsize=(12, 6), facecolor='white')

x = np.arange(len(category_metrics))
width = 0.4

# Bar chart for Sales
bars1 = ax1.bar(x, category_metrics['Sales'], width, label='Sales', 
                color=SOFT_BLUE, edgecolor='white', linewidth=2, alpha=0.85)
ax1.set_xlabel('Category', fontsize=12, fontweight='500', color='#34495E')
ax1.set_ylabel('Sales ($)', fontsize=12, fontweight='500', color=SOFT_BLUE)
ax1.tick_params(axis='y', labelcolor=SOFT_BLUE)
ax1.set_xticks(x)
ax1.set_xticklabels(category_metrics['Category'], fontsize=10, fontweight='500')
ax1.spines['top'].set_visible(False)

# Line chart for Profit Margin
ax2 = ax1.twinx()
line = ax2.plot(x, category_metrics['Profit_Margin'], color=SOFT_CORAL, marker='o', 
                linewidth=2.5, markersize=8, label='Profit Margin %', 
                markerfacecolor='white', markeredgecolor=SOFT_CORAL, markeredgewidth=2)
ax2.set_ylabel('Profit Margin (%)', fontsize=12, fontweight='500', color=SOFT_CORAL)
ax2.tick_params(axis='y', labelcolor=SOFT_CORAL)
ax2.spines['top'].set_visible(False)

# Add value labels
for i, (bar, margin) in enumerate(zip(bars1, category_metrics['Profit_Margin'])):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'${height/1000:.0f}K', ha='center', va='bottom', 
            fontsize=9, fontweight='500', color='#34495E')
    ax2.text(i, margin + 0.3, f'{margin:.1f}%', ha='center', va='bottom', 
            fontsize=9, fontweight='500', color=SOFT_CORAL)

ax1.set_title('Sales vs Profit Margin by Category', fontsize=16, fontweight='600', pad=20, color='#2C3E50')
ax1.grid(axis='y', alpha=0.2, linestyle='-', linewidth=0.5)
fig.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "profit_margin_analysis.png"), dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

# Print summary statistics
print("\n" + "="*60)
print("ALL CHARTS CREATED SUCCESSFULLY")
print("="*60)
print(f"\nTotal Charts Created: 9")
print(f"Location: {CHARTS_DIR}")
print(f"\nCharts List:")
print("   1. Sales Trend Over Time (Monthly)")
print("   2. Sales per Year")
print("   3. Profit per Category")
print("   4. Top 10 Products by Sales")
print("   5. Sales by Region (Pie Chart)")
print("   6. Sales by Segment (Donut Chart)")
print("   7. Correlation Heatmap")
print("   8. Top 10 States by Sales")
print("   9. Profit Margin Analysis")
print("\n" + "="*60)
print("Professional visualizations ready for analysis")
print("="*60 + "\n")
