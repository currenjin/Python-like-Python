## **리스트의 순열을 사전순으로!**

### 숫자를 담은 1차원 리스트 mylist가 있어요. 원소로 이루어진 모든 순열을 사전순으로 리턴하는 solution 함수를 만드세요!<br><br>
input example 1:<br>
`[2, 1]`<br><br>
output example 1:<br>
`[[1, 2], [2, 1]]`
<br><br><br>
input example 2:<br>
`[1, 2, 3]`<br><br>
output example 2:<br>
`[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`
<br><br>

**아마 해당 기능을 모르신다면 for문을 이용해 리스트를 만들어 갈 것이라 예상돼요!<br>**
```python
def solution(mylist):
    result = [mylist[:]]
    c = [0] * len(mylist)
    i = 0
    while i < len(mylist):
        if c[i] < i:
            if i % 2 == 0:
                mylist[0], mylist[i] = mylist[i], mylist[0]
            else:
                mylist[c[i]], mylist[i] = mylist[i], mylist[c[i]]
            result.append(mylist[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬의 itertools에는 permutations라는 함수가 있어요!<br>
```python
import itertools
def solution(mylist):
    mylist.sort()
    return list(map(list, itertools.permutations(mylist)))
```
<br>
아주 간단하게 구현이 되는군요!<br>
정말 우리가 생각하는 것 이상의 기능을 가진 함수들이 많은 것 같아요.<br>