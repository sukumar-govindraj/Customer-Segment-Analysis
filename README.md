
# Customer Segmentation Analysis using sales data 

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

## EDA, Visualizations and Power BI Dashboard

1. **Sales vs. Profit by Category**: A scatter plot depicting the relationship between Sales and Profit, colored by product category.
![image](https://github.com/user-attachments/assets/4b0c0cb7-34ef-483b-9100-7587c303e6a4)

3. **Sales Distribution by Category**: A boxplot showing the distribution of sales across different product categories.
  ![image](https://github.com/user-attachments/assets/eb932e2b-9b56-4b89-a05b-7e7b035a466e)

4. **Top 10 Products by Sales**: A bar chart highlighting the top 10 products based on total sales.
 ![image](https://github.com/user-attachments/assets/02e88778-13d4-420c-86e1-e9e00bb6658e)

**Power BI Dashboard**
![image](https://github.com/user-attachments/assets/37f9635e-a7a9-4bb6-9c02-d1bca8eaaea6)
![image](https://github.com/user-attachments/assets/ca112056-027f-447e-b19c-61412857bb9b)
![image](https://github.com/user-attachments/assets/c036e8ee-f60d-498d-a52f-13e52e9ebe3e)

## Model Performance 

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
