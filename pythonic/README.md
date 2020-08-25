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

- [반올림 및 수학 함수](./basic/round.py)
```python
import math
print(help(math))

# 반올림
pie = 3.1415
print(round(pie, 2))
```
<br>

- [문자열 인덱스 슬라이싱](./basic/slice.py)
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

- [문자의 메소드](./basic/string_method.py)
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

- [문자열 포맷과 f-strings](./basic/format&f-strings.py)
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

## 데이터 구조

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

### [List](./data_structure/list.py)

- [list 메소드](./data_structure/list_method.py)
- [list 복사](./data_structure/list_copy.py)
<br>

### [Tuple](./data_structure/tuple.py)

- [tuple 언패킹](./data_structure/tuple_unpacking)
<br>

### [Dictionary](./data_structure/dictionary.py)

- [dictionary 메소드](./data_structure/dictionary_method.py)
- [dictionary 복사](./data_structure/dictionary_copy.py)
<br>

### [Set](./data_structure/set.py)

- [set 메소드](./data_structure/set_method.py)
<br>
<br>

</details>

## 제어 흐름과 코드 구조

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

### 반복문

- [while(else, continue, break)](./control_flow&code_structure/while.py)
- [for(else, continue, break)](./control_flow&code_structure/for.py)
<br>

### 조건문

- [if](./control_flow&code_structure/if.py)
- [값이 있는지 확인](./control_flow&code_structure/in.py)
<br>

### 함수

- [함수의 정의](./control_flow&code_structure/def.py)
- [parameter](./control_flow&code_structure/def_parameter.py)
- [input](./control_flow&code_structure/input.py)
- [range](./control_flow&code_structure/range.py)
- [zip](./control_flow&code_structure/zip.py)
- [enumerate](./control_flow&code_structure/enumerate.py)
- [함수 안에 함수가?](./control_flow&code_structure/def_in_def.py)
- [함수의 설명을 넣어보자!](./control_flow&code_structure/docstrings.py)
- [parameter to tuple, dictionary](./control_flow&code_structure/parameter_tup,dic.py)
<br>

### Comprehensions

- [List](./control_flow&code_structure/list_comprehension.py)
- [Dictionary](./control_flow&code_structure/dictionary_comprehension.py)
- [Set](./control_flow&code_structure/set_comprehension.py)
- [Generator](./control_flow&code_structure/generator_comprehension.py)
<br>

### [주석](./control_flow&code_structure/comment.py)
### [논리 연산](./control_flow&code_structure/logical_operation.py)
### [None](./control_flow&code_structure/comment.py)
### [한 줄이 길어진다면?](./control_flow&code_structure/next_line.py)
### [예외 처리](./control_flow&code_structure/exception.py)
### [Namespace&Scope](./control_flow&code_structure/namespace&scope.py)
<br>

### [Decorator](./control_flow&code_structure/decorator.py)
### [Generator](./control_flow&code_structure/generator.py)
### [Lambda](././control_flow&code_structure/lambda.py)
<br>
<br>

</details>

## 모듈과 패키지

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

### [모듈과 패키지를 만들어 Import](./module&package/import&as.py)
### [\_\_name\_\_, \_\_main\_\_](./module&package/name&main.py)
### [내장 함수](./module&package/builtin_function.py)
- [공식 문서](https://docs.python.org/ko/3/library/functions.html)
### [표준 라이브러리](./module&package/library.py)
- [공식 문서](https://docs.python.org/ko/3/library/index.html)
<br>
<br>

</details>

## 객체와 클래스

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

### [Class](./object&class/class.py)
- [클래스 상속](./object&class/class_inheritance.py)
- [클래스 다중상속](./object&class/class_multiple_inheritance.py)
- [클래스 변수](./object&class/class_variable.py)
- [클래스 메소드와 스태틱 메소드](./object&class/class&static_method.py)
<br>

### [메소드 오버라이딩](./object&class/method_override.py)
### [특수 메소드](./object&class/special_method.py)
<br>

### [property](./object&class/property.py)
### [덕타이핑](./object&class/duck_typing.py)
<br>
<br>

</details>
