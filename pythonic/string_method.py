# string method를 활용해봅니다.

s = 'My name is Hyunjin. Hi Hyunjin'
print(s)
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('X')
print(is_start)

print("##################")

# 각각 맨 앞/맨 뒤부터 해당 변수에서 문자의 인덱스를 찾아준다.
print(s.find('Hyunjin'))
print(s.rfind('Hyunjin'))

# 맨 앞 문자만 대문자
print(s.capitalize())

# 각 단어의 제일 앞 문자만 대문자
print(s.title())

# 모두 대문자 및 소문자
print(s.upper())
print(s.lower())

# 문자를 치환
print(s.replace('Hyunjin', 'Jeong'))
