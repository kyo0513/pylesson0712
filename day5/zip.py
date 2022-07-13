import pandas as pd

df=pd.read_csv('13TOKYO.CSV',header=None,encoding="shift_jis")

print(len(df))
print(df.columns.values)

results=df[df[2] == 1600006]
print(results[[2,6,7,8]])

#results=df[df[8].str.contains('四谷')]   #含む検索
results=df[df[8]=='四谷']                 #ダイレクト検索
print(results[[2,6,7,8]])


