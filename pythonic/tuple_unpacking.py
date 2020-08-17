# tuple unpacking
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
# x, y = (10, 20)
# x, y = 10, 20
print(x, y)

# 서로의 값을 변경
x, y = y, x
print(x, y)
