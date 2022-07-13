from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import random

df=pd.DataFrame(columns=['Aさん','Bさん'])

for i in range(1,32):
    weight_a=random.uniform(60,63)
    weight_b=random.uniform(55,58)
    df.loc[str(i)+'日']=[weight_a,weight_b]
  
df.plot()
plt.grid()
plt.show()