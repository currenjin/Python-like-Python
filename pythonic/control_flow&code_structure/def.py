# 함수를 정의합니다.

def say_something():
    s = 'hi'
    return s

# 소괄호를 안쓰면 변수로 인식한다.
say_something()


result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'melon'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)
