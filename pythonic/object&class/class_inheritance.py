# 클래스의 상속

# 상속자(object를 썼다)
class Car(object):
    def run(self):
        print('run')

# 상속된 자식
class HyundaiCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

# 상속자 오브젝트
car = Car()
car.run()

print('#####')

# 상속된 클래스의 오브젝트
hyundai_car = HyundaiCar()
hyundai_car.run()
# Hyundai_car.auto_run() 불가능하다.

print('#####')

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
