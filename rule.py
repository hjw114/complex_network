import math

def speed(x, y, x1, y1):
    x0 = x1 - x
    y0 = y1 - y
    angle = math.atan2(x0, y0)
    sp = 1 * 1 * math.pow(math.e, 0.1783 * 1 * math.cos(angle))
    return sp

def rule(net, x, y, sl, sta, lim):
    sp1 = speed(x, y, x, y + sl)
    sp2 = speed(x, y, x + sl, y)
    sp3 = speed(x, y, x, y - sl)
    sp4 = speed(x, y, x - sl, y)
    if net[x, y + sl] == lim or net[x, y + sl] == -1 or net[x, y + sl] == 100:
        sp1 = 0
    if net[x + sl, y] == lim or net[x + sl, y] == -1 or net[x, y + sl] == 100:
        sp2 = 0
    if net[x, y - sl] == lim or net[x, y - sl] == -1 or net[x, y + sl] == 100:
        sp3 = 0
    if net[x - sl, y] == lim or net[x - sl, y] == -1 or net[x, y + sl] == 100:
        sp4 = 0
    sta1 = sta + (sp1 + sp2 + sp3 + sp4)/sl + (math.pow(sp1, 2) + math.pow(sp2, 2) + math.pow(sp3, 2) + math.pow(sp4, 2))/(2 * math.pow(sl, 2))
    if sta1 > lim:
        sta1 = lim
    return sta1