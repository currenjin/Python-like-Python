# seek를 사용합니다.

with open('test.txt', 'a') as f:
    f.write('test')

with open('test.txt', 'r') as f:
    # 현재 위치 출력
    print(f.tell())

    # 해당 위치에서 문자 한 개만 출력
    print(f.read(1))

    # 2만큼 이동해서 문자 한 개만 출력
    f.seek(2)
    print(f.read(1))
