import numpy as np
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from scipy.stats import norm
from math import exp, sqrt, pi

a = np.loadtxt('1-1.txt')

# ecdf = ECDF(a)
# plt.step(ecdf.x, ecdf.y)
# plt.ylabel('$F(x)$', fontsize=20)
# plt.xlabel('$x$', fontsize=20);

# plt.savefig('ecdf.png')

# # эмпирическая оценка для плотности
# plt.hist(a, bins=100)
# plt.savefig('density_hist.png')



# проверка на нормальное распределение
x = np.linspace(-10, 10, 1000)
# pdf ==  Probability Density Function
pdf = norm.pdf(x, scale=2.85, loc=0.6)
# получилось нормальное распределение со сдвигом
# примерно (х - 0.6) и масштабированием 2.85 примерно
plt.plot(x, pdf, lw=3)

plt.hist(a, bins=100, density=True)

plt.ylabel('$f(x)$')
plt.xlabel('$x$')

plt.savefig('check_norm.png')