import random

def counting_sort(list, exp):
    length = len(list)
    output = [0] * length
    count = [0] * 10

    for i in range(length):
        index = list[i] // exp
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in list[::-1]:
        index = i // exp
        output[count[(index) % 10] - 1] = i
        count[(index) % 10] -= 1

    for i in range(length):
        list[i] = output[i]

def radix_sort(list):
    max_value = max(list)

    exp = 1
    while max_value // exp > 0:
        counting_sort(list, exp)
        exp *= 10

    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(radix_sort(num_list.copy()))

