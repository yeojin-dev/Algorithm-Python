import random

def cocktail_sort(list):
    start = 0
    end = len(list) - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        for i in range(end, start, -1):
            if list[i-1] > list[i]:
                list[i], list[i-1] = list[i-1], list[i]
                swapped = True

        if not swapped:
            break

        start += 1

    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(cocktail_sort(num_list.copy()))
