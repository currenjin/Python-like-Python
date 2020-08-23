# 집합 내포 표기

s = set()

# 1부터 9까지를 짝수만 집합에 넣는다.
for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

# 위 코드를 comprehension으로
s = {i for i in range(10) if i % 2 == 0}
print(s)
