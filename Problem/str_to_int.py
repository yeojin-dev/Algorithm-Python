# python int() 메소드 구현하기

def str_to_int(num):
    result = 0
    for digit in num:
        result *= 10
        result += ord(digit) - ord('0')
    return result

