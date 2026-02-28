# Sort List
## Sort List Alphanumerically
List objects have a sort() method that will sort the list alphabetically, ascending by default:

## Example:
Sort the list alphabetically:
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```
<img width="448" height="37" alt="image" src="https://github.com/user-attachments/assets/e70acde6-5e62-4a42-a3d2-fdb2b48fcb3d" />

## Example:
Sort the list numerically:
```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```
<img width="194" height="33" alt="image" src="https://github.com/user-attachments/assets/32710b8a-68ac-48e8-8ad8-631afa2e2eff" />

## Sort Descending
To sort descending, use the keyword argument reverse = True:

## Example:
Sort the list descending:
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```
<img width="448" height="35" alt="image" src="https://github.com/user-attachments/assets/672930c4-899d-4fae-987b-a909d7cefbb0" />

## Example:
Sor the list descending:
```python
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
```
<img width="189" height="32" alt="image" src="https://github.com/user-attachments/assets/e534663f-4911-4f3c-841a-88b098bec47c" />

## Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number firts).

## Example:
Sort the list based on how close the number is to 50.
```python
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```
<img width="192" height="35" alt="image" src="https://github.com/user-attachments/assets/4b0761df-8056-4868-96ea-d396f7e2db50" />

## Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

## Example:
Case sensitive sorting can give an unexpected result:
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```
<img width="336" height="29" alt="image" src="https://github.com/user-attachments/assets/e06dcb43-e48d-4a1c-b53b-f9c7f94c9541" />

Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:

## Example:
Perform a case-insensitive sort of the list:
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```
<img width="342" height="40" alt="image" src="https://github.com/user-attachments/assets/160c0bfc-d8f3-439d-b0c1-74b07350449a" />

## Reverse Order
What if you want to reverse the order of a  list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.

## Example:
Reverse the order of the list items:
```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 
```
<img width="338" height="36" alt="image" src="https://github.com/user-attachments/assets/18bb9ced-014c-4478-9439-ee9e25b2880d" />
