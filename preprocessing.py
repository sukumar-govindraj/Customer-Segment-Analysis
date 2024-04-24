import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sna

df= pd.read_excel("Superstore - Sales.xlsx")
label_encoder = LabelEncoder()
df['Customer ID']=label_encoder.fit_transform(df['Customer ID'])


sales_segments = df.groupby('Customer ID').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()


df['Order Date'] = pd.to_datetime(df['Order Date'])
order_frequency = df.groupby('Customer ID')['Order Date'].agg(['min', 'max', 'count']).reset_index()
order_frequency.columns = ['Customer ID', 'FirstOrderDate', 'LastOrderDate', 'OrderCount']
order_frequency['OrderRecency'] = (order_frequency['LastOrderDate'] - order_frequency['FirstOrderDate']).dt.days
pd.to_datetime(order_frequency['FirstOrderDate'])
pd.to_datetime(order_frequency['LastOrderDate'])
order_frequency.info()
