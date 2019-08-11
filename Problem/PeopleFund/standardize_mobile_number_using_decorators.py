def wrapper(f):
    def fun(l):
        f([f"+91 {number[-10:-5]} {number[-5:]}" for number in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
