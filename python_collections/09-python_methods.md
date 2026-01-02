# What is a Method?
* A method is a function that belongs to an object(list, string, dictionary, etc.).

# Difference:
* Function: woks independently
* Method: is called using an object such as (object.method())

# String Method:
```python
	name = "python data engineer"
	print(name.upper())
	print(name.title())
	print(name.replace("python", "java"))
```
# List Methods:
```python
	fruits = ["apple", "banana", "cherry"]
	fruits.append("orange")
	fruits.remove("banana")
	fruits.sort()
	print(fruits)
```
# Dictionary Methods:
```python
	student = {
	    "name": "Ayan",
	    "age": 25,
	    "course": "Python"
	}
	print(student.keys())
	print(student.values())
	print(student.items())
```
# Method vs Function:
```python
	# Function
	numbers = [1, 2, 3]
	print(len(numbers))
	
	# Method
	numbers.append(4)
```
