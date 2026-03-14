# Python *args and ** kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will passed into your function.
*args and **kwargs allow function to accept a unknown number of arguments.

## Arbitary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly.

## Example:
Using *args to accept any number of arguments:
```python
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
```

## Output
The youngest child is Linus


