# 파이썬의 내장함수
# https://docs.python.org/ko/3/library/functions.html

import builtins

# 그냥 print하는 내용은 사실 builtins에 존재함.
builtins.print('hi')

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# 점수가 높은 순대로 정렬
print(sorted(ranking, key=ranking.get, reverse=True))
