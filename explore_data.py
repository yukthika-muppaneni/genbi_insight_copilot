import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Show the first few rows
print("🔍 Here’s the data:")
print(df.head())

# Plot Revenue by Date
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Revenue"], marker='o')
plt.title("📊 Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
