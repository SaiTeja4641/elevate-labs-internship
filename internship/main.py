import pandas as pd

df = pd.read_excel(r'C:\internship\marketing_campaign.xlsx')
df = df.drop_duplicates()

# 2. Handle missing values (drop rows with missing income)
df = df.dropna(subset=['Income'])

# 3. Standardize text columns
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

# 4. Convert date to uniform format (dd-mm-yyyy)
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')  # ensure it's datetime

# 5. Rename columns for consistency
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Fix data types
df['income'] = df['income'].astype(int)  # Convert to integer
# (other types like int64 are already correct, date is now datetime)

# 7. Export cleaned dataset
df.to_excel('cleaned_marketing_campaign.xlsx', index=False)
print("✅ Cleaned dataset saved as 'cleaned_marketing_campaign.xlsx'")
