import numpy as np

dimension = int(input())
matrix = [list(map(float, input().split())) for _ in range(dimension)]
print(round(np.linalg.det(matrix), 2))
