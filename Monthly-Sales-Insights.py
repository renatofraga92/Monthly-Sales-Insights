import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew, kurtosis

# Fictitious data: monthly sales in dollars (January to December)
monthly_sales = [1200, 1500, 1300, 1800, 2000, 2200, 1900, 1700, 1600, 1400, 1300, 1250]

# 1. Visualizations

# Bar Chart - Compares monthly sales values
plt.figure(figsize=(10, 6))
plt.bar(range(1, 13), monthly_sales, color='skyblue')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.show()

# Line Graph - Shows the sales trend over time
plt.figure(figsize=(10, 6))
plt.plot(range(1, 13), monthly_sales, marker='o', linestyle='-', color='green')
plt.title("Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()

# Histogram - Analyzes the distribution of sales
plt.figure(figsize=(10, 6))
sns.histplot(monthly_sales, bins=4, kde=True, color='blue')
plt.title("Sales Distribution")
plt.xlabel("Sales ($)")
plt.ylabel("Frequency")
plt.show()

# 2. Descriptive Statistics
mean_sales = np.mean(monthly_sales)  # Mean (average) sales
median_sales = np.median(monthly_sales)  # Median sales
std_dev_sales = np.std(monthly_sales, ddof=1)  # Standard deviation (sample, ddof=1)
skewness_sales = skew(monthly_sales)  # Skewness (measure of asymmetry)
kurtosis_sales = kurtosis(monthly_sales)  # Kurtosis (measure of tail heaviness, excess kurtosis)

# Display results
print("=== Descriptive Statistics of Monthly Sales ===")
print(f"Mean: ${mean_sales:,.2f}")
print(f"Median: ${median_sales:,.2f}")
print(f"Standard Deviation: ${std_dev_sales:,.2f}")
print(f"Skewness: {skewness_sales:.2f}")
print(f"Kurtosis: {kurtosis_sales:.2f}")
