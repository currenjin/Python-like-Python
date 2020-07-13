## **짝수인 값만을 제곱해보세요!**

### 정수를 담은 mylist를 입력받아 원소 중 짝수인 값만을 제곱해 새 리스트를 리턴하는 solution 함수를 완성해주세요.<br><br>
input example:<br>
`[3,2,6,7]`<br><br>
3은 홀수이므로 무시합니다.<br>
2는 짝수이므로 제곱합니다.<br>
6은 짝수이므로 제곱합니다.<br>
7은 홀수이므로 무시합니다.<br><br>
output example:<br>
`[4, 36]`<br><br><br>
**특정 기능을 모르시는 많은 분들은 아마 아래와 같이 for문 안에 if문을 사용할 것이라고 예상돼요!<br>**
```python
def solution(mylist):
    answer = []
    for i in mylist:
        if i % 2 == 0:
            answer.append(i**2)
    return answer
```
<br><br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 list comprehension을 이용해 for문과 if문을 한 번에 처리할 수 있답니다!<br>
```python
def solution(mylist):
    answer = [i ** 2 for i in mylist if i % 2 == 0]
    return answer
```
<br>
초보자 분들은 이해하시기엔 무리일 수 있는 문법입니다. 아래는 문법인데요!<br>

`["async"] "for" target_list "in" or_test [comp_iter]`<br><br>

[여기](https://docs.python.org/3/reference/expressions.html?highlight=list%20comprehension#displays-for-lists-sets-and-dictionaries)를 클릭해 list comprehension syntax를 확인해주시는 것도 학습에 대한 좋은 방법입니다. :)<br>
