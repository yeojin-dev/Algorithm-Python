def fibonacci(index):
    if index < 2:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


mem = [0] * 19  # memory for dynamic algorithm


def fibonacci_dynamic(index):
    if index < 2:
        return index

    mem_index = index - 2

    if mem[mem_index]:
        return mem[mem_index]
    else:
        mem[mem_index] = fibonacci(index - 1) + fibonacci(index - 2)
        return mem[mem_index]


for i in range(1, 21):
    print(fibonacci_dynamic(i))
