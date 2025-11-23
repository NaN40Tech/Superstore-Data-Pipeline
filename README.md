# Superstore Data Pipeline & Analytics

A complete end-to-end data pipeline project that demonstrates ETL (Extract, Transform, Load) processes, data analysis, and visualization using Python and MySQL.

## Project Overview

Developed an end-to-end data pipeline to analyze retail sales data from a fictional Superstore. This project encompasses **ETL (Extract, Transform, Load)** processes to clean 9,000+ transaction records, **relational database schema design**, and **automated visualization dashboards**. The analysis provides deep insights into sales trends, category profitability, and customer segmentation to support data-driven business decisions.

## Features

- **Data Cleaning & Transformation**: Automated ETL pipeline using Pandas
- **Database Integration**: MySQL storage with optimized schema and indexes
- **Advanced Analytics**: Statistical analysis and correlation studies
- **Professional Visualizations**: 9 publication-ready charts with soft pastel color scheme
- **Modular Architecture**: Clean, maintainable code structure

## Tech Stack

- **Python 3.13**: Core programming language
- **Pandas 2.3.3**: Data manipulation and analysis
- **MySQL**: Relational database for data storage
- **Matplotlib 3.10.7**: Static visualizations
- **Seaborn 0.13.2**: Statistical data visualization
- **NumPy 2.3.5**: Numerical computing

## Project Structure

```
project_3_superstore/
├── data/
│   └── Superstore.csv              # Raw dataset
├── scripts/
│   ├── cleaning_analysis.py        # ETL & exploratory analysis
│   ├── load_to_mysql.py           # Database loading script
│   ├── query_and_visualization.py # Analytics & charts generation
│   └── verify_correlation.py      # Data validation tool
├── output/
│   ├── cleaned_superstore.csv     # Processed dataset
│   └── charts/                    # Generated visualizations (9 charts)
├── config.py                       # Configuration management
├── schema.sql                      # MySQL table schema
├── main.py                         # Pipeline orchestration
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
└── README.md                       # Documentation
```

## Installation

### Prerequisites

- Python 3.9+
- MySQL Server 8.0+
- pip (Python package manager)

### Setup

1. Clone the repository
```bash
git clone [repository-url]
cd project_3_superstore
```

2. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database credentials
```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

5. Set up MySQL database
```bash
mysql -u root -p < schema.sql
```

## Usage

### Run Complete Pipeline

Execute the entire data pipeline with one command:

```bash
python main.py
```

This will:
1. Clean and transform the raw data
2. Create MySQL database schema
3. Load data into MySQL
4. Generate all analytics and visualizations

### Run Individual Scripts

**Data Cleaning:**
```bash
python scripts/cleaning_analysis.py
```

**Load to MySQL:**
```bash
python scripts/load_to_mysql.py
```

**Generate Visualizations:**
```bash
python scripts/query_and_visualization.py
```

## Analytics & Visualizations

The project generates 9 professional visualizations:

1. **Sales Trend Over Time** - Monthly sales progression (2014-2017)
2. **Sales per Year** - Annual revenue comparison
3. **Profit by Category** - Category-wise profitability analysis
4. **Top 10 Products** - Best-selling products by revenue
5. **Sales by Region** - Geographic sales distribution (pie chart)
6. **Sales by Segment** - Customer segment analysis (donut chart)
7. **Correlation Heatmap** - Relationship between key metrics
8. **Top 10 States** - State-level sales performance
9. **Profit Margin Analysis** - Sales vs profit margin by category

All charts are export-ready at 300 DPI with professional soft pastel color scheme.

## Key Insights

- **Sales Growth**: 47% increase from 2014 ($484K) to 2017 ($733K)
- **Profit Margin**: Technology category shows highest profit margin (10.1%)
- **Discount Impact**: Negative correlation (-0.220) between discount and profit
- **Top Performers**: California leads with highest sales volume

## Data Pipeline Flow

```
Raw CSV Data → Data Cleaning → MySQL Database → Analytics → Visualizations
     ↓              ↓                ↓              ↓            ↓
Superstore.csv  Pandas ETL    MySQL Tables   SQL Queries   PNG Charts
```

## Database Schema

The MySQL database uses an optimized schema with indexes on:
- `Order_Date` (time-based queries)
- `Category` (category analysis)
- `Region` (geographic analysis)
- `Customer_ID` (customer tracking)

## Contributing

This is a portfolio project. For suggestions or improvements, please open an issue.

## License

MIT License - feel free to use this project for learning purposes.

## Author

**Nabila Salvaningtyas**  
*Data Analyst & Administrator*

---

## Acknowledgments

- Dataset: [Superstore Dataset Final](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) on Kaggle
- Inspiration: Real-world business intelligence workflows
