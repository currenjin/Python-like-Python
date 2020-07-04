## **알파벳을 모두 출력해볼까?**

### 입력으로 0을 주면 소문자 알파벳, 입력으로 1을 주면 대문자 알파벳을 사전 순으로 출력하세요!<br><br><br>
input example:<br>
`0`<br><br>
output example:<br>
`abcd...`<br><br><br>
input example:<br>
`1`<br><br>
output example:<br>
`ABCD...`<br><br><br>
**아마 많은 분들은 이렇게 알파벳을 출력하기 위해 모두! 입력할 것 같아요.<br>**
`answer = 'abcdefghik....'`<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬으로는 아주 간단하죠. string 상수를 이용하면 됩니다!<br>
```python
import string
num = int(input().strip())

if num == 0:
  print(string.ascii_lowercase)
elif num == 1:
  print(string.ascii_uppercase)

# 추가로 대소문자 모두, 숫자 출력하는 string 상수
string.ascii_letters
string.digits
```
string 상수를 사용하니 너무도 손쉽게 나열할 수 있습니다.<br><br>
더 많은 string 상수를 알고싶다면 [이곳](https://docs.python.org/3.4/library/string.html)을 클릭해주세요.<br><br>