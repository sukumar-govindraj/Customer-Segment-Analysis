
# Sales Data Analysis Project

## Project Overview

This project aims to analyze a sales dataset, performing exploratory data analysis (EDA) to uncover insights, relationships, and trends within the data. The dataset includes information on orders, customers, products, and financial metrics like sales and profit.

## Dataset

The dataset includes the following features:
- `Row_ID`: Unique identifier for each row
- `Order_ID`: Unique identifier for each order
- `Order_Date`: The date when the order was placed
- `Ship_Date`: The date when the order was shipped
- `Ship_Mode`: The mode of shipment (e.g., Second Class, Standard Class)
- `Customer_ID`: Unique identifier for each customer
- `Country`, `City`, `State`, `Postal_Code`: Geographic information related to the order
- `Region`: The region where the order was placed
- `Product_ID`: Unique identifier for each product
- `Category`: Category of the product (e.g., Furniture, Office Supplies)
- `Sub-Category`: Sub-category of the product
- `Product_Name`: Name of the product
- `Sales`: The sales amount for the order
- `Quantity`: The quantity of the product ordered
- `Discount`: The discount applied to the order
- `Profit`: The profit earned from the order
- `CoGS`: Cost of Goods Sold

## EDA and Visualizations

1. **Correlation Matrix**: A heatmap showing the correlation between different numeric features in the dataset.
   ![Correlation Matrix](correlation_matrix.png)

2. **Sales vs. Profit by Category**: A scatter plot depicting the relationship between Sales and Profit, colored by product category.
   ![Sales vs. Profit by Category](sales_vs_profit.png)

3. **Sales Distribution by Category**: A boxplot showing the distribution of sales across different product categories.
   ![Sales Distribution by Category](sales_distribution_by_category.png)

4. **Top 10 Products by Sales**: A bar chart highlighting the top 10 products based on total sales.
   ![Top 10 Products by Sales](top_10_products_by_sales.png)

## Tools and Libraries Used

- **Python**: The primary language used for analysis.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations in Python.
- **Seaborn**: A Python visualization library based on matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.
- **Yellowbrick**: A suite of visual diagnostic tools for machine learning.
- **SQL**: Utilized to store the clustered data for further analysis.
- **Power BI**: Used to showcase the analysis and insights derived from the data.

## How to Run the Project

1. Clone the repository to your local machine.
2. Ensure you have Python installed along with the required libraries (`pandas`, `matplotlib`, `seaborn`, `yellowbrick`).
3. Run the Jupyter notebook or the Python script provided to generate the visualizations and insights.
4. Use the SQL scripts provided to create and store the clustered data.
5. Open the Power BI file to view and interact with the analysis.

## Conclusion

This project provides a comprehensive analysis of sales data, helping to uncover patterns and trends that can inform business decisions. The visualizations generated offer clear insights into the relationships between different factors such as sales, profit, and product categories. Additionally, the use of SQL and Power BI enhances the ability to manage and visualize the data effectively.
