#1d
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a.ndim)   # 1

#2d
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b)
print(b.ndim)   # 2

#3d
c = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(c)
print(c.ndim)   # 3
