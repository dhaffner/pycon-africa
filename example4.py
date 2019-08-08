# Example #4: Currying with toolz.curry
from toolz import curry

names = ['Dustin', 'Erik', 'Arnold', 'Rose']

@curry
def greeting(salutation, name):
    return f'{salutation.title()}, {name}!!!'

hello = greeting('hello')
for name in names:
    print(hello(name))
