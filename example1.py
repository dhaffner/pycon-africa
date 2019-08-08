# Example #1: Currying with inner functions

# Given a function, f(x, y)...
def f(x, y):
    return x ** 2 + y ** 2

# ...currying constructs a new function, h(x), that takes an argument 
# from X and returns a function that maps Y to Z.
#
# f(x, y) = h(x)(y)
#
def h(x):
    def curried(y):
        return f(x, y)
    return curried


fix10 = h(10)

for y in range(10):
    print(f'fix10({y}) = {fix10(y)}')