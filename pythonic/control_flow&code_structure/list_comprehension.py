# 리스트 내포 표기

t = (1, 2, 3, 4, 5)

# t의 내용을 r에 집어넣는 것
r = []
for i in t:
    r.append(i)
print(r)

# 위 코드를 이 방법으로 할 수 있다.
r = [i for i in t]
print(r)


# 짝수만 저장
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

# 위 코드를 이 방법으로 할 수 있다.
r = [i for i in t if i % 2 == 0]
print(r)
