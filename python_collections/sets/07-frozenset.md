# Frozenset
Frozenset is an immutable version of a set.
Like sets, it contains unique, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.

## Creating a frozenset
Use the frozenset() constructor to create a frozenset from any iterable.

## Example:
Create a frozenset and check its type:
```python
x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)
#display the data type of x:
print(type(x)) 
```
<img width="412" height="62" alt="image" src="https://github.com/user-attachments/assets/50ca7111-63cb-4dc5-bb55-be8da47bae4b" />

## Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non mutating operations of sets.

|Method| Shotcut| Description|
|------|--------|------------|
|copy()|        |Retruns a shallow copy|
|difference()| - | Returns a new frozenset with the difference|
|intersection()| & | Returns a new frozenset with the intersection|
|isdisjoint()|    | Returns whether two frozensets have have an intersection|
|issubset()| <= / < | Returns True if this frozenset is a (proper) subset of another|
|issuperset()| >= / > | Returns True if this frozenset is a (proper) superset of another|
|symmetric_difference()| ^ | Returns a new frozenset with the symmetric differences|
|union() | | | Retuns a new frozenset containing the union|
