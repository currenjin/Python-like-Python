# 특수 메소드를 사용합니다.

class Word(object):

    # 이 생성자가 특수 메소드다.
    def __init__(self, text):
        self.text = text

    # 문자열을 읽어왔을 때 출력하는 특수 메소드이다.
    def __str__(self):
        return 'Word!!!!'

    # 길이를 가져오는 특수 메소드이다.
    def __len__(self):
        return len(self.text)

    # 더하는 특수 메소드이다.
    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    # 입력된 값이 서로 같은가를 판단하는 특수 메소드이다.
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('##############')
w3 = Word('test')
print(w)
print(len(w))
print(w + w2)
print(w == w2)
print(w == w3)
