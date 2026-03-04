# Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

## Example:
Create a dictionary that contain three dictionaries:
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
```
<img width="1307" height="40" alt="image" src="https://github.com/user-attachments/assets/54603855-c0ae-42cd-aa75-1120e63e89f2" />

Or, if you want to add three dictionaries into a new dictionary:

## Example:
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
```python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```
<img width="1312" height="36" alt="image" src="https://github.com/user-attachments/assets/e8da247d-9aaa-443f-9817-93cf792b0940" />

## Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

## Example:
Print the name of child 2:
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
```
<img width="70" height="28" alt="image" src="https://github.com/user-attachments/assets/bf60e4c8-1db1-40d9-bc56-ad165d6653a8" />

## Loop Through Nested Dictionaries
You can loop through a dictionary by using the items() method like this:

## Example:
Loop through the keys and values of all nested dictionaries:
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
```
<img width="133" height="211" alt="image" src="https://github.com/user-attachments/assets/69da5f75-c871-44c3-9af4-896e098f5e8f" />
