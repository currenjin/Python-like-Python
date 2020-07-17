## **이진 탐색을 해보세요!**

<br>**이진 탐색이란?**<br>
데이터가 정렬된 배열에서 특정 값을 찾아내는 알고리즘을 이야기해요.<br><br>
배열 중간 임의의 값을 지정해 찾고자하는 X와 비교합니다.<br> 이때, X가 중간값보다 작으면 중간값을 기준으로 좌측 데이터를 대상으로, <br>
X가 중간값보다 크면 우측 데이터를 대상으로 재탐색을하고 X값을 찾을 때 까지 이 행위를 반복하죠!<br><br><br>
### 정수 여러개가 들어있는 mylist를 입력받고 이진 탐색을 이용해 x를 찾아보세요!<br><br>
input example:
```python
mylist = [1, 2, 3, 7, 9, 11, 33]
x = 3

bisect(mylist, 3)
```
output example:
```
3
```
<br><br>
**다른언어나 특정 기능을 모르시는 분들은 아마 아래와 같이 직접 작성할 것 같아요.<br>**
```python
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))
```
<br>

***

### **보다 파이썬답게 작성한다면?<br><br>**
파이썬에서는 bisect.bisect 메소드를 이용해 아래와 같이 코드를 작성할 수 있어요.<br>
```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```
<br>
알고리즘 문제에서 검색속도가 아주 빠른 이진 탐색을 이렇게도 쉽게 구현할 수 있습니다!