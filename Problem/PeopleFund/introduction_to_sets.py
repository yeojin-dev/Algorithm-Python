def average(array):
    array_set = set(array)
    return sum(num for num in array_set) / len(array_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
