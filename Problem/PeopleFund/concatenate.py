import numpy as np


sizes = list(map(int, input().split()))

arr1 = list()
arr2 = list()

for _ in range(sizes[0]):
    arr1.append(list(map(int, input().split())))

for _ in range(sizes[1]):
    arr2.append(list(map(int, input().split())))

print(np.concatenate((np.array(arr1), np.array(arr2)), axis=0))
