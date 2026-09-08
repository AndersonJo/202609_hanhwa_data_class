import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv("titanic.csv")
df["Sex"] = (df["Sex"] == "male").astype(int)
df["Age"] = df["Age"].fillna(df["Age"].median())

features = ["Pclass", "Sex", "Age", "Fare"]
X, y = df[features], df["Survived"]

clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)
print("accuracy:", clf.score(X, y))

plt.figure(figsize=(16, 8))
plot_tree(clf, feature_names=features, class_names=["Died", "Survived"], filled=True)
plt.savefig("titanic_tree.png", dpi=150, bbox_inches="tight")
