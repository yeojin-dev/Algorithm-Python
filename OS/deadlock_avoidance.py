# 단일 리소스 타입에 대한 Banker's Algorithm

n = int(input())
res_max = int(input())
res_allocation = list(map(int, input().split()))
res_available = res_max
res_need = list(map(int, input().split()))


def safty_check(n, res_max, res_allocation, res_available, res_need):
    res_work = res_available.copy()
    finish = [False] * n
    
    while True:
        try:
            for i in n:
                if not finish[i] and res_need[i] <= res_work[i]:
                    work[i] += res_allocation[i]
                    finish[i] = True
                    raise continue_from_first
            return all(result for result in finish)
        except continue_from_first:
            continue
