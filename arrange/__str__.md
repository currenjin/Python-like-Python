## **클래스 인스턴스를 출력해보세요!**
<br>

### 2차원 평면 위의 점을 나타내는 Coord 클래스의 인스턴스를 (x 값, y 값)으로 출력하세요!<br><br>
**많은 사람들은 아래와 같이 클래스 바깥에 출력 함수를 만들거나, print 문 안에서 format을 지정해요.<br>**
```python
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

point = Coord(1, 2)
print('({}, {})'.format(point.x, point.y))
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 __str__ 메소드를 사용해 class 내부에서 출력 format을 지정할 수 있습니다.<br>
```python
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
```