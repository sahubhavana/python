import pandas as pd

# Read dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print(df.head())

# Remove rows with missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")
