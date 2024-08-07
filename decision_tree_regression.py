# -*- coding: utf-8 -*-
"""decision_tree_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ud6bc35JueEeJ3UqCSZM_y5sueKL5Nts
"""

from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi, 0.1).reshape(-1, 1)
y = np.cos(x)
N = 4   # глубина дерева

clf = tree.DecisionTreeRegressor(max_depth=N)  # модель дерева
clf = clf.fit(x, y)                             # подача данных для обучения
yy = clf.predict(x)                             # предсказывание по выборке

# график
plt.plot(x, y, label="cos(x)")
plt.plot(x, yy, label="Desicion Tree Regression")
plt.title(f"max_depth = {N}")
plt.legend()
plt.grid()
plt.show()