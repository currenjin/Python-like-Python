# 다중 상속을 사용합니다.

class Person(object):
    def talk(self):
        print('talk')

class Car(object):
    def run(self):
        print('run')

# 위 두 클래스를 같이 상속하는 것(추천은 안함)
# 각 상속받은 클래스에 같은 함수가 있다면 왼쪽 클래스의 함수가 우선순위
class PersionCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersionCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
