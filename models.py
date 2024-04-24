import pyodbc
import pandas as pd


con = pyodbc.connect(
    r"Driver= {ODBC Driver 17 for SQL Server};"
    r"Server=SUKUMAR\SQLEXPRESS;"
    r"Database=SuperStore;"
    r"Trusted_Connection=yes;"
)

df =  pd.read_csv("C:/Users/Chugu/Downloads/category_segments.csv")
# df = df.head(5)


def getData(con):
    cursor = con.cursor()
    cursor.execute("select * from dbo.category")
    print(f"{cursor.rowcount} has been inserted")
    con.commit()

    
def insertData(con, df, table_name):
    cursor = con.cursor()

    sqlq = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['?'] * len(df.columns))})"

    for index, row in df.iterrows():
        values = tuple(row)
        cursor.execute(sqlq, values)
    con.commit()

insertData(con,df,'dbo.category');

getData(con);


