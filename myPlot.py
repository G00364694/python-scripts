
"""
============
Scatter plot
============
"""
import matplotlib.pyplot as plt

a = [590,540,740,130,810,300,320,230,470,620,770,250]
b = [32,36,39,52,61,72,77,75,68,57,48,48]
c = [35,64,49,58,66,70,77,78,58,57,38,28]
d = [3,6,9,5,11,7,9,15,8,17,18,28]

data = (a, b, c)
#colors = ("red", "blue", "yellow", "green")
#groups = ("setosa", "verticosa", "hibiscosa", "flower")

colors = ("red", "blue", "yellow")
groups = ("setosa", "verticosa", "hibiscosa")
# 1, 1, 1, 1, axisbg="1.0"
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    #ax.scatter(X, Y, Z, K, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    ax.scatter(x, y, alpha=0.8, edgecolors='none', c=colors, s=30, label=group)

plt.title('Relationship Between X, Y, Z, K')
plt.legend(loc=2)
plt.show()