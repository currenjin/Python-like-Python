## **숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 나머지를 공백으로 구분해 출력해보세요!**


input example:<br>
`5 3`<br><br>
output example:<br>
`1 2`<br><br><br>
이런 상황에서 파이썬에 익숙치가 않다면<br>
아래처럼 나머지와 몫을 따로 구할거라고 예상이 돼요.<br><br>
`print(a//b, a%b)`<br><br>
***

### **보다 파이썬답게 작성한다면?<br><br>**
div: 몫과 나머지를 한 번에 구하는 함수<br>
unpacking(*): 한 번에 묶여있던 인자들을 개별 인자로 분리<br><br><br>
**div**와 **unpacking**을 이용해 다음과 같이 작성할 수 있어요.<br>
`print( *divmmod(a,b) )`<br><br>
output:<br>
`1 2`<br><br><br>
만약 *(unpacking)을 붙이지 않는다면 결과는 아래와 같아져요.<br>
`(1, 2)`<br><br><br><br>
**!! 그렇다고 divmod를 사용하는 것이 무조건 좋은 방법은 아니에요.**<br>
> 팀의 스타일, 가독성을 고려했을 때 'a//b, a%b'를 사용하는 방법이 더 좋을 수도 있답니다.<br>
> 또, divmod는 작은 숫자를 다룰 때 'a//b, a%b'보다 느립니다.(큰 숫자를 계산할 때는 더 빠르죠)<br>