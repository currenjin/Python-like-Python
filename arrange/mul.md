## **문자열이 반복되도록 연산을 해볼까?!**

### 주어지는 정수 n이 있어요. * 문자를 이용해 높이가 n인 삼각형을 출력해보세요!<br><br>
input example:<br>
`3`<br><br>
output example:<br>
```
*
**
***
```
<br><br>
**아마 해당 기능을 모르시는 분들은 for 문을 이용해 기존 문자열에 문자열을 여러 번 붙이는 작업을 할 것 같아요.<br>**
```python
n = int(input().strip())
answer = ''
for i in range(1, n+1):
    answer += '*'
    print(answer)
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 * 연산을 이용해 코드를 획기적으로 줄일 수 있답니다!<br>
```python
n = int(input().strip())
for i in range(1, n+1):
    print('*' * i)
```
<br><br>
추가로, * 연산을 이용해 [123, 456, 123, 456, 123, ...]처럼 123, 456이 여러번 반복되는 리스트를 만들 수 있어요!<br>
```python
n = int(input().strip())
print([123, 456] * n)
```