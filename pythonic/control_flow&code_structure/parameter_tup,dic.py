# 인수의 튜플화와 사전화

# 인수가 몇 개가 들어올지 모른다면 *args를 이용해 튜플화시켜라.
def say_something(word, *args):
    print(word, args)
    for arg in args:
        print(word, arg)

say_something('Hi!', 'Mike', 'Nance')


# 인수가 몇개 들어오든 **kwargs를 이용해 사전화해라
def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, '=', v)

menu(entree='beef', drink='coffee', dessert='cake')


# 튜플과 사전형을 섞을 수 있다.(튜플이 먼저 와야함(*))
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
