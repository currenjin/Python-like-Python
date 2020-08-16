# Pythonic Code Style

파이써닉한 코드 작성을 위해 생각하고 정리하는 공간이에요.<br>
목적은 누가봐도 알기 쉬운 코드를 작성하는 것이죠.

## 기본

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

- 변수를 문장처럼 사용해보자!
<br>`my_name_is = hyunjin`
<br>

- [반올림 및 수학 함수](./round.py)
```python
import math
print(help(math))

# 반올림
pie = 3.1415
print(round(pie, 2))
```
<br>

- [문자열 인덱스 슬라이싱](./slice.py)
```python
word = python
print(word[0])
print(word[1])

# 문자 치환
word = 'j' + word[1:]

# 문자열 전체 출력
print(word[:])

# 문자열의 길이
print(len(word))
```
<br>

- [문자의 메소드](./string_method.py)
```python
s = 'My name is Hyunjin. Hi Hyunjin'

# 첫 단어에 My가 있으면 True
is_start = s.startswith('My')
print(is_start)

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
```
<br>

- [문자열 포맷과 f-strings](./format&f-strings.py)
```python
# 문자열의 format을 사용해봅니다.
print('a is {}'.format('a'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {0} {1}'.format('Jeong', 'Hyunjin'))
print('My name is {0} {1}. My Family name is {0} '.format('Jeong', 'Hyunjin'))
print('My name is {family} {name}. My Family name is {family} '.format(family='Jeong', name='Hyunjin'))


# Python 3.6부터는 format대신 f-string이 사용가능합니다. 활용도와 처리속도가 높아 좋습니다!
family = 'Jeong'
name = 'Hyunjin'
print(f'My name is {family} {name}. My Family name is {family}')
```
<br>

</details>
<br>

## 데이터 구조

<details markdown="1">
<summary>접기/펼치기</summary>

<br>




<br>

<details>
<br>
