import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Quantity": [5, 10, 8, 3, 7, 6],
    "Price": [50000, 20000, 15000, 50000, 20000, 15000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display the dataset
print("SALES DATA")
print(df)

# Calculate total revenue using NumPy
total_revenue = np.sum(df["Total_Sales"])
print("\nTotal Revenue:", total_revenue)

# Calculate average sales using NumPy
average_sales = np.mean(df["Total_Sales"])
print("Average Sales:", average_sales)

# Calculate total quantity sold for each product
product_quantity = df.groupby("Product")["Quantity"].sum()

# Find the best-selling product
best_product = product_quantity.idxmax()
print("Best-Selling Product:", best_product)

# Calculate revenue for each product
product_revenue = df.groupby("Product")["Total_Sales"].sum()

print("\nRevenue by Product:")
print(product_revenue)

# Create a bar chart
product_revenue.plot(kind="bar")

plt.title("Sales Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()