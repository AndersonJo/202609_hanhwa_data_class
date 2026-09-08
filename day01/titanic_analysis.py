import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

df = pd.read_csv("titanic.csv")

print("=== 기본 정보 ===")
print(df.shape)
print(df.isnull().sum())

print("\n=== 전체 생존율 ===")
print(df["Survived"].mean())

print("\n=== 성별 생존율 ===")
print(df.groupby("Sex")["Survived"].agg(["count", "sum", "mean"]))

print("\n=== 객실 등급별 생존율 ===")
print(df.groupby("Pclass")["Survived"].agg(["count", "sum", "mean"]))

print("\n=== 성별 x 객실 등급 생존율 ===")
print(pd.crosstab(df["Sex"], df["Pclass"], values=df["Survived"], aggfunc="mean"))

print("\n=== 연령대별 생존율 ===")
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 40, 60, 100], labels=["아동", "청소년", "청년", "중년", "노년"])
print(df.groupby("AgeGroup", observed=True)["Survived"].agg(["count", "mean"]))

print("\n=== 가장 많이 죽은 그룹 (성별 x 등급, 사망자 수) ===")
dead = df[df["Survived"] == 0].groupby(["Sex", "Pclass"]).size().sort_values(ascending=False)
print(dead)
