import pandas as pd
import sqlite3

print("🚀 Starting ETL process...")

# Extract
data = pd.read_csv(r'C:\Users\HP\Documents\data_project\data\sales.csv')
print("\n✅ Extracted Data:")
print(data)

# Transform
data['total'] = data['amount'] * 1.15
print("\n✅ Transformed Data:")
print(data)

# Load
conn = sqlite3.connect(r'C:\Users\HP\Documents\warehouse.db')
data.to_sql('sales_table', conn, if_exists='replace', index=False)

# Create index
cursor = conn.cursor()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON sales_table(id);")

# Metadata
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("\n📊 Tables:")
for table in tables:
    print(table)

cursor.execute("PRAGMA table_info(sales_table);")
columns = cursor.fetchall()

print("\n📋 Columns:")
for col in columns:
    print(col)

conn.close()

print("\n🎉 ETL Process Completed Successfully!")