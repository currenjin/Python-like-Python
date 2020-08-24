# 상대경로로 임포트한 모습(추천은 안한다)

from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')
