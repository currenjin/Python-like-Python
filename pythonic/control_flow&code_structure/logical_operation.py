# 논리 연산자를 사용합니다.

a = 2
b = 2

# 같은가
a == b

# 다른가
a != b

# a가 더 큰가
a > b

# b가 더 큰가
a < b

# a가 같거나 더 큰가
a >= b

# b가 같거나 더 큰가
a <= b

# a와 b가 둘 다 0인가
if a > 0 and b > 0:
    print('a and b = 0')

# a와 b가 둘 중 하나라도 0인가
if a > 0 or b > 0:
    print('a or b = 0')
