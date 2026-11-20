import pandas as pd
df=pd.read_csv("Titanic-Dataset.csv")
print(df)
print(df[["Name","Sex","Age","Fare","Survived"]])

passengers=((df["Sex"]=="female") & (df["Fare"]>30))
print((df["Sex"]=="female") & (df["Fare"]>30))

# print(df.query("Sex==female  and  Fare>30"))


print(df.groupby("Pclass").agg(
  Survival_rate=("Survived","max"),
  Average_Fare=("Fare","mean"),
  Average_Age=("Age","mean")
))
