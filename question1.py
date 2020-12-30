from math import sqrt

perimeters = {}
for a in range(1, 1000):
    for b in range(1, int(a / 2) + 1):
        c = sqrt(a ** 2 + b ** 2)
        p = a + b + c
        if c == int(c) and p < 1001:
            perimeters[p] = perimeters.get(p, 0) + 1

inverse = [(value, key) for key, value in perimeters.items()]
print(max(inverse)[1])
