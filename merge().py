import pandas as pd
sales=pd.DataFrame({"order":["001","002","003"],"Branch":["Nairobi","Kisumu","Machakos"],
                    "Sales":[1000,3400,3200]})
#print(sales)
branches=pd.DataFrame({"Branch":["Nairobi","Machakos","Mombasa"],"Manager":["Mary","Mueni","Mulu"]})
#print(branches)
result=pd.merge(sales,branches,on="Branch",how="outer")
print(result)