import pandas as pd

# List your files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)
    
    # Filter for pink morsels
    df = df[df["product"] == "pink morsel"]
    
    # Clean price (remove $ and convert to float)
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
    
    # Create sales column
    df["sales"] = df["price"] * df["quantity"]
    
    # Select required columns
    df = df[["sales", "date", "region"]]
    
    dfs.append(df)

# Combine all dataframes
final_df = pd.concat(dfs)

# Save to CSV
final_df.to_csv("data/processed_sales.csv", index=False)