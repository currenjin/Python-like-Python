# 제너레이터를 사용합니다.

l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


# 위 코드를 제너레이터로 표현하면?
def greeting():
    yield 'Good morning'
    for i in range(5):
        print(i)
    yield 'Good afternoon'
    for i in range(5):
        print('run')
    yield 'Good night'

for g in greeting():
    print(g)

# 제너레이터같은 경우에는 값을 한 번에 출력하지 않을 수 있어 편하다.

g = greeting()
print(next(g))
print(next(g))
print('@@@@')
print(next(g))
