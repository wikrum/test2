import pandas as pd
import openpyxl

ds = pd.read_csv("C:/Users/vikram.b.rao/Documents/Projects/HR analytics/test_2umaH9m.csv")
print(ds.head())
ds1 = ds[ds['department']=='HR']
ds1.to_excel("C:/Users/vikram.b.rao/Documents/Projects/HR analytics/HR.xlsx")

x= input("Enter the number:")
print("New number : ", x*2)
input("Enter to exit")