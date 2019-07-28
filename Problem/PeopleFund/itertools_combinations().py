from itertools import combinations

string, n = input().split()
for number in range(1, int(n)+1):
    for characters in combinations(sorted(string), number):
        print(''.join(characters))
