# Python은 None을 어떻게 바라볼까?

is_empty = None
#print(help(is_empty))
if is_empty is None:
    print('None!!')

# 1과 True가 서로 같은지를 비교하기 떄문에 False 출력
print(1 is True)

a = 0
if a is not None:
    print('Not None!!')
