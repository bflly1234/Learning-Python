import pandas as pd

# prov ,  channel , date_of_birth , cust_ID , buy_date , buy_amount , year_old
salesDF = pd.read_excel('E:\sales.xlsx')
# 2.3.1 Common functions：data type, first or last record, initial setup to 5
print(salesDF.dtypes)
print(salesDF.head())
print(salesDF.tail())
# 2.3.2 Descriptive statistics
print('Mean: ', salesDF[['buy_amount', 'year_old']].mean())
print('Sum: ', salesDF[['buy_amount', 'year_old']].sum())
print('median: ', salesDF[['buy_amount', 'year_old']].median())
print('Var: ', salesDF[['buy_amount', 'year_old']].var())
print('Std: ', salesDF[['buy_amount', 'year_old']].std())
print('Max: ', salesDF[['buy_amount', 'year_old']].max())
print('Quantile: ', salesDF[['buy_amount', 'year_old']].quantile())
print('Count: ', salesDF[['buy_amount', 'year_old']].count())
print('Idx-max: ', salesDF[['buy_amount', 'year_old']].idxmax())
# 2.3.3 Frequency Function
print('Prov Name: ', salesDF['prov'].unique())
print('How Many prov: ', salesDF['prov'].nunique())
# Note: Queries the location of the first occurrence of each variable, ***
print('How Many prov: ', salesDF['prov'].drop_duplicates())
# 2.3.4 Substitution Function (might need to know more)
# 2.3.5 Sort Function
print(salesDF.sort_values('prov', ascending=False))
print(salesDF.sort_values(['prov', 'channel']))
# rank() might need to know more
# 2.3.6 apply() function might need to know more
# 2.4 window?
