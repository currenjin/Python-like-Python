# 문자열을 자를 수 있는 인덱스 slice입니다.
word = 'python'

print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
# Error string index out of range
# print(word[100])

# Error object does not support item assignment
# word[0] = 'j'
word = 'j' + word[1:]
print(word)
print(word[:])
print(len(word))
