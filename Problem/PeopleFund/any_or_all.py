n = input()
numbers = list(map(int, input().split()))
print(all(number > 0 for number in numbers) and any(str(number) == str(number)[::-1] for number in numbers))
