import sqlite3

def get_metadata():
    conn = sqlite3.connect('database/warehouse.db')
    cursor = conn.cursor()
    
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        
        # Get columns
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        for col in columns:
            print(f"Column: {col[1]} | Type: {col[2]}")
    
    conn.close()

if __name__ == "__main__":
    get_metadata()