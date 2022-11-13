# If always getting error messages such like *****pageckage missing, go to "file=>Settings=>Python Interpreter   Click + to install the missing lib"
import pymysql
import pandas as pd
import numpy as np

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='abc123456',
    db='test'
)
cursor = db.cursor()
cursor.execute("select prov, channel, buy_date, buy_amount from sales")
salesData = cursor.fetchall()
db.close()

# Right click > Go to > Implementation of a method to know more options
df = pd.DataFrame(salesData)
# Transfer dataset character from object to float or errors
df[3] = df[3].astype('float')
df['Year'] = pd.DatetimeIndex(df[2]).year
print(df)

# generate a pivot table of sales data row = prov and channel, columns = year ,  values = buy_amount, margin shows the subtotal of both col and row
pt = df.pivot_table(index=[0, 1], columns='Year', values=3, aggfunc=np.sum, margins=True, margins_name='SubTotal')
pt.to_excel('E:\sales.xlsx',index=[0, 1], index_label=["Prov", "Channel"])
print(pt)
print('Done!')#read excel files
df2 = pd.read_excel('E:\sales.xlsx')
print(df2)
