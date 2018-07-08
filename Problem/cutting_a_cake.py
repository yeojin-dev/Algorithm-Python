# 케이크 자르기
# 참고 문제 : http://www.codeup.kr/JudgeOnline/problem.php?id=2628


a, b = map(int, input().split())
c, d = map(int, input().split())

if a > b:
    a, b = b, a

count = 0

for i in c, d:
    if a < i < b:
        count += 1

if count == 1:
    print('cross')
else:
    print('not cross')

