# 딕셔너리를 파악해봅니다.
# 키-값 형태
d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])

# 값 변경
d['x'] = 100
print(d)
d['x'] = 'a'
print(d)

# 키 추가
d[1] = 200
print(d)

# 키-값 적용
print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))
