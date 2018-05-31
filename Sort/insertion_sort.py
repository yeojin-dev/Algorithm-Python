import random

def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        curr_value = list[i]
        index = i
        while index > 0 and list[index - 1] > curr_value:
            list[index] = list[index - 1]
            index -= 1
        list[index] = curr_value
    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(insertion_sort(num_list.copy()))

