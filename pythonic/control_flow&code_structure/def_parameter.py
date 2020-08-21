# 함수의 선언과 인수

# 입력되는 a, b값은 정수형이다.
def add_num(a: int, b: int) -> int:
    return a + b

# r = add_num('a', 'b')
r = add_num(10, 20)
print(r)


# 여러 Parameter를 넣는다.(순서대로)
# 미리 값을 지정해도 된다. 하지만 항상 아랫줄이 최신임을 기억하자.
# def menu(entree='beef', drink='wine', dessert='ice'):
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

# menu('beef', 'beer', 'ice')
menu(entree='beef', dessert='ice', drink='beer')


# Default Parameter
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(y)

y = [1, 2, 3]
r = test_func(200, y)
print(y)

# 두 번 반환하면 100이 두 개 나온다.
# 빈 리스트는 한 번만 생성되기 때문에 두 번 실행하면 기존 l을 참조한다.
r = test_func(100)
print(r)
r = test_func(100)
print(r)

# 빈 리스트는 초기화해서 넣으라는 코드를 추가한다.
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)
