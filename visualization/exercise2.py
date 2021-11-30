import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

np.random.seed(1000)
y = np.random.standard_normal(20) # 生成正态分布的随机数
x = range(len(y))
plt.plot(x,y)
plt.show()