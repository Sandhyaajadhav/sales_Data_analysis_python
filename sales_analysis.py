import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/sales_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Total_Sales'] = data['Quantity'] * data['Price']

print(data.info())
print("Total Revenue:", data['Total_Sales'].sum())

product_sales = data.groupby('Product')['Total_Sales'].sum()
print(product_sales)

data['Month'] = data['Date'].dt.month
monthly_sales = data.groupby('Month')['Total_Sales'].sum()

plt.figure()
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('output/monthly_sales.png')
plt.show()

plt.figure()
sns.barplot(x='Region', y='Total_Sales', data=data)
plt.title('Sales by Region')
plt.tight_layout()
plt.savefig('output/region_sales.png')
plt.show()
