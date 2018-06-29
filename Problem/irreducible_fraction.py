# 기약분수 구하기
# 참고 문제 : http://www.codeup.kr/JudgeOnline/problem.php?id=2604


# 유클리드 호제법
def get_gcd(num1, num2):
    return get_gcd(num2, num1 % num2) if num1 % num2 else num2


numerator = input().split('.')[1]
denominator = 10 ** len(numerator)
numerator = int(numerator)

gcd = get_gcd(denominator, numerator)

print('{}/{}'.format(
    numerator//gcd,
    denominator//gcd,
))

