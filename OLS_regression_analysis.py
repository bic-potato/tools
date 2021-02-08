import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
data = pd.read_csv("D:/Documents/PythonTools/olsdata.csv", index_col=None, header=None, names=['c', 'A'], encoding='utf-8')


x = data['c']
y = data['A']
est = smf.ols(formula='A~c', data=data).fit()
y_Predict = est.predict(x)
r = est.rsquared
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('regression equation')
plt.text(0.000001, 0.72, f'$R^{2}$={r:.4f}', )
dict1 = dict(est.params)
plt.text(0.000001, 0.8, f'$y=${dict1["c"]:.3f}$x+${dict1["Intercept"]:.3f}')
plt.xlabel('c', style='italic')
plt.ylabel('A', style='italic')
ax1.scatter(x, y, s=10, c='c')
ax1.plot(x, y_Predict, c='darkorange', linewidth=0.6)
plt.show()
