import pandas as pd

pd.set_option('display.max_columns', None)

df_p = pd.read_csv('../datab/Products.csv', sep = ';')
df_c = pd.read_csv('../datab/Customers.csv', sep = ';')
df_o = pd.read_csv('../datab/Orders.csv', sep = ';')
df_od = pd.read_csv('../datab/Order_details.csv', sep = ';')
df_e = pd.read_excel('../datab/Employees.xlsx')

df_od['Discount_fact'] = df_od['UnitPrice']*df_od['Quantity']*df_od['Discount']
df_od['Revenue'] = df_od['UnitPrice']*df_od['Quantity'] - df_od['Discount_fact']
df_od_2 = df_od.groupby('OrderID').agg({'Discount_fact':'sum', 'Revenue':'sum'}).reset_index()

#print(df_o.columns)
df_o = df_o.merge(df_od_2)
df_o = df_o.merge(df_c)
df_o_result = df_o.groupby('ContactName').Revenue.sum().sort_values()
print(df_o_result)