# property 사용합니다.

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class HyundaiCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model)
        # enable 앞에 _를 붙이며 property를 사용한다는 것을 알린다.
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # property 함수를 선언해서 값을 임의로 바꿀 수 없게 한다.
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # setter 넣으면 임의로 변경이 가능하다.(비밀번호 확인의 용도로도 가능)
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

# 패스워드를 설정
tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
