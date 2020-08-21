# DocStrings를 사용한다.

# 설명은 함수 안에 넣는게 좋다.
def example_func(param1, param2):
    """
    hi
    """
    print(param1)
    print(param2)
    return True

# 확인하기
print(example_func.__doc__)
help(example_func)
