## **파일 입출력을 해보세요!**

### myfile.txt라는 파일을 읽는 코드를 작성해보세요! 자유롭게요.<br><br>
**아마 대부분의 사람들은 아래 처럼 EOF를 만날 때 까지 파일 읽기를 반복할거에요..<br>**
```python
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    raw = line.split()
    print(raw)
f.close()
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 `with-as`구문을 이용해 코드를 더욱 간결하게 작성할 수 있답니다.<br>
```python
with open('myfile.txt') as f:
    for line in f.readlines():
        print(line.strip().split('\t'))
```
<br>
위 처럼 파일을 close하지 않아도 돼요. while-as 블록이 종료되면 자동으로 close 되거든요.<br>
readlines 옵션으로 EOF까지만 읽기 때문에 while 문 안에서 EOF 체크를 할 필요가 없답니다.<br><br>

**그리고 `with-as`문은 파일뿐만아니라 socket, http 등에서도 활용이 가능합니다!**

