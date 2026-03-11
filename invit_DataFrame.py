import pandas as pd

data = pd.read_csv("E:/upwork_projects/players.csv")

print(data)

print(data["goals"])

for g in data["goals"]:
    print(g)

for i in range(len(data)):
    print(data["name"][i], data["goals"][i])
