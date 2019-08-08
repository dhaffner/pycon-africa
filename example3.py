# Example #4: Currying with functools.partial
from functools import partial

names = ['Dustin', 'Erik', 'Arnold', 'Rose']

def greeting(salutation, name):
    return f'{salutation.title()}, {name}!!!'

hello = partial(greeting, 'hello')
for name in names:
    print(hello(name))
