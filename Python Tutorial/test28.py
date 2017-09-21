import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 200)
C, S = np.cos(X), np.sin(X)

plt.plot(X,C, label='sin')
plt.plot(X,S, label='cos')

plt.xlim(X.min(), X.max())
plt.yticks([-1, 0, +1])
plt.legend(loc='upper left')

plt.show()

