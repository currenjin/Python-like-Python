# 사전형 내포 표기

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

# d라는 사전형에 w, f를 저장하기
d = {}
for x, y in zip (w, f):
    d[x] = y
print(d)

# 위 코드를 comprehension으로
d = {x: y for x, y in zip(w, f)}
print(d)
