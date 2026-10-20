import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print(df.head())
print(df.info())
print(df.describe())

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())

print("Total Sales:", df["Sales"].sum())

print("Average Sales:", df["Sales"].mean())

print("Highest Sales:", df["Sales"].max())

print("Lowest Sales:", df["Sales"].min())

print("Total Quantity Sold:", df["Quantity"].sum())

category_sales = df.groupby("Category")["Sales"].sum()

print("Category-wise Sales:")
print(category_sales)

# STEP 14 - Region-wise Sales

region_sales = df.groupby("Region")["Sales"].sum()

print("Region-wise Sales:")
print(region_sales)
df.groupby("Region")["Sales"].sum()

# STEP 15 - Category-wise Sales Bar Chart

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

# STEP 16 - Region-wise Sales Bar Chart

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.show()

# STEP 17 - Product-wise Sales

product_sales = df.groupby("Product")["Sales"].sum()

print("Product-wise Sales:")
print(product_sales)

plt.bar(product_sales.index, product_sales.values)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.show()

# STEP 18 - Quantity Sold by Product

product_quantity = df.groupby("Product")["Quantity"].sum()

print("Quantity Sold by Product:")
print(product_quantity)

plt.bar(product_quantity.index, product_quantity.values)

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")

plt.xticks(rotation=45)

plt.show()

# STEP 19 - Sales Distribution by Category

sns.boxplot(x="Category", y="Sales", data=df)

plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# STEP 20 - Correlation Heatmap

correlation = df[["Sales", "Quantity"]].corr()

print("Correlation:")
print(correlation)

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.show()

# STEP 21 - Find Important Insights

print("\n--- Important Insights ---")

# Highest selling product
highest_product = product_sales.idxmax()
highest_product_sales = product_sales.max()

print("Highest Selling Product:", highest_product)
print("Highest Product Sales:", highest_product_sales)

# Highest sales region
highest_region = region_sales.idxmax()
highest_region_sales = region_sales.max()

print("Highest Sales Region:", highest_region)
print("Highest Region Sales:", highest_region_sales)

# Highest quantity product
highest_quantity_product = product_quantity.idxmax()
highest_quantity = product_quantity.max()

print("Highest Quantity Sold Product:", highest_quantity_product)
print("Highest Quantity:", highest_quantity)

# STEP 22 - Outlier Analysis

plt.figure(figsize=(8, 5))

sns.boxplot(y=df["Sales"])

plt.title("Sales Outlier Analysis")
plt.ylabel("Sales")

plt.show()

# STEP 23 - Sales Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["Sales"], bins=5)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()