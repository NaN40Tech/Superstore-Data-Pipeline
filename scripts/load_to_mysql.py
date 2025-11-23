import pandas as pd
import mysql.connector
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG, CLEANED_DATA_FILE

df = pd.read_csv(CLEANED_DATA_FILE)

db = mysql.connector.connect(**DB_CONFIG)

cursor = db.cursor()

insert_query = """
INSERT INTO sales (
    Row_ID, Order_ID, Order_Date, Ship_Date, Ship_Mode,
    Customer_ID, Customer_Name, Segment, Country, City,
    State, Postal_Code, Region, Product_ID, Category,
    Sub_Category, Product_Name, Sales, Quantity, Discount, Profit
)
VALUES (%s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    data = (
        row["Row ID"],
        row["Order ID"],
        row["Order Date"],
        row["Ship Date"],
        row["Ship Mode"],
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"],
        row["Country"],
        row["City"],
        row["State"],
        row["Postal Code"],
        row["Region"],
        row["Product ID"],
        row["Category"],
        row["Sub-Category"],
        row["Product Name"],
        row["Sales"],
        row["Quantity"],
        row["Discount"],
        row["Profit"]
    )
    cursor.execute(insert_query, data)

db.commit()
print(f"Success: Uploaded {len(df)} rows to MySQL database")

cursor.close()
db.close()
