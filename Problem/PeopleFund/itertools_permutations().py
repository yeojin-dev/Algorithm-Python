from itertools import permutations

string, number = input().split()
print('\n'.join([''.join(i) for i in permutations(sorted(string), int(number))]))
