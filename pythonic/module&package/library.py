# 표준 라이브러리
# https://docs.python.org/ko/3/library/index.html

s = "fdsafadsfadsfsaddasgreabvfbftrnb"

# s의 글자 수를 세는 것
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

# 표준 라이브러리의 collections를 사용하면
from collections import defaultdict

d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)
print(d['f'])
