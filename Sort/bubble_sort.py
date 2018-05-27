import random

def bubble_sort(list):
    length = len(list)
    for i in range(length, 0, -1):
        for j in range(i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(selection_sort(num_list.copy()))
