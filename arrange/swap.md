## **두 변수의 값을 바꿔보세요!**

### 변수 a와 b가 주어집니다. 두 변수의 값을 서로 바꿔보세요!<br><br>
input example:<br>
```
a = 3
b = 'abc'
```
<br>
output example:<br>

```
a = 'abc'
b = 3
```
<br><br>
**왠만하면 사람들은 값을 임시로 저장할 변수를 이용해 두 값을 바꿀거에요.<br>**
```python
a = 3
b = 'abc'

tmp = a
a = b
b = tmp
```
<br><br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 아래와 같이 두 값을 바꿔치기 할 수 있답니다! 아주 간단하게요.<br>
```python
a = 3
b = 'abc'

a, b = b, a
```
<br>
너무도 간단한 방식인 swap 이었습니다!