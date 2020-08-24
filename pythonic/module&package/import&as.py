# Import와 AS

# 패키지만 가져오기
# import package.tools.utils
# r = package.utils.say_twice('hello')

# 패키지의 모듈만 가져오기
# from package.tools import utils
# r = utils.say_twice('hello')

# 패키지의 모듈 안 함수만 가져오기(추천은 안함)
# from package.tools.utils import say_twice
# r = say_twice('hello')

# 패키지의 모듈을 가져와서 별칭을 정하기(추천은 안함)
# from package.tools import utils as u
# r = u.say_twice('hello')

# print(r)


# from package.talk import human
# r = human.sing()
# 해당 모듈은 절대경로로 함수를 참조함
# r = human.cry()

# print(r)

# __init__파일에서 all 항목을 넣어 애스터리스크를 사용 가능했다.(추천은 안함)
# from package.talk import *

# print(animal.sing())
# print(animal.cry())
# print(human.sing())
# print(human.cry())


# 옛 버전과 새 버전 간의 오류를 해결하기 위한 예외처리
# try:
#     from package import utils
# except:
#     from package.tools import utils

# r = utils.say_twice('word')
# print(r)
