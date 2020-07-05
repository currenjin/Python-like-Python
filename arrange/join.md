## **Sequence 멤버를 하나로 이어붙여보자!**

### 문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 함수를 리턴해보세요!<br><br>
input example:<br>
`['1','100','33']`<br><br>
output example:<br>
`'110033`<br><br><br>

**이 문제와 연관된 함수를 모르시는 분들은 아마 아래처럼 작성할 것 같아요.<br>**
```python
def solution(mylist):
    answer = ''
    for i in mylist:
        answer += i
    return answer
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 join 함수를 사용하면 코드를 아주 간단하게 줄일 수 있답니다!<br>
```python
def solution(mylist):
    return ''.join(mylist)
```
<br><br>
**join 함수**<br>
join 함수는 리스트 문자열들을 합치는 역할을 해요.<br>
위 처럼 문자열을 붙이는 방법을 사용하기도 하겠지만 문자열 사이사이에 특정 패턴을 넣을 수도 있답니다!<br><br>
input example:
```python
def solution(mylist):
    return '-'.join(mylist)
```
<br>output:<br>
`1-100-33`<br><br>
문자열들을 심플하게 다룰 수 있는 join 함수였습니다!<br>

