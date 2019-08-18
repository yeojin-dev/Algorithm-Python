superset = set(input().split())
print(all(superset.issuperset(set(input().split())) for _ in range(int(input()))))
