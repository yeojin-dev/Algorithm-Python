from itertools import product

print(*list(product(map(int, input().split()), map(int, input().split()))))
