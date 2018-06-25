import random

def selection_sort(list):
    length = len(list)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if list[min_index] > list[j]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(selection_sort(num_list.copy()))

