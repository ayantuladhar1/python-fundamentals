# Change Item Value
To change the value of a specific item, refer to the index number.

## Example:
Change the second item:
```python
thislist = ["apple", "banana", "cherry']
thislist[1] = "blackcurrant"
print(thislist)
```
<img width="319" height="40" alt="image" src="https://github.com/user-attachments/assets/1125bb43-fd87-4276-9cb7-5c2021b62eb0" />

## Change a Range of Items Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.

## Example:
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```
<img width="599" height="55" alt="image" src="https://github.com/user-attachments/assets/742dfd3d-40c0-4a81-876c-d3b772e062a9" />

If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.

## Example:
Change the second value by replacing it with two new values:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```
<img width="440" height="38" alt="image" src="https://github.com/user-attachments/assets/1b59ebcb-90e0-4ab8-832b-a71ef8dfdb41" />

Note: The length of the list will change when the number of items inserted deos not match the number of items replaced.
If you insert less items than you replace, the new items will be inserted where you specified and the remaining items will move accordingly"

## Example:
Change the second and third value by replacing it with one value:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```
<img width="216" height="34" alt="image" src="https://github.com/user-attachments/assets/f622972f-1306-43f2-99b3-f652600b3169" />

## Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts as item ast the specified index:

## Example:
Insert "watermelon" as the third item:
```python
thislist = ["apple", "banana", "cherry']
thislist.insert(2, "watermelon")
print(thislist)
```
<img width="387" height="30" alt="image" src="https://github.com/user-attachments/assets/c4a4abf4-0e3f-4a35-962b-e4aa949d1ade" />

Note: As a result of the example above, the list will now contain 4 items.
