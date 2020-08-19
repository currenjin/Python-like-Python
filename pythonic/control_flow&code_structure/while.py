# while문을 이용합니다. while else문과 continue, break도 사용합니다.

count = 0
while count < 5:
    print(count)
    count += 1

# break로 빠져나오기
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# continue로 넘어가기
count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

# while else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')
