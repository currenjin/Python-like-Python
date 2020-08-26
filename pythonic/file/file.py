# 파일을 조작합니다.

# 파일을 여는데 없다면 생성해서 test라는 문자를 입력하고 저장합니다.
f = open('test.txt', 'w')

# a는 파일에 내용을 추가하는 역할을 합니다.
# f = open('test.txt', 'a')

# r은 파일을 읽는 역할을 합니다.
# f = open('test.txt', 'r')

f.write('test\n')
print('My', 'name', 'is', 'Hyunjin', file=f)

# 파일을 닫습니다.
f.close()


# f.close()를 까먹을 수 있다면 with를 사용한다.
with open('test.txt', 'a') as f:
    f.write('test')

# 파일을 읽어오기
with open('test.txt', 'r') as f:
    # print(f.read())
    # 한 줄씩 읽어오기
    while True:
        line = f.readline()
        print(line, end='')
        # 3글자 씩
        # chunk = 3
        # line = f.read(chunk)
        # print(line)
        if not line:
            break
