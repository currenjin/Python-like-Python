# 쓰기와 읽기를 동시에

s = """\
AAA
BBB
CCC
DDD
"""

# w: 쓰기, +: 읽기
with open('test.txt', 'w+') as f:
    f.write(s)

    # 제일 앞으로 가서 출력
    f.seek(0)
    print(f.read())
