# Example #2: Currying with lambdas

names = ['Dustin', 'Erik', 'Arnold', 'Rose']

def greeting(salutation, name):
    return f'{salutation.title()}, {name}!!!'

hello = lambda name: greeting('hello', name)
for name in names:
    print(hello(name))
