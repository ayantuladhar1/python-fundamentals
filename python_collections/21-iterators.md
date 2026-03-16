# Python Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next()__.

## Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator.

## Example:
Return an iterator from a tuple, and print each value:
```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
```

## Output
apple  
banana  
cherry  

Even strings are iterable objects, and can return an iterator:

## Example:
Strings are also iterable objects, containing a sequence of characters:
```python
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
```

## Output
b  
a  
n  
a  
n  
a  

## Looping Through an Iterator
We can also use a for loop to iterate through an iterable object:

## Example:
Iterate the values of a tuple:
```python
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
```

## Output
apple  
banana  
cherry  

## Example:
Iterate the character of a string:
```python
mystr = "banana"

for x in mystr:
  print(x)
```

## Output
b  
a  
n  
a  
n  
a  

The for loop actually creates an iterator object and executes the next() method for each loop.
