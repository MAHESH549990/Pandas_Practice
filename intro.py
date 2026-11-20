import pandas as pd

df=pd.read_csv("iris.csv")

# print(df.head(10))
# print(df.shape)
# print(df.dtypes)


patel_length=df[(df["PetalLengthCm"]>4.7) & (df["Species"]=="Iris-virginica")]

species=df[df["Species"]=="Iris-virginica"]
# print(patel_length)
# print(species)


df=df.assign(petal_ratio=df["PetalLengthCm"]/df["PetalWidthCm"])

print(
  df.groupby("Species")["petal_ratio"].mean()
)
print(df)