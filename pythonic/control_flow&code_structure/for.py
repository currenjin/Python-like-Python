# for문을 사용합니다. for else문과 continue, break도 사용합니다.

list = [1, 2, 3, 4, 5]
for i in list:
    print(i)
# 이렇게 반복 처리하는 것을 iterator라고한다.

# break를 사용합니다.
for i in ['My', 'name', 'is', 'Hyunjin']:
    if i == 'name':
        break
    print(i)

# continue를 사용합니다.
for i in ['My', 'name', 'is', 'Hyunjin']:
    if i == 'name':
        continue
    print(i)

# for else
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all!')

# for문으로 dictionary 처리
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)
