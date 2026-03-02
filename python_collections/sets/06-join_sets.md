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

## Intersection
Keep ONLY the duplicates
The interaction() method will return a new set, that only contains the items that are present in both sets.

## Example:
Join Set 1 and Set 2 but keep only the duplicates:
```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
```
<img width="99" height="37" alt="image" src="https://github.com/user-attachments/assets/2ef38b50-e6a7-4eba-9180-0e3677d76b19" />

You can use the & operator insetad of the intersection() method, and you will get the same result.

## Example:
Use & to join two sets:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
```
<img width="94" height="34" alt="image" src="https://github.com/user-attachments/assets/85549a08-8125-411b-afbc-8060bb2dbc07" />

Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

## Example:
Keep the items that exists in both set 1 and set 2:
```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
```
<img width="98" height="40" alt="image" src="https://github.com/user-attachments/assets/da569f0d-7db8-4995-81f0-f844803ac070" />

The value True and 1 are considered the same value. The same goes for False and 0.

## Example:
Join sets that contains the values True, False, 1 and 0 and see what is considered as duplicates:
```python
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}
set3 = set1.intersection(set2)
print(set3)
```
<img width="231" height="44" alt="image" src="https://github.com/user-attachments/assets/239781f9-116f-4a96-b1e3-1d6409c403bf" />

## Difference
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

## Example:
Keep all items from set 1 that are not in set 2:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
```
<img width="209" height="43" alt="image" src="https://github.com/user-attachments/assets/cfb8cf0a-9b15-4f62-ace6-08c1dae3c8fc" />

You can use the - operator insted of difference() method and you will get the same result.

## Exanple:
Use - to join two sets:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
```
<img width="213" height="48" alt="image" src="https://github.com/user-attachments/assets/27c0cad4-e493-404e-9bf7-337fab6aabcf" />

Note: The - operator only allows you to join sets with sets and not with other data types like you can with the difference() method.

The difference_update() method will keep the items from the first set that are not in the other set, but will change the original set instead of returning a new set.

## Example:
Use the difference_update() method to keep only the items from the first set that are not present in the other set:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
```
<img width="212" height="45" alt="image" src="https://github.com/user-attachments/assets/c8d33ff3-c0a9-40a8-ba03-4a4a0074a867" />

## Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

## Example:
Keep the items that are not present in both sets:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
```
<img width="441" height="34" alt="image" src="https://github.com/user-attachments/assets/77030a82-f7c9-40af-90ea-8cd24db0b61c" />

You can use the ^ operator instead of the symmetric_difference() method and you will get the same result.

## Example:
Use ^ to join two sets:
```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
```
<img width="444" height="50" alt="image" src="https://github.com/user-attachments/assets/91d638dc-6338-4fb8-9d43-b520ba77ff06" />

Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with symmetric_difference() method.

The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

## Example:
Use the symmetric_difference_update() method to keep the items that are not present in both sets:
```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
```
<img width="444" height="50" alt="image" src="https://github.com/user-attachments/assets/1e296f5a-c8be-42bf-ad12-b9a708d2323b" />
