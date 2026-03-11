import pandas as pd

# 读取CSV文件
data = pd.read_csv("sales.csv")

# 保存为Excel文件
data.to_excel("sales.xlsx", index=False)

print("CSV successfully converted to Excel!")
