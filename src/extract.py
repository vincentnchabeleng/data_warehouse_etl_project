import pandas as pd

def extract_data():
    data = pd.read_csv('data/sales.csv')
    print("Data Extracted:")
    print(data)
    return data

if __name__ == "__main__":
    extract_data()