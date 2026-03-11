import pandas as pd

data = pd.read_csv("players1.csv")

print("Player1 Data:")
print(data)

top_scorer = data.loc[data["goals"].idxmax()]

print("\nTop Scorer:")
print(top_scorer["player"], "-", top_scorer["goals"], "goals")

data_sorted = data.sort_values(by="goals", ascending=False)

data_sorted.to_excel("football_analysis.xlsx", index=False)

print("\nAnalysis exported to football_analysis.xlsx")
