# dictionary method

d = {'x': 10, 'y': 20}

print(help(dict))

print(d.keys())
print(d.values())

# d2의 내용을 d에 덮어쓰기
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)

print(d.get('x'))

# 값이 없기에 아무것도 안나온다.
r = d.get('z')
print(type(r))

# 키-값 삭제
d.pop('x')
print(d)
del d['y']
print(d)
# del d
d.clear()
print(d)

# 값이 있는지 판별
print('j' in d)
