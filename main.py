"""
Superstore Data Pipeline & Analytics
Main orchestration script to run the entire data pipeline
"""

import os
import sys
import mysql.connector
from config import DB_CONFIG

def run_pipeline():
    """Run the complete data pipeline"""
    
    print("="*70)
    print("SUPERSTORE DATA PIPELINE & ANALYTICS")
    print("="*70)
    
    # Step 1: Data Cleaning & Analysis
    print("\n[STEP 1/4] Running Data Cleaning & Analysis...")
    print("-" * 70)
    try:
        from scripts import cleaning_analysis
        os.system('python scripts/cleaning_analysis.py')
        print("Success: Data cleaned and initial analysis complete")
    except Exception as e:
        print(f"Error in cleaning_analysis.py: {e}")
        return False
    
    # Step 2: Create Database Schema
    print("\n[STEP 2/4] Setting up MySQL Database Schema...")
    print("-" * 70)
    try:
        # Connect to MySQL server (without database)
        db = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = db.cursor()
        
        # Create database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cursor.close()
        db.close()
        
        # Connect to the database and create table
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        
        # Read and execute schema file
        with open('schema.sql', 'r') as f:
            schema_sql = f.read()
            # Split by semicolon and execute each statement
            for statement in schema_sql.split(';'):
                if statement.strip():
                    cursor.execute(statement)
        
        db.commit()
        cursor.close()
        db.close()
        print("Success: Database schema created")
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False
    
    # Step 3: Load Data to MySQL
    print("\n[STEP 3/4] Loading Data to MySQL...")
    print("-" * 70)
    try:
        os.system('python scripts/load_to_mysql.py')
        print("Success: Data loaded to MySQL")
    except Exception as e:
        print(f"Error in load_to_mysql.py: {e}")
        return False
    
    # Step 4: Generate Visualizations
    print("\n[STEP 4/4] Generating Analytics & Visualizations...")
    print("-" * 70)
    try:
        os.system('python scripts/query_and_visualization.py')
        print("Success: All visualizations generated")
    except Exception as e:
        print(f"Error in query_and_visualization.py: {e}")
        return False
    
    # Pipeline Complete
    print("\n" + "="*70)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("="*70)
    print("\nOutput files:")
    print(f"  - Cleaned data: output/cleaned_superstore.csv")
    print(f"  - Charts: output/charts/ (9 visualizations)")
    print(f"  - Database: MySQL '{DB_CONFIG['database']}' database")
    print("\n" + "="*70)
    
    return True

if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
