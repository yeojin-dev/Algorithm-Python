# finding ugly number
# 참고 문제 : http://codingdojang.com/scode/436


# the naive way
index = int(input())


def max_divide(num1, num2):
    while num1 % num2 == 0:
        num1 //= num2
    return num1


def is_ugly(number):
    num_div_2 = max_divide(number, 2)
    num_div_3 = max_divide(num_div_2, 3)
    result = max_divide(num_div_3, 5)

    if result == 1:
        return True
    else:
        return False


count = 0
number = 0

while count != index:
    number += 1
    if is_ugly(number):
        count += 1

print(number)

# dynamic algorithm
def get_ugly_number(index):

    ugly_numbers = [0] * index
    ugly_numbers[0] = 1

    idx_ugly2 = idx_ugly3 = idx_ugly5 = 0

    next_ugly_by_2 = 2
    next_ugly_by_3 = 3
    next_ugly_by_5 = 5

    for i in range(1, index):
        ugly_numbers[i] = min(next_ugly_by_2, next_ugly_by_3, next_ugly_by_5)

        if ugly_numbers[i] == next_ugly_by_2:
            idx_ugly2 += 1
            next_ugly_by_2 = ugly_numbers[idx_ugly2] * 2

        if ugly_numbers[i] == next_ugly_by_3:
            idx_ugly3 += 1
            next_ugly_by_3 = ugly_numbers[idx_ugly3] * 3

        if ugly_numbers[i] == next_ugly_by_5:
            idx_ugly5 += 1
            next_ugly_by_5 = ugly_numbers[idx_ugly5] * 5

    return ugly_numbers[-1]


index = int(input())

print(get_ugly_number(index))

