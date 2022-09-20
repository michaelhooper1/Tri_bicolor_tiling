import numpy as np
from itertools import combinations

modulus = 12345787

def f(n, colors):
    a = np.matrix([
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0]
    ])
    for color in colors:
        a[0, color-1] += 1
    
    b = np.zeros((5, 1))
    b[0, 0] = 1

    # res = a^n * b % modulus
    res = np.identity(5)
    while n > 0:
        if n % 2:
            res = res.dot(a) % modulus
        n //= 2
        a = a.dot(a) % modulus
    return int(res.dot(b)[0])


def insane_tri_bicolor_tiling(n, r, g, b):
    return sum(f(n, [a, b]) - f(n, [a]) - f(n, [b]) + 1 for a, b in combinations([r,g,b], 2) if n >= a+b) % modulus
