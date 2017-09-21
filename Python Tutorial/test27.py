import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 200)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(10,5))
plt.plot(X,C, color="green", linewidth=5.0, linestyle="--")
plt.plot(X,S, color="red",   linewidth=2.5, linestyle="-")

plt.show()

