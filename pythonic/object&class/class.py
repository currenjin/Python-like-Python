# 클래스의 정의

# python3에서는 object를 안쓰고 ():만 사용해도 됨
# class Person(object):
class Person():

    # 생성자이자 클래스 초기화(자기 이름을 프린트)
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


    # 소멸자(해당 오브젝트를 더이상 안쓸 때 실행된다.)
    def __del__(self):
        print('good bye')

person = Person('HyunJIn')
person.say_something()

# 소멸자 실행
del person
print('###########')
