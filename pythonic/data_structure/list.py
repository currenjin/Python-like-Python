# 리스트를 파악해봅니다.

l = [1, 10, 4, 30, 3, 1]

print(l[0])
print(l[-1])
print(l[2:5])
print(len(l), type(l), sep=', ')
print(l[::-1])

# 각 리스트를 합쳐 이차원 리스트를 만들어 출력한다!
a = ['a', 'b', 'c']
x = [a, l]

print(x)
print(x[0])
print(x[0][1])

a = x + l
print(a)


# 문자열은 이렇게 치환하면 에러나지만 리스트는 가능
a[0] = 'd'
print(a)

a[2:4] = ['E', 'C', 'F']
print(a[:])

# 리스트를 비운다.
a[:] = []
print(a)

# 리스트의 값 추가
l.append(100)
print(l)

l.insert(0, 300)
print(l)

# 리스트 맨 뒤 값을 출력하고 삭제
l.pop()
print(l)

# 리스트 값 삭제
del l[0]
print(l)

l.remove(3)
print(l)

# del l
# print(l)
