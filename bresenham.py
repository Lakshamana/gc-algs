# coding: utf-8
# Algoritmo de Bresenham

"""
ponto = {'x': xvalue, 'y': yvalue}
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def prtab(tab):
    for line in tab: 
        print(line)


def calcAngular(p1: Point, p2: Point):
    return (p2.x - p1.x) / (p2.y - p1.y)


def reflexao(p1: Point, p2: Point):
    m = calcAngular(p1, p2)
    trocaxy = trocax = trocay = False
    if m > 1 or m < -1:
        p1.x, p1.y = p1.y, p1.x
        p2.x, p2.y = p2.y, p2.x
        trocaxy = True
    if p1.x > p2.x:
        p1.x = -p1.x
        p2.x = -p2.x
        trocax = True
    if p1.y > p2.y:
        p1.y = -p1.y
        p2.y = -p2.y
        trocay = True
    return (p1, p2, trocaxy, trocax, trocay)

#points: list of point dicts
def reflexaoInv(points: list, trocaxy, trocax, trocay):
    new_points = []
    for p in points:
        if trocaxy:
            p.x, p.y = p.y, p.x
        if trocax:
            p.x = -p.x
        if trocay:
            p.y = -p.y
        new_points.append(p)
    return new_points


def plot(tab, p: Point):
    tab[p.x][p.y] = 1

def bresenham(malha, p1: Point, p2: Point):
    (p1, p2, trocaxy, trocax, trocay) = reflexao(p1, p2)
    x = p1.x
    y = p1.y
    init_point = Point(x, y)
    m = calcAngular(p1, p2)
    e = m - 0.5
    plot(malha, init_point)
    p = []
    while x < p2.x:
        if e >= 0:
            y += 1
            e -= 1
        x += 1
        e += m
        new_point = Point(x, y)
        p.append(new_point)
    p = reflexaoInv(p, trocaxy, trocax, trocay)
    for point in p: 
        plot(malha, point)
    return p

order = int(input('Digite a ordem da malha de desenho: '))
malha = [[0 for i in range(order)] for i in range(order)]
prtab(malha)
p1 = Point(0, 0)
p2 = Point(2, 3)
bresenham(malha, p1, p2)
print()
prtab(malha)