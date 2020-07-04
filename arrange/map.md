## **모든 멤버의 Type을 변환해볼까?**

### solution 함수는 문자열 리스트를 mylist를 입력받아요. 이 리스트를 정수형 리스트로 바꿔주세요!<br><br>
input example:<br>
`['1','100','33']`<br><br>
output example:<br>
`[1,100,33]`<br><br>
단, 문자열에는 숫자만이 들어가있답니다!<br><br><br>

**아마 해당 함수에 대해서 알지 못 하시는 분들은 아래와 같이 작성할 수 있다고 생각돼요.<br>**
```python
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(int(i))
    return answer
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에는 map 함수가 존재해요!<br>
이 함수를 이용하면 for 문을 사용하지 않아도 멤버 타입을 단번에 변환할 수 있답니다.<br>
```python
def solution(mylist):
    answer = list(map(int, mylist))
    return answer
```
<br><br>
`map(적용 함수, 적용하는 요소)`<br><br>
**아래 처럼 map 함수를 이용해 다른 함수로 적용을 시킬 수도 있습니다!**<br><br>
example input:
```python
def Add(a):
    return a + a

b = [1,2,3,4,5]
print(list(map(Add, b)))
```
<br>

output:
```
[2, 4, 6, 8, 10]
```
<br>

**파이썬은 정말 알면 알수록 매력적인 언어같아요.**
