# 메소드 오버라이드

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class HyundaiCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        # 부모의 함수를 불러올 때에는 super()를 사용한다.
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('#####')

hyundai_car = HyundaiCar('Sonata')
print(hyundai_car.model)
hyundai_car.run()

print('#####')

tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
