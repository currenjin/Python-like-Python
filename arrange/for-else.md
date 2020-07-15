## **제곱수를 찾아보세요!**

### 입력되는 수는 5개입니다. 숫자를 차례로 곱해 나온 수가 제곱수 1이 되면 'found'를 출력, 제곱수가 없다면 'not found'를 출력하세요.<br><br>
input example:<br>
```
2
4
2
5
1
```
<br>
output example:<br>

`found`<br><br>
수를 곱해나가면 2, 8, 16, 80, 80이 나옵니다.<br>
여기서 16은 4를 제곱해 나온 수이므로 제곱수이기 때문에 found를 출력합니다.<br><br>
**특정 기능을 모르시는 많은 분들은 아래와 같이 flag 변수 등을 이용해 문제를 풀거에요.<br>**
```python
import math

a = [int(input()) for _ in range(5)]
tot = 1
flag = True
for i in a:
    tot *= i
    if math.sqrt(tot) == int(math.sqrt(tot)):
        flag = False
        print('found')
        break
if flag:
    print('not found')
```
<br><br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 for-else 문을 이용해 코드를 더욱 짧게 쓰며 의미를 알아보기 쉽답니다!<br>
```python
import math

a = [int(input()) for _ in range(5)]
tot = 1
for i in a:
    tot *= i
    if math.sqrt(tot) == int(math.sqrt(tot)):
        print('found')
        break
else:
    print('not found')
```
<br>
다수의 프로그래밍 언어에서 else문은 if와 함께 오는 경구가 대부분이에요.<br>
하지만 파이썬에선 위 처럼 for와 같이 사용하기도 하죠.<br><br>
위 상황처럼 for 문이 중간에 break 되었는지를 판별해야 하는 경우가 있어 테스트 변수를 입력하고 처리합니다.<br>
하지만 이제 우리는 알았습니다. for-else를 이용해 간단하게 해결할 수 있다는걸<br>
