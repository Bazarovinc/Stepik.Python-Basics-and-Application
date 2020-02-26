# 3D Plot of graphene dispersion

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def sqrt(x):
    return np.sqrt(x)

def cos(x):
    return np.cos(x)

# Constants
a = 1.0
d = a*np.sqrt(3)
t = 2.7
t2 = 0.5

print ("The display is not up to the mark! Modification needed.\n" )


fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-2.0*np.pi, 2.0*np.pi, 0.1)
y = np.arange(-2.0*np.pi, 2.0*np.pi, 0.1)
x, y = np.meshgrid(x, y)

f=t*sqrt(3.0+2.0*cos(a*x)+4.0*cos(a/2.0*x)*cos(d/2.0*y))

surf = ax.plot_surface(x, y, f, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=False)


f=-f
surf = ax.plot_surface(x, y, f, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=False)
ax.set_zlim3d(-3.0, 3.0)
fig.colorbar(surf, shrink=1.0, aspect=5)

plt.show()