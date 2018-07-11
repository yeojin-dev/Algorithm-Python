import random

def quick_sort_pythonic(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort_pythonic(less) + [pivot] + quick_sort_pythonic(greater)

def partition(list, start, end):
    pivot = list[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] > pivot:
            right -= 1
        if right < left:
            done = True
        else:
            list[left], list[right] = list[right], list[left]
    list[start], list[right] = list[right], list[start]  # 피봇 교환
    return right

def quick_sort_cpp_style(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort_cpp_style(list, start, pivot - 1)
        quick_sort_cpp_style(list, pivot + 1, end)
    return list

def quick_sort_iterative(list, start, end):
    stack = []
    stack.append(start)
    stack.append(end)

    while stack:
        end = stack.pop()
        start = stack.pop()
        pivot = partition(list, start, end)

        if pivot - 1 > start:
            stack.append(start)
            stack.append(pivot - 1)

        if pivot + 1 < end:
            stack.append(pivot + 1)
            stack.append(end)

    return list

num_list = list()

for i in range(20):
    num = random.randrange(500)
    num_list.append(num)

print(quick_sort_iterative(num_list.copy(), 0, len(num_list) - 1))

