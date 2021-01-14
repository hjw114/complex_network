from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import net

def pro():
    number = np.random.uniform(0, 3)
    if number <= 1:
        number = 1
    elif number <= 2:
        number = 2
    elif number <= 3:
        number = 3
    return number

def x_y(net):
    x = []
    y = []
    for i in range(net.shape[0]):
        x.append(i)
    for i in range(net.shape[1]):
        y.append(i)
    X, Y = np.meshgrid(np.array(x), np.array(y))
    return X, Y

def th_D(net, x, y):
    z = []
    ax = plt.axes(projection='3d')
    for i in range(net.shape[1]):
        z_ = []
        for j in range(net.shape[0]):
            if net[j][i] == -1:
                z_.append(0)
            else:
                z_.append(pro())
        z.append(z_)
    z = np.array(z)
    ax.plot_surface(x, y, z, cmap='rainbow')
    plt.show()


if __name__ == '__main__':
    path = 'D:/python/complex network/2010120120101231'
    nvdi = net.load(path)
    x, y = x_y(nvdi)
    th_D(nvdi, x, y)
