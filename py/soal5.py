import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

rekreasi = pd.read_csv('data.csv')

data3 = rekreasi['wilayah'].value_counts()

fig = plt.figure()
x = data3.index
y = data3.values
plt.bar(x,y,color = 'black', width =0.6)
plt.xticks(rotation = 90)
plt.xlabel('wilayah')
plt.ylabel('value')
plt.title('banyak jenis usaha di jakarta')
plt