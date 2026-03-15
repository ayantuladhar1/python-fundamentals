# Arrays
Note: Python does not have a built-in support fir Arrays, but Python Lists can be used instead.

Note: This page shows you how to use LISTS as ARRAYS, however to work with arrays in Python you will have to import a library, like NumPy library.
Arrays are used to store multiple values in one single variable:

## Example:
Create an array containing car names:
```python
cars = ["Ford", "Volvo", "BMW"]
print(cars)
```

## Output
```list
['Ford', 'Volvo', 'BMW']
```

## What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
```python
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
```
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
An array can hold many values under a single name, and you can access the values by referring to an index number.

## Access the Elements of an Array
You refer to an array elements by referring to the index number.

## Example:
Get the value of the first array item:
```python
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
```

## Output
Ford

## Example:
Modify the value of the first array item:
```python
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
```

## Output
```list
['Toyota', 'Volvo', 'BMW']
```

## The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

## Example:
Return the number of elements in the cars array:
```python
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
```

## Output
3

Note: The length of an array is always one more than the highest array index.

## Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

## Example:
Print each item in the cars array:
```python
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
```

## Output
Ford  
Volvo  
BMW  

## Adding Array Elements
You can use the append() method to add an element to an array.

## Example:
Add one more elemet to the cars array:
```python
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
```

## Output
```list
['Ford', 'Volvo', 'BMW', 'Honda']
```

