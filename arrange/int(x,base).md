## **{N} 진법으로 표기된 숫자를 10진법 숫자로 출력해보아요!**



input example:
`3212 5`
output example:
`432`
위 예시는 '3212' 값을 가진 5진법 숫자를 10진법으로 출력한 내용이에요.<br><br>
파이썬에 익숙하지 않다면(기능을 모르거나) 아래와 같이 코드가 나오겠어요!<br><br>
```python
num = '3212'<br>
base = 5<br>
answer = 0<br>
for idx, i in enumerate(num[::-1]):<br>
    answer += int(i) * ( base ** idx )<br>    
print(answer)
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
int(x, base = 10) 형태로 진법 변환을 지원해요!<br>
```python
num = '3212'
base = 5
answer = int(num, base)
print(answer)
```
코드가 아주 간단하면서 짧아지죠?<br><br>
output:<br>
`432`<br><br>
원하는 결과가 정상적으로 출력되네요!<br><br>
