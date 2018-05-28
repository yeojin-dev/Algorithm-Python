"""
exponentiation-by-squaring
파이썬 코드로 구현
https://yeojin-dev.github.io/blog/exponentiation-by-squaring/
"""

# The naive way
def pow_naive(base, exponent):
    result = 1
    if exponent != 0:
        while exponent != 0:
            result *= base
            exponent -= 1
        return result
    else:
        return 1

# Exponentiation by squaring
def exponentiation_by_squaring(base, exponent):
    if exponent == 1:
        return base
    if exponent % 2 == 1:
        return base * exponentiation_by_squaring(base, exponent // 2) ** 2
    else:
        return exponentiation_by_squaring(base, exponent // 2) ** 2

# exponentiation_by_squaring(optimized)
def exponentiation_by_squaring_optimized(base, exponent):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result
