## **2차원 리스트를 1차원 리스트로 바꿔보자!**

### 문자열을 담은 2차원 리스트, mylist가 있습니다. solution 함수가 mylist를 1차원 리스트로 만들도록 리턴하세요!<br><br>
input example1:<br>
`[[1], [2]]`<br><br>
output example:<br>
`[1, 2]`
<br><br><br>
input example2:<br>
`[['A', 'B'], ['X', 'Y'], ['1']]`<br><br>
output example:<br>
`['A', 'B', 'X' ,'Y', '1']`
<br><br>

**아마 해당 기능을 모르신다면 for문을 이용해 리스트를 더해가겠죠?<br>**
```python
def solution(mylist):
    answer = []
    for i in mylist:
        answer += i
    return answer
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬엔 다양한 방법이 있어요!<br>
```python
def solution(mylist):

# example 1) SUM
    answer = sum(mylist, [])
    return answer

# example 2) itertools.chain
import itertools
    return list(itertools.chain.from_iterable(mylist))

# example 3) itertools, unpacking
import itertools
    return list(itertools.chain(*mylist))

# example 4) reduce_1
from functools import reduce
import operator
    return list(reduce(operator.add, mylist))

# example 5) reduce_2
from functools import reduce
    return list(reduce(lambda x, y: x+y, mylist))

```
<br><br>