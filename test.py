import pandas as pd
import numpy as np
import matplotlib as mpl
import sklearn as sk

print("pandas: ", pd.__version__)
print("numpy: ", np.__version__)
print("matplotlib: ", mpl.__version__)
print("sklearn: ", sk.__version__)

columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]

heart = pd.read_csv("../datasets/heart+disease/processed.cleveland.data",
                    names=columns,
                    na_values=["?", "-9", "-9.0"])

#how big is the dataset?
print(f"Shape: {heart.shape}")

#what are the columns and types?
heart.info()

#what does the data look like?
heart.head(10)
heart.sample(10, random_state=42)

#how much data  is missing?
#print(f"Missing data: {heart.isna().mean().sort_values(ascending=False)}")

#print(f"Missing values per column: {heart.isna().sum().sum()}")

for col in heart.columns:
    if heart[col].nunique() < 20:
        print(f"\n{col}:")
        print(heart[col].value_counts().head(10))


fake_news = pd.read_csv("../datasets/FakeNewsNet.csv",
                        names=columns)
#what are the columns and types?
fake_news.info()

#what does the data look like?
fake_news.head(10)
fake_news.sample(10, random_state=42)

#how much data  is missing?
print(f"Missing data: {fake_news.isna().mean().sort_values(ascending=False)}")

print(f"Missing values per column: {fake_news.isna().sum().sum()}")

for col in fake_news.columns:
    if fake_news[col].nunique() < 20:
        print(f"\n{col}:")
        print(fake_news[col].value_counts().head(10))