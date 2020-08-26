# 파일을 조작합니다.

# 파일을 여는데 없다면 생성해서 test라는 문자를 입력하고 저장합니다.
f = open('test.txt', 'w')

# a는 파일에 내용을 추가하는 역할을 합니다.
# f = open('test.txt', 'a')

# r은 파일을 읽는 역할을 합니다.
# f = open('test.txt', 'r')

f.write('test\n')
# print('My', 'name', 'is', 'Hyunjin', file=f)

# 파일을 닫습니다.
f.close()
