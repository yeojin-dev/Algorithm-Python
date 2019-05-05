from collections import Counter

shoes_cnt = input()
shoes = Counter(map(int, input().split()))
customer_cnt = int(input())

money_earned = 0
for customer in range(customer_cnt):
    size, price = tuple(map(int, input().split()))
    if shoes.get(size):
        money_earned += price
        shoes[size] -= 1

print(money_earned)
