# 문자열의 format을 사용해봅니다.
print('a is {}'.format('a'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {0} {1}'.format('Jeong', 'Hyunjin'))
print('My name is {0} {1}. My Family name is {0} '.format('Jeong', 'Hyunjin'))
print('My name is {family} {name}. My Family name is {family} '.format(family='Jeong', name='Hyunjin'))


# Python 3.6부터는 format대신 f-string이 사용가능합니다. 활용도와 처리속도가 높아 좋습니다!
family = 'Jeong'
name = 'Hyunjin'
print(f'My name is {family} {name}. My Family name is {family}')
