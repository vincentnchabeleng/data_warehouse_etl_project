def transform_data(data):
    # Add a new column (Derived field)
    data['amount_with_tax'] = data['amount'] * 1.15
    
    # Rename columns (standardization)
    data.columns = [col.lower() for col in data.columns]
    
    print("Transformed Data:")
    print(data)
    
    return data