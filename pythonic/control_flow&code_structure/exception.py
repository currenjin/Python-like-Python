# 예외처리

l = [1, 2, 3]
i = 5

# 에러에 대한 예외처리를 진행합니다. 인덱스 에러로인한 프로그램 종료되지 않음
try:
    l[i]
# except:
# except IndexError:
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print("Don't worry: {}".format(ex))
except Exception as ex:
    print('other: {}'.format(ex))
# 성공시 실행하는 else
else:
    print('done')
# 무조건 실행하는 finally
finally:
    print('clean up')


# 독자 예외 작성
class UppercaseError(Exception):
    pass

# 모든 문자가 대문자라면 에러를 출력(공동 개발 시에는 설명을 붙이는게 좋다)
def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go next')
