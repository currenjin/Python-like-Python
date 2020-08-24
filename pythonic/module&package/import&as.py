# Import와 AS

# 패키지만 가져오기
# import package_1.utils
# r = package_1.utils.say_twice('hello')

# 패키지의 모듈만 가져오기
from package_1 import utils
r = utils.say_twice('hello')

# 패키지의 모듈 안 함수만 가져오기(추천은 안함)
# from package_1.utils import say_twice
# r = say_twice('hello')

# 패키지의 모듈을 가져와서 별칭을 정하기(추천은 안함)
# from package_1 import utils as u
# r = u.say_twice('hello')

print(r)
