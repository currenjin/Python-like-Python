## **2차원 리스트를 뒤집어보자!**

### solution 함수는 mylist 인자에 2차원 리스트를 입력받고 행과 열을 뒤집어버린 값을 리턴하죠!<br><br><br>
input example:<br>
`[[1,2,3], [4,5,6], [7,8,9]]`<br><br>
output example:<br>
`[[1,4,7], [2,5,8], [3,6,9]]`<br><br><br>

**많은 분들이 2중 for문을 이용해 작성할 것 같아요. 저도 마찬가지였어요.<br>**
```python
def solution(mylist):
    answer = [[],[],[]]
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            answer[i].append(mylist[j][i])
    return answer
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
알아보니.. zip과 unpacking을 이용해 아주 간단한 코딩이 가능하더라구요.<br>
```python
def solution(mylist):
    answer = list(map(list, zip(*mylist)))
    return answer
```
<br><br>
**zip 함수**<br>
zip은 iterable(멤버를 하나씩 차례로 반환 가능한 object)의 요소들을 모으는 iterator를 만들어요.<br>
`대표적인 타입: list, str, tuple`<br><br>
example1 input:
```python
list1 = [1,2,3,4]
list2 = [10,20,30,40]
list3 = [100,200,300,400]
for i in zip(list1,list2,list3):
    print(i)
```
<br>

output:
```python
(1, 10, 100)
(2, 20, 200)
(3, 30, 300)
(4, 40, 400)
```
<br><br>
example2 input:
```python
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)
```
<br>

output:
```
{'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```
<br>

이렇게 zip함수를 이용하면 딕셔너리 또한 간단하게 만들 수 있어요!<br><br>
파이썬은 정말 알면 알수록 매력적인 언어같아요.