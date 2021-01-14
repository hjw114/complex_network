import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import net
import rule

np.set_printoptions(threshold=np.inf)

def point_rule(net, point, lim):
    x = net.shape[0]
    y = net.shape[1]
    for i in range(x):
        for j in range(y):
            if [i, j] in point:
                net[i, j] = rule.rule(net, i, j, 1, net[i, j], lim)
                if net[i, j] == lim:
                    if net[i, j + 1] == 0:
                        point.append([i, j + 1])
                    if net[i + 1, j] == 0:
                        point.append([i + 1, j])
                    if net[i, j - 1] == 0:
                        point.append([i, j - 1])
                    if net[i - 1, j] == 0:
                        point.append([i - 1, j])

def img_show(net, lim):
    x = net.shape[0]
    y = net.shape[1]
    img = []
    for i in range(x):
        for j in range(y):
            if net[i][j] == 0:
                img.append([255, 0, 0])
            elif net[i][j] == 100:
                img.append([0, 0, 255])
            elif net[i][j] == -1:
                img.append([255, 255, 0])
            elif net[i][j] == lim:
                img.append([0, 0, 0])
            else:
                img.append([0, 255, 0])
    img_ = np.array(img).reshape(x, y, 3)
    img_ = Image.fromarray(np.uint8(img_))
    img_.show()

def sum(net, lim):
    x = net.shape[0]
    y = net.shape[1]
    burn = 0
    forest = 0
    for i in range(x):
        for j in range(y):
            if net[i][j] == 0:
                forest += 1
            elif net[i][j] == lim:
                burn += 1
    return burn, forest

def pic(burn, forest, time):
    plt.plot(time, forest)
    plt.plot(time, burn)
    plt.show()

if __name__ == '__main__':
    path = 'D:/python/complex network/2010120120101231'
    nvdi = net.load(path)
    net, point = net.net(nvdi, 8)
    burn = []
    forest = []
    time = []
    i = 0
    while(i < 20000):
        point_rule(net, point, 10)
        burn_t, forest_t = sum(net, 10)
        burn.append(burn_t)
        forest.append(forest_t)
        time.append(i+1)
        i += 1
        print("第" + str(i) + "次")
        print("燃烧面积=" + str(burn_t))
        print("剩余森林面积=" + str(forest_t))
    img_show(net, 10)
    pic(burn, forest, time)
