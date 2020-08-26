# 템플릿 작성

import string

s = """\
Hi $name.

$contents

Have a good time!
"""

with open('template.txt', 'w') as f:
    f.write(s)

with open('template.txt') as f:
    t = string.Template(f.read())

# t = string.Template(s)
contents = t.substitute(name="Hyunjin", contents="How are you?")
print(contents)

#with open('test.txt')
