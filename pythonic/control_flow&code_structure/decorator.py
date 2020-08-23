# 데코레이터를 사용합니다.

def print_info(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

@print_info
def sub_num(a, b):
    return a - b

add_num(10, 20)

sub_num(20, 10)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)
