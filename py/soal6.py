import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

grouped_data = data.groupby(['kecamatan','jenis_usaha']).size().unstack().fillna(0)
grouped_data.plot(kind='bar', stacked=True)
plt.xlabel('kecamatan')
plt.ylabel('jumlah usaha')
plt.title('sebaran jenis usaha di setiap kecamatan')
plt.legend(title='jenis usaha')
plt