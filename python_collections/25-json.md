# Python JSON
JSON is a syntax for storing and exchanging data.
JSON is text, written with javaScript object notation.

## JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.

## Example:
Import the json module:
```python
import json
```

## Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it buusing the json.loads() method.
The result will be a Python dictionary.

## Example:
Convert from JSON to Python:
```python
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
```
<img width="32" height="23" alt="image" src="https://github.com/user-attachments/assets/cb538088-a47a-42ee-a9d3-7f684fb76604" />

## Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

## Example:
Convert from Python to JSON:
```python
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
```
<img width="416" height="30" alt="image" src="https://github.com/user-attachments/assets/a77c0ce9-722c-4e7a-b7d4-e4ab7e1828da" />

You can convert Python objects of the following types, into JSON strings:
* dict
* list
* tuple
* string
* int
* float
* True
* False
* None

## Example:
Convert Python objects into JSON strings, and print the values:
```python
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```
<img width="252" height="230" alt="image" src="https://github.com/user-attachments/assets/75919bd7-5b57-40d3-bd48-49adc40e054f" />

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
|Python| JSON|
|------|-----|
|dict|	Object|
|list|	Array|
|tuple|	Array|
|str|	String|
|int|	Number|
|float|	Number|
|True|	true|
|False|	false|
|None|	null|

## Example:
Convert a Python object containing all the legal data types:
```python
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
```
```dictionary
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
```

## Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() methods has parameters to make it easier to read the result:

## Example:
Use the indent parameter to define the number of indents:
```python
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
```
<img width="308" height="507" alt="image" src="https://github.com/user-attachments/assets/4c85d52f-a9aa-464b-aa6b-abfa5225d335" />

You can also define the separators, default value is (",",":") which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

## Example:
Use the separators parameter to change the default separator:
```python
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
```
<img width="311" height="512" alt="image" src="https://github.com/user-attachments/assets/2975d41f-d190-4ba3-b51d-03fad3682306" />

## Order the Result
The json.dumps() method has parameters to order the keys in the result:

## Example:
Use the sort_keys parameter to specify if the result should be sorted out or not:
```python
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
```
<img width="302" height="511" alt="image" src="https://github.com/user-attachments/assets/c49d6b5d-f159-41c6-8f8e-6f541ee36b4d" />
