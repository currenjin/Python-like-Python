# namespace & scope

# 로컬 변수와 글로벌 변수의 차이(함수 안에서의 변수와 함수 밖에서의 변수)
animal = 'cat'

def f():
    animal = 'dog'
    print('local:', animal)
    print(locals())
    # animal = 'dog' ERROR,
f()
print('global:', animal)
print(globals())


# 함수의 main
def m():
    """TEST"""
    print(m.__name__)
    print(m.__doc__)

print(__name__)
