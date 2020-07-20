## **제일 많이 언급된 알파벳을 출력해보아요!**

### 문자열 my_str에서 가장 많이 등장하는 알파벳을 출력해보세요! 만약 여러개라면 사전순으로요.<br><br><br>
input example 1:<br>
`'aab'`<br><br>
output example 1:<br>
`'a'`<br><br><br>
input example 2:<br>
`'dfdefdgf'`<br><br>
output example 2:<br>
`'df'`<br><br><br>
**저를 포함해 많은 분들은 아래처럼 반복문을 이용해 작성할 것이라고 예상돼요!<br>**
```python
my_str = input().strip()
answer = ''
tmp = []
for i in range(0, len(my_str)):
    tmp.append(my_str.count('%s' % my_str[i]))
max = max(tmp)
tmp = list(i for i, j in enumerate(tmp) if j == max)
for i in tmp:
    if my_str[i] not in answer:
        answer += my_str[i]
print(''.join(sorted(answer)))
```
<br><br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
알아보았더니! 파이썬에선 collections.Counter 클래스를 이용하면 아주 간단하게, 간략하게 코드를 작성할 수 있답니다.<br>
```python
import collections

my_str = input().strip()
answer = collections.Counter(my_str)

print(sorted(answer))
```
<br><br>