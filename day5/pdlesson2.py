import pandas as pd
df=pd.read_csv('test.csv')

data_s=df[df['国語'] >= 90]
print(data_s)
#&,|
data_s=df[(df['国語'] >=90) & (df['数学'] >=80) ]
print(data_s)

#集計
print('数学の最高点',df['数学'].max())
print('数学の最低点',df['数学'].min())
print('数学の平均点',df['数学'].mean())
print('数学の中央値',df['数学'].median())
print('数学の合計  ',df['数学'].sum())

#mode？を使うと同点がいればそれを出す

math_df=df.sort_values('数学')
print(math_df)

kokugo_df=df.sort_values('国語',ascending=False)
print(kokugo_df)

df_T=df.T
print(df_T)

li=df.values
print(li)

#csv化
kokugo_df.to_csv("export1.csv")
kokugo_df.to_csv("export2.csv",index=False)
kokugo_df.to_csv("export3.csv",index=False,header=False)



