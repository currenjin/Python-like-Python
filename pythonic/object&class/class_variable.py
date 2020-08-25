# 클래스 변수를 사용합니다.

class Person(object):

    # 만약 self.kind가 아닌 그냥 kind 변수일 경우 해당 변수를 모든 오브젝트가 공유한다.
    kind = 'human'

    def __init__(self, name):
        # self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()



class T(object):
    # words = []
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)
