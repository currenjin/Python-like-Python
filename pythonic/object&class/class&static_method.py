# 클래스 메소드와 스태틱 메소드

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    # 오브젝트를 안써도 메소드를 가져올 수 있다.
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    # def what_is_your_kind(self):
        #return self.kind

    # 이렇게 쓰는 것도 가능하다.
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

# 오브젝트가 출력
a = Person()
print(a)
print(a.kind)
print(a.x)
print(a.what_is_your_kind())

print('######################################')

# 클래스가 출력
b = Person
print(b)
print(b.kind)
# print(b.x)
print(b.what_is_your_kind())

print('######################################')

# 오브젝트 없이
print(Person.kind)
print(Person.what_is_your_kind())
Person.about(1999)
