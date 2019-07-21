m, n = [set(input().split()) for _ in range(4)][1::2]
print("\n".join(sorted(m.union(n)-m.intersection(n),key=int)))
