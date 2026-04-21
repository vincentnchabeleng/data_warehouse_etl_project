import sqlite3

def load_data(data):
    conn = sqlite3.connect('database/warehouse.db')
    
    data.to_sql('sales_transform', conn, if_exists='replace', index=False)
    
    print("Data Loaded into Warehouse")
    
    conn.close()