# 한 줄이 길어져 읽기 어려울 경우 '\'를 이용해 다음 줄도 이어서 작성할 수 있습니다.

s = 'aaaaaaa' \
    + 'bbbbbbbb'
print(s)

# 또, 소괄호로 묶을 수도 있다.

s = ('cccccc'
    + 'dddddddd')
print(s)

# 문자를 한 줄에 80개 이상 사용하면 다음 줄로 넘겨야한다.
