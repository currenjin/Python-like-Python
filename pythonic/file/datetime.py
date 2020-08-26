# datetime을 사용한다.

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(strftime('%H_%M_%S_%f'))

print(now)
d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(second=1)
print(now - d)

import time
time.sleep(1)
print(time.time())
