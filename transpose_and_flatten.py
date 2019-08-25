import numpy as np

arr = list()
for _ in range(int(input().split()[0])):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
print(arr.transpose())
print(arr.flatten())
