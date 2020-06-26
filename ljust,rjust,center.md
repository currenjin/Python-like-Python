## **정렬을 보다 심플하게!**

### 문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌/중/우로 정렬한 길이 n인 문자열을 한 줄씩 출력하세요.<br><br><br> ###
**단 조건이 있어요.<br><br>**
s의 길이는 n보다 작아요.<br>
(n - s의 길이)는 짝수에요.<br>
s는 알파벳과 숫자로만 이루어져 있으며, 공백 문자가 포함되어있지 않아요.<br><br><br>
input example:<br>
`abc 7`<br><br>
output example:<br>
```
abc<br>
    abc<br>
        abc<br>
```
<br><br>
이런 문제가 생겼을 때 저 같은 경우는 이렇게 했습니다!<br>
```python
s, n = input().strip().split(' ')
print("{:<{n}}".format(s, n=n))
print("{:^{n}}".format(s, n=n))
print("{:>{n}}".format(s, n=n))
```
<br><br>
그리고 정렬에 대한 기능을 모르는 분들은 아마 이렇게 작성하셨을거라 예상돼요.<br>
```python
### 우측정렬
s, n = input().strip().split(' ')

answer = ''
for i in range(n-len(s)):
    answer += ' '
answer += s
print(answer)
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 **ljust, center, rjust** 이라는 string의 메소드를 이용해 아주아주 쉽게 코드를 작성할 수 있어요.<br>
```python
s, n = input().strip().split(' ')

print(s.ljust(int(n)))
print(s.center(int(n)))
print(s.rjust(int(n)))
```
너무너무 유용합니다.<br><br>
시도해보신다면 원하는 결과가 출력되는.. 아주 쉽게 출력이 되는 모습을 볼 수 있어요!<br><br>