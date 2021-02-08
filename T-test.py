from typing import List, Any, Union
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv("D:/Documents/PythonTools/ttestdata.csv", index_col=None, header=None, names=['ctrl', 'Tricanie', 'Tricanie removed', 'alcohol', "alcohol removed"], encoding='utf-8')
print(stats.shapiro(data["ctrl"]))
print(stats.shapiro(data["Tricanie"]))
print(stats.shapiro(data['Tricanie removed']))
print(stats.shapiro(data['alcohol']))
print(stats.shapiro(data["alcohol removed"]))
print(stats.levene(data["ctrl"], data["Tricanie"]))
print(stats.ttest_ind(data["ctrl"], data["Tricanie"]))
print(stats.ks_2samp(data["Tricanie"], data['Tricanie removed']))
print(stats.ks_2samp(data["ctrl"], data['Tricanie removed']))
print(stats.ks_2samp(data['alcohol'], data["alcohol removed"]))
print((stats.ks_2samp(data["ctrl"], data['alcohol'])))
y = []
for i in ['ctrl', 'Tricanie', 'Tricanie removed', 'alcohol', "alcohol removed"]:
    x = list(data[i])
    y.append(sum(x)/len(x))
plt.bar(x = ['ctrl', 'Tricanie', 'Tricanie removed', 'alcohol', "alcohol removed"], height=y, color='#3CB371',alpha=0.6,  width=0.4)
plt.xlabel("treatment")
plt.ylabel("heart rate")
plt.show()
plt.plot(['ctrl', 'Tricanie', 'Tricanie removed', 'alcohol', "alcohol removed"], y, "#9932CC", marker=".")
plt.xlabel("treatment")
plt.ylabel("heart rate")
plt.show()
