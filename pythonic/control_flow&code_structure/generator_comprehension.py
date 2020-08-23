# 제네레이터 내포 표기

# 0부터 9까지를 짝수만 제네레이터에 저장
def g():
    for i in range(10):
        if i % 2 == 0:
            yield i
g = g()
print(next(g))
print(next(g))
print(next(g))

# 위 코드를 comprehension으로
g = (i for i in range(10) if i % 2 == 0)
print(next(g))
print(next(g))
print(next(g))

# ()으로 표시하지만 튜플타입으로 만들어지지 않는다.
# 튜플로 만들고자하면 tuple()형식으로 지정
