import pandas as pd
df=pd.read_csv("supermarket_messy_practice.csv")
#print(df.head())
#print(df.shape)
#print(df.info())
#print(df.isnull().sum())
#print(df[df.duplicated()])
#print(df[df.isnull().any(axis=1)])
#print(df["Branch"].value_counts())
#print(df["Product"].value_counts())
#print(df["Quantity"].dtype)
df["Quantity"]=df["Quantity"].replace({"two":2}).astype(int)
#print(df["Quantity"].value_counts())
#print(df["Quantity"].dtype)
#print(df[df["Quantity"] <0])
#print(df["Price"].dtype)
#print(df["Price"].value_counts())
#print(df[df["Price"]=="free"])
df["Price"]=df["Price"].replace({"free":70}).astype(int)
#print(df[df["Price"]<=0])
#print(df["Total_Sales"].value_counts())
#print(df[df["Total_Sales"]<0])
#print(df[df["Total_Sales"]==0])
#print(df[(df["Quantity"]==0) & (df["Total_Sales"]>0)])
#df["Quantity"]=df["Quantity"].replace({0:2,-2:2}).astype(int)
#print(df[(df["Quantity"]==0) & (df["Total_Sales"]>0)])
#df["Total_Sales"]=df["Total_Sales"].replace({-100:100}).astype(int)
#print(df[df["Total_Sales"]<0])
#print(df.columns)
#print(df["Sale_Date"].value_counts())
df["Sale_Date"]=pd.to_datetime(df["Sale_Date"],errors="coerce")
#print(df["Sale_Date"])
#print(df[df["Order_ID"].duplicated()])
#print(df[df["Order_ID"]=="S026"])

df["Expected_Sales"] = df["Quantity"] * df["Price"]

wrong_sales = df.loc[
    df["Expected_Sales"] != df["Total_Sales"]
]

print(wrong_sales[["Order_ID", "Quantity", "Price", "Total_Sales", "Expected_Sales"]])










