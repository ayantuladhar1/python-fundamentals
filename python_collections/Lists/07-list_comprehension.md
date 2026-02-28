# List Comprehension
List comprehension offers a shorter syntac when you want to create a new list based on the value of an existing list.

## Example:
Based on a list of fruits, you want a new list, containing only the fruits wuith the letter 'a' in the name.
Without list comprehension you will have to write a for statement with a conditional test inside.

## Example:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
  newlist.append(x)
print(newlist)
```
<img width="261" height="37" alt="image" src="https://github.com/user-attachments/assets/c8c3d059-6aae-423b-9522-7bc184e9b8bc" />

With list comprehension you can do all that with only one line of code

## Example:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```
<img width="259" height="37" alt="image" src="https://github.com/user-attachments/assets/4d387d90-6e60-4522-9c59-e12efbecb139" />

## The Syntax
```python
newlist = [expression for item in iterable if condition == True]
```
The return value is a new list, leaving the old list unchanged.

## Condition
The condition is like a filter that only accepts the item that evaluates to True.

## Example:
Only accept items that are not 'apple':
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
```
<img width="332" height="34" alt="image" src="https://github.com/user-attachments/assets/ed4ffdef-9320-427c-80f3-916b8eef6449" />

The condition if x != "apple" will return True for all elements other than "apple", making the new list contains all fruits except "apple".
The condition is optional and can be omitted:

## Example
With no if statement
```python
newlist = [x for x in fruits]
```
<img width="404" height="38" alt="image" src="https://github.com/user-attachments/assets/5a0c8b7e-218e-482e-8ef0-04ffa5d762b8" />

## Iterable
The iterable can bo any iterable object, like a list, tuple, set, etc.

## Example:
You can use the range() function to create an iterable:
```python
newlist = [x for x in range(10)]
```
<img width="277" height="31" alt="image" src="https://github.com/user-attachments/assets/84fd587b-fc4f-4a98-90f5-6b42363993a4" />

Same example but with a condition:

## Example:
Accept only number lower than 5:
```python
newlist = [x for x in range(10) if x < 5]
```
<img width="141" height="38" alt="image" src="https://github.com/user-attachments/assets/aed52a00-65be-4d1e-bfa6-1fe338f2f497" />

## Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

## Example:
Set the values in the new list to upper caseL
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
```
<img width="416" height="47" alt="image" src="https://github.com/user-attachments/assets/d170efb1-f3ac-4bb4-af1d-4e0d6067a234" />

You can set the outcome to whatever you like:

## Example:
Set all values in the new list to 'hello':
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
```
<img width="404" height="34" alt="image" src="https://github.com/user-attachments/assets/8728e062-378a-4341-bf47-db1eb78e470c" />

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

## Example:
Return 'orange' instead of 'banana':
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
```
<img width="414" height="34" alt="image" src="https://github.com/user-attachments/assets/4ddf4d6f-cfdb-43d3-b666-382a38fe2bcc" />
