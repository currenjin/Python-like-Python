# 리스트의 복사를 주의하세요.

# i의 주소값을 복사하기 때문이다.
i = [1, 2, 3, 4, 5]
j = i
j[0]

print('j =', j)
print('i =', i)

X = ['a', 'b']
Y = X
Y[0] = 't'

print(id(X))
print(id(Y))
print(X)
print(Y)

X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))
print(X)
print(Y)


# 복사
x = [1, 2, 3, 4, 5]
y = x.copy()
#y = x[:]
y[0] = 100

print('y = ', y)
print('x = ', x)
