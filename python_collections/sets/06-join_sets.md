# Join Sets
There are several ways to join two or more sets in Python.
* The union() and update() methods joins all items from both sets.
* The intersection() method keeps ONLY the duplicates.
* The difference() method keeps the items from the first set that are not in the other sets.
* The symetric_difference() method keeps all items EXCEPT the duplicates.

## Union
The union() method returns a new set with all items from both sets.

## Example:
Join set1 and set2 into a new set:
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
```
<img width="228" height="42" alt="image" src="https://github.com/user-attachments/assets/7c3216c4-0e7c-45cd-a09e-bc6aeb1f5ab5" />

You can use the | operator instead of the union() method, and you will get the same result.

## Example:
Use | to join two sets:
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
```
<img width="258" height="41" alt="image" src="https://github.com/user-attachments/assets/74e0f7b3-1091-433c-bf8e-5575414e7d87" />

## Join Multiple Sets
All the joining methods and operators can be used to join multiple sets.
WHen using a method, just add more sets in the parantheses, separated by commas:

## Example:
Join multiple sets with the union() method:
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
```

<img width="618" height="37" alt="image" src="https://github.com/user-attachments/assets/0ca2c5ca-9783-4b86-8dd4-122810e465c1" />

When using the | operator, separate the sets with more | operators:

## Example:
Use | to join two sets:
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)
```
<img width="610" height="38" alt="image" src="https://github.com/user-attachments/assets/f06bad9c-6036-40e0-815a-009dd4efe9ae" />

## Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.

## Example:
Join a set with a tuple:
```python
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
```
<img width="254" height="31" alt="image" src="https://github.com/user-attachments/assets/76c75f84-f28c-4e8a-9be5-f3f9aaef874b" />

Note The | operator only allows you to join sets with sets and not other data types like you can with the union() method.

## Update
The update() method inserts the items in set 2 into set 1:
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
```
<img width="242" height="38" alt="image" src="https://github.com/user-attachments/assets/3262e0e9-3074-4c04-a9be-f43e83c77a00" />

Both union() and update() will exlude any duplicate items.
