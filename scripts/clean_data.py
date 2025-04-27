import pandas as pd # type: ignore

# Step 1: Load your uploaded original file
df = pd.read_csv('../data/real_estate_utah.csv')

# Step 2: Basic Cleaning
df = df.drop_duplicates()  # remove duplicate rows
df = df.dropna(subset=['text'])  # drop rows where description ('text') is missing
df['beds'] = df['beds'].fillna(0)  # fill missing beds with 0
df['baths'] = df['baths'].fillna(0)  # fill missing baths with 0
df['garage'] = df['garage'].fillna(0)  # fill missing garage with 0

# Step 3: Save it with the correct name
df.to_csv('../data/real_estate_cleaned.csv', index=False)

print("✅ File 'real_estate_cleaned.csv' generated successfully!")
