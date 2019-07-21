from collections import OrderedDict

n = int(input())
od = OrderedDict()

for _ in range(n):
    i = input().split()
    item = ' '.join(i[:-1])
    price = int(i[-1])
    od[item] = od.get(item, 0) + price

for item, price in od.items():
    print('{} {}'.format(item, price))
