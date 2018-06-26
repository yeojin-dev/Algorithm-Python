import random

numbers = sorted([random.randrange(1000) for i in range(20)])
value = random.choice(numbers)


def binary_search(list, value, low=0, high=0):
    if low > high:
        return False
    mid = (low + high) // 2
    if value > list[mid]:
        return binary_search(list, value, mid + 1, high)
    elif value < list[mid]:
        return binary_search(list, value, low, mid - 1)
    else:
        return mid


result = binary_search(numbers, value, low=0, high=len(numbers)-1)
print(result)
