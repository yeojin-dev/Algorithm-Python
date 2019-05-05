def swap_case(s):        
    return ''.join(letter.swapcase() for letter in s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
