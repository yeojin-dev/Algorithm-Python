from itertools import combinations_with_replacement

string, n = input().split()
for characters in combinations_with_replacement(sorted(string), int(n)):
    print(''.join(characters))
