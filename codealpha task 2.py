import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sales_data_2023.csv")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set Seaborn style
sns.set(style="whitegrid")

# 1. 📈 Total Sales Over Time
df_daily = df.groupby(df['Date'].dt.to_period("M")).sum(numeric_only=True)
df_daily.index = df_daily.index.to_timestamp()

plt.figure(figsize=(10, 6))
plt.plot(df_daily.index, df_daily['Sales'], marker='o', color='blue')
plt.title("Total Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. 📊 Sales by Region
plt.figure(figsize=(8, 6))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum, ci=None)
plt.title("Total Sales by Region")
plt.ylabel("Total Sales")
plt.show()

# 3. 📊 Sales by Product Category
plt.figure(figsize=(8, 6))
sns.barplot(x='Product', y='Sales', data=df, estimator=sum, ci=None)
plt.title("Total Sales by Product")
plt.ylabel("Total Sales")
plt.show()

# 4. 🧍‍♂️ Sales by Customer Type
plt.figure(figsize=(8, 6))
sns.barplot(x='Customer_Type', y='Sales', data=df, estimator=sum, ci=None)
plt.title("Sales by Customer Type")
plt.ylabel("Total Sales")
plt.show()

# 5. 🥧 Profit Distribution per Product
plt.figure(figsize=(8, 6))
sns.boxplot(x='Product', y='Profit', data=df)
plt.title("Profit Distribution by Product")
plt.ylabel("Profit")
plt.show()

# 6. 📈 Sales vs Profit Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sales', y='Profit', hue='Product', data=df)
plt.title("Sales vs Profit by Product")
plt.show()