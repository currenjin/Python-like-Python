# IN을 사용합니다.

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

#if not a == b:
#    print('not equal')

if a != b:
    print('not equal')
# 더 직관적으로 보기 위해선 부등호를 사용한다.

#is_ok = True
is_ok = 1
if is_ok:
    print('True')

is_ok = []
if is_ok:
    print('True')
else:
    print('False')
