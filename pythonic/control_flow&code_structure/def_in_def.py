# 함수 안의 함수

# 밖에서 사용할 필요가 없을 때 사용
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)


# 클로저

def outer(a, b):

    def inner():
        return a + b

    return inner

# print(outer(1, 2))

# outer 1, 2를 선언한 시점에서 outer의 return inner를 f에 집어넣는다.
f = outer(1, 2)

# 이제 inner가 실행이 되고 a와 b는 1, 2니까 3을 돌려준다.
r = f()
print(r)

# 보통 값을 저장하고 나눠 계산하고 싶을 때 사용한다.
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
