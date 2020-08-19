# 복사 시 주의해야한다.
x = {'a': 1}
y = x
y['a'] = 1000

# 주소가 복사되기 때문에 역시 함께 바뀐다.
print(x)
print(y)

# copy 사용
x = {'a': 1}
y = x.copy()
y['a'] = 1000

print(x)
print(y)
