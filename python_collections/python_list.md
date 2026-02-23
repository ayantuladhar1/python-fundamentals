# Lists are used to store multiple items in a single variable.  

```python
thislist = ["apple", "banana", "cherry"]  
```

List items are ordered, changeable, and allow duplicate values.  
List items are indexed, the first item has index [0], the second item has index [1] etc.  
  
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.  
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.  
  
# Lists allow duplicate values
```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```
<img width="519" height="36" alt="image" src="https://github.com/user-attachments/assets/858299c5-47c1-4911-a785-eb21c440b544" />

# To determine how many items a list has, use the len() function
* Print the number of items in the list:  
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
<img width="24" height="21" alt="image" src="https://github.com/user-attachments/assets/d88eb2be-d41d-4543-91c3-63a898729d02" />

# List Items - Data Types  
* List items can be of any data type:  
* String, int and boolean data types:  
```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

* A list can contain different data types:  
* A list with strings, integers and boolean values:  
```python
list1 = ["abc", 34, True, 40, "male"]
```

# Using the list() constructor to make a List
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```
<img width="317" height="28" alt="image" src="https://github.com/user-attachments/assets/9d06868d-9c8d-4854-8aaf-69229f23a118" />

# Access Items  
* List items are indexed and you can access them by referring to the index number:  
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
<img width="81" height="26" alt="image" src="https://github.com/user-attachments/assets/2a8c496c-e679-4802-937a-c7fbc244428b" />

# Negative Indexing  
* Negative indexing means start from the end  
* -1 refers to the last item, -2 refers to the second last item etc.  
* Print the last item of the list:  
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
<img width="65" height="30" alt="image" src="https://github.com/user-attachments/assets/5285f170-ada3-4311-845f-d942c5844bee" />

* Return the third, fourth, and fifth item:  
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
<img width="303" height="37" alt="image" src="https://github.com/user-attachments/assets/6bdb9550-817f-4f2c-953c-c14902e5e0cf" />

* This example returns the items from the beginning to, but NOT including, "kiwi":  
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```
<img width="430" height="35" alt="image" src="https://github.com/user-attachments/assets/86830d60-834f-4142-8797-06121228a843" />

* This example returns the items from "cherry" to the end:
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```
<img width="487" height="35" alt="image" src="https://github.com/user-attachments/assets/4ebbe9ff-ed26-46da-8e77-be322a6cc88c" />

* Change the second item:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
<img width="384" height="33" alt="image" src="https://github.com/user-attachments/assets/58d4dbf6-fa89-4220-8641-f48c741f9b06" />

# Append Items
* To add an item to the end of the list, use the append() method:
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```
<img width="419" height="41" alt="image" src="https://github.com/user-attachments/assets/871ed689-1ff3-4bbd-80d3-2e5ebdd37890" />

# To insert a list item at a specified index, use the insert() method
* The insert() method inserts an item at the specified index:
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```
<img width="417" height="41" alt="image" src="https://github.com/user-attachments/assets/34f97460-7047-4001-abc8-309f0871e3e0" />

# Remove Specified Item
* The remove() method removes the specified item.
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```
<img width="202" height="41" alt="image" src="https://github.com/user-attachments/assets/89ca2cfe-ba28-4328-bfb8-c0e1b90d66b0" />

* If there are more than one item with the specified value, the remove() method removes the first occurance:  
* Remove the first occurance of "banana":
```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```
<img width="399" height="38" alt="image" src="https://github.com/user-attachments/assets/0ed152e4-ebdd-4858-989f-ce5d605706b8" />

# Remove Specified Index
* The pop() method removes the specified index.
* Remove the second item:
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```
<img width="227" height="34" alt="image" src="https://github.com/user-attachments/assets/6c7ed5c1-ad85-49af-847b-956dcc5e118a" />

* If you do not specify the index, the pop() method removes the last item.
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```
<img width="209" height="44" alt="image" src="https://github.com/user-attachments/assets/23640d27-111f-46b5-8257-b9ccccac7c4e" />

# The del keyword also removes the specified index:
* Remove the first item:
```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```

# Delete the entire list
```python
thislist = ["apple", "banana", "cherry"]
del thislist
```
<img width="233" height="35" alt="image" src="https://github.com/user-attachments/assets/4b5b2e56-44ea-4f7f-a09d-c0e2c179def3" />

# Clear the List
* The clear() method empties the list.
* The list still remains, but it has no content.
```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```
<img width="42" height="28" alt="image" src="https://github.com/user-attachments/assets/5160cce5-2714-4d88-a20e-e7482ae1734c" />

# You can loop through the list items by using a for loop
* Print all items in the list, one by one:
```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```
<img width="81" height="75" alt="image" src="https://github.com/user-attachments/assets/9500165f-bd93-4a24-875a-48907118595f" />

* Print all items by referring to their index number:
```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```
<img width="74" height="70" alt="image" src="https://github.com/user-attachments/assets/301bbc4d-5550-4de5-83c7-f3c0e277aa50" />

* Print all items, using a while loop to go through all the index numbers
```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```
<img width="76" height="71" alt="image" src="https://github.com/user-attachments/assets/58ca2908-9dfb-44c0-a028-78c9ff18dd48" />

# List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
```
<img width="309" height="143" alt="image" src="https://github.com/user-attachments/assets/07e743e0-63b9-447e-a0e0-8b6d6d0026ad" />

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```
<img width="301" height="31" alt="image" src="https://github.com/user-attachments/assets/366ce8ef-e985-48a7-b6a3-d985bcd054ac" />

# Python - Sort Lists
* Sort the list alphabetically:
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```
<img width="531" height="40" alt="image" src="https://github.com/user-attachments/assets/92ab7424-9ad9-44ab-828c-18a8789adad2" />

* Sort Descending
To sort descending, use the keyword argument reverse = True
```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```
<img width="538" height="34" alt="image" src="https://github.com/user-attachments/assets/82a1cbc1-26be-4ce9-87c1-3a073eb2532f" />
