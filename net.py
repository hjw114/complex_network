import numpy as np
import random
import cmath

np.set_printoptions(threshold=np.inf)

def net(net, d):
    x = net.shape[0]
    y = net.shape[1]

    number = []
    test = []

    for i in range(d):
        cf = 0
        number.append([])
        for j in range(2):
            if j == 0:
                num = random.randint(0, x - 1)
            else:
                num = random.randint(0, y - 1)
            number[i].append(num)
            if j == 1:
                test.append(number[i][0])
                test.append(number[i][1])
                for k in number:
                    if test == k:
                        cf = 1
                while net[number[i][0], number[i][1]] == 100 or net[number[i][0], number[i][1]] == -1 or cf == 1:
                    del number[i]
                    number.append([])
                    for j in range(2):
                        if j == 0:
                            num = random.randint(0, x - 1)
                        else:
                            num = random.randint(0, y - 1)
                        number[i].append(num)
                    for k in number:
                        if test == k:
                            cf = 1
                        else:
                            cf = 0
    return net, number

def load(path):
    nvdi = np.loadtxt(path)
    jud = np.array(np.random.rand(681, 841))
    net = np.zeros(shape=(681, 841))
    for i in range(681):
        for j in range(841):
            net[i][j] = 100 * (~((jud[i][j] < cmath.sqrt(nvdi[i][j])) and (nvdi[i][j] < 1)))
            if nvdi[i][j] > 1:
                net[i][j] = -1
    return net

if __name__ == '__main__':
    path = 'D:/python/complex network/2010120120101231'
    nvdi = load(path)
    net, point = net(nvdi, 8)
    print(net)
    print(point)