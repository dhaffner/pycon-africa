from __transformers__ import ellipsis_partial  

# Curry a function call
f = map(lambda x: x ** 2, ...)
printer = print(...)

# Curry an operator!
h = 1 + ...

# Curry a keyword argument
formatter = "Pycon Africa 2019, {name}!".format(name=...)

lst = list(range(1000))
sort_lst_with_key = sorted(lst, key=...)

# Curry a list comprehension
get_elements_less_than = [x for x in lst if x < ...]
print(get_elements_less_than(20))
