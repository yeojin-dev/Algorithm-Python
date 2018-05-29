import random

def merge_sort(list):
    length = len(list)
    if length > 1:
        mid = length // 2
        left_list = list[:mid]
        right_list = list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = 0
        j = 0
        k = 0

        length_right = len(right_list)
        length_left = len(left_list)

        while i < length_left and j < length_right:
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1

        while i < length_left:
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < length_right:
            list[k] = right_list[j]
            j += 1
            k += 1

    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(selection_sort(num_list.copy()))

