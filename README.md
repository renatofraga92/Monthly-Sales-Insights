# Monthly Sales Insights

## Overview
This project analyzes and visualizes monthly sales data for a fictitious store over a year (January to December) using Python. It creates bar charts, line graphs, histograms, and calculates descriptive statistics to explore patterns, trends, and the distribution of sales.

## Features
- Bar Chart: Compares monthly sales values.
- Line Graph: Shows the sales trend over time.
- Histogram: Analyzes the distribution of sales with a density curve.
- Descriptive Statistics: Calculates mean, median, standard deviation, skewness, and kurtosis to quantify the data's behavior.

## Data
The dataset consists of 12 monthly sales figures in dollars: [1200, 1500, 1300, 1800, 2000, 2200, 1900, 1700, 1600, 1400, 1300, 1250].

## Visualizations Explained
- **Bar Chart ("Monthly Sales")**: Displays monthly sales as vertical bars, allowing comparison across months. The skyblue color enhances readability, and labels indicate months (1-12) and sales in dollars.
- **Line Graph ("Sales Trend Over Time")**: Illustrates the sales trend with a green line and circular markers, showing how sales evolve from January to December. A grid is added for better readability.
- **Histogram ("Sales Distribution")**: Uses Seaborn to create a histogram with 4 bins and a density curve (kde), visualizing the distribution of sales. The blue color and frequency labels highlight the data's shape.

## Descriptive Statistics Explained
Descriptive statistics summarize the main characteristics of the sales data:
- **Mean**: The average sales value, calculated as $1,616.67, representing the central tendency.
- **Median**: The middle value, $1,600.00, less affected by outliers, indicating the typical sales amount.
- **Standard Deviation**: Measures variability, calculated as $356.60 (approximately 22% of the mean), indicating moderate variability in sales.
- **Skewness**: Measures asymmetry, with a value of 0.36, indicating positive skewness (a long tail to the right), driven by the June peak of 2200.
- **Kurtosis**: Measures the "tailedness" of the distribution, with a value of -0.98 (excess kurtosis), indicating thinner tails than a normal distribution, suggesting fewer extreme outliers.

## Observations and Analyses
- The general sales trend over the year shows a gradual increase from January (1200) to a peak in June (2200), followed by a gradual decline to December (1250). There are no clear outliers, but June represents the month with significantly higher sales (above the mean of 1616.67), while January and December are below the mean, indicating months with lower sales.
- The sales distribution is positively skewed, with a long tail to the right due to the peak in June, as indicated by a skewness of approximately 0.36.
- The standard deviation (22% of the mean) suggests moderate variability, consistent with seasonal fluctuations but not extreme dispersion.

## Requirements
- Python 3.x
- Libraries: pandas, seaborn, matplotlib, numpy, scipy

## How to Run
1. Clone this repository.
2. Install the required libraries using `pip install pandas seaborn matplotlib numpy scipy`.
3. Run the script (`python monthly_sales_analysis.py`) to generate and display the visualizations and statistics.

## License
This code is protected by copyright and is not licensed for use, modification, or distribution without explicit permission from the author. All rights reserved. Please contact renatofraga.rr@gmail.com for inquiries.
