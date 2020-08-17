# 리스트의 메소드를 활용해봐요.

r = [1, 2, 3, 4, 5, 1, 2, 3]

# 위치 검색
print(r.index(3))
print(r.index(3, 3))

# 리스트 값 카운트
print(r.count(3))

# 리스트 정렬
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

# 문자를 각 기준에 따라 리스트 값으로 변경
s = 'My name is Hyunjin.'
to_split = s.split(' ')
print(to_split)

# 리스트의 각 값 사이에 해당 값을 넣어 문자열로 출력
x = ' '.join(to_split)
print(x)

print(help(list))
