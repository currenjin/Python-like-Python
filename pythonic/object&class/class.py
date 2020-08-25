# 클래스의 정의

# python3에서는 object를 안쓰고 ():만 사용해도 됨
# class Person(object):
class Person():

    # 클래스 초기화(자기 이름을 프린트)
    def __init__(self, name='Default'):
        self.name = name
        print(self.name)

    # 메소드
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(3)

    # 다른 메소드에서 언급
    def run(self, num):
        print('run' * num)

person = Person('HyunJIn')
person.say_something()

# def persion(name):
#    if name == 'A':
#        print('hello')
