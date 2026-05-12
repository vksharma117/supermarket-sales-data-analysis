import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Supermarket Sales Project/supermarket_sales_dataset.csv")

print(df)
print(df.head())
print(df.info())
print(df.describe())

# Product line wise revenue
product_revenue = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
print(product_revenue)

# Product line wise revenue by bar chart
product_revenue.plot(kind='bar' , color='red')
plt.title("Revenue by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Revenue")
plt.show()

# Product line wise revenue by pie chart
product_revenue.plot(kind='pie' , autopct="%1.1f%%" , color='red')
plt.title("Revenue by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Revenue")
plt.show()

# City wise total sales
City_sales = df.groupby('City')['Total'].sum().sort_values(ascending=False)
print(City_sales)

# Most used payment method
Payment = df['Payment'].value_counts()
print(Payment)

# Highest average customer rating
rating = df.groupby('Product line')['Customer stratification rating'].mean().sort_values(ascending=False)
print(rating)

# Average profit per transaction
avg_profit = df['Gross income'].mean()
print(avg_profit)

# Average profit per transaction by histogram
plt.hist(df['Gross income'], bins=20)
plt.title("Profit Distribution")
plt.xlabel("Gross Income")
plt.ylabel("Frequency")
plt.show()

# Month wise sales trend
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total'].sum()
print(monthly_sales)

# Month wise sales trend by line chart
monthly_sales.plot(kind='line')
plt.title("Month Wise Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
