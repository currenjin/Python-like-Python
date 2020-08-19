# set method
s = {1, 2, 3, 4, 5}
print(s)

# 안됨 print(s[0])

# 추가하고 지우고
s.add(6)
print(s)
s.remove(6)
print(s)

s.clear()
print(s)

print(help(set))
