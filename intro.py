import pandas as pd

df=pd.DataFrame({
  "Name":["Mahesh Bhatt","Neeraj Bhatt","Rohit Singh"],
  "Age":[21,22,19],
  "Programming":["JS","Python","C++"]
})

print(df)

df2=pd.read_csv("raw_data.csv")
print(df2)