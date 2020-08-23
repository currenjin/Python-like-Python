# 람다를 사용합니다.

# 예로, 대소문자를 잘 못 입력했을 때 앞 글자만 대문자로 변경
l = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'Sun']

# change_words의 출력 부분에서 func는 람다함수에서 대문자로 변경해 가져온다.
def change_words(words, func):
    for word in words:
        print(func(word))

# 람다를 이용하면 아래 코드와 같은 방식을 사용한다.
# sample_func = lambda word: word.capitalize()
# def sample_func(word):
#     return word.capitalize()

# change_words(l, sample_func)


# 람다를 한 번에 사용하면 더욱 편리하다.
change_words(l, lambda word: word.capitalize())
