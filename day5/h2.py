import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df=pd.read_csv('FEH_00200524_220712104724.csv',index_col='全国・都道府県',encoding='shift_jis')
print(len(df))
print(df.columns.values)

print(df['2021年'])
df['2021年'] = pd.to_numeric(df['2021年'].str.replace(",",""))
print(df['2021年'])

df['2021年'].plot.bar(figsize=(10,6))
plt.show()

