# 집합을 파악해봅니다.

a = {1, 2, 2, 3, 4, 4, 4, 4, 5, 6}

# 중복된 값을 없애고 유니크한 값만 출력
print(a)
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)

# 해당되는 값을 연산한다. (not, and, or, xor)
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)
