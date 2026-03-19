# Python String Formatting
F-String was introduced in Python 3.6, and is now the preferred way if formatting strings.
Before Python3.6 we had to use the format() method.

## F-Strings
F-String allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:

## Example:
Create an f-string:
```python
txt = f"The price is 49 dollars"
print(txt)
```
<img width="211" height="33" alt="image" src="https://github.com/user-attachments/assets/dcb0c48c-8f5e-4142-851d-8944c74a8190" />

## Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

## Example:
Add a placeholder for the price variable:
```python
price = 59
txt = f"The price is {price} dollars"
print(txt)
```
<img width="213" height="33" alt="image" src="https://github.com/user-attachments/assets/45ee33e0-3d7a-476c-abcc-b7206adfc1f9" />

A placeholder can also include a modifier to format the value.
A modifier is included by adding a colon : followed by legal formatting type, like .2f which means fixed point with 2 decimals:

## Example:
Display the price with 2 decimals:
```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```
<img width="231" height="31" alt="image" src="https://github.com/user-attachments/assets/fe21ed72-09dd-4ae3-9c06-5ead510422e7" />

You can also format a value directly without keeping it in a variable:

## Example:
Display the value 95 with 2 decimals:
```python
txt = f"The price is {95:.2f} dollars"
print(txt)
```
<img width="242" height="38" alt="image" src="https://github.com/user-attachments/assets/9ee7cb51-a62a-4a19-b558-411e1ae40ef1" />

## Perform Operations in F-Strings
You can perform Python operations inside the placeholders.
You can do math operations:

## Example:
Add taxes before displaying the price:
```python
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
```
<img width="246" height="37" alt="image" src="https://github.com/user-attachments/assets/e359217f-1649-440f-add8-ed3d6fae646e" />

You can perform if...else statements inside the placeholders:

## Example:
Return "Expensive" if the price is over 50, otherwise return "Cheap":
```python
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)
```
<img width="144" height="30" alt="image" src="https://github.com/user-attachments/assets/850afde1-9efd-4cd4-8b31-18331639c427" />

## Execute Functions in F-Strings
You can execute functions inside the placeholder:

## Example:
Use the string method upper() to convert a value into upper case letters:
```python
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)
```
<img width="122" height="32" alt="image" src="https://github.com/user-attachments/assets/3cbbd8b3-dd2e-44b3-abea-a9acdc21a694" />

The function does not have to be a built-in Python method, you can create your own functions and use them:

## Example:
Create a function that converts feet into meters:
```python
def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
```
<img width="423" height="31" alt="image" src="https://github.com/user-attachments/assets/ceb6aa59-0bf2-44e1-8adb-f7859ea1811f" />

## More Modifiers
At the beginning of this chapter we explained how to use the .2f modifier to format a number into fixed point number with 2 decimals.
There are several other modifiers that can be used to format values:

## Example:
Use a comma as a thousand separator:
```python
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
```
<img width="250" height="29" alt="image" src="https://github.com/user-attachments/assets/285f8a6b-0bad-495a-9761-f23e496e10bd" />

Here is a list of all the formatting types.
|Formatting Types|
|----------------|
|:<	Left aligns the result (within the available space)|
|:>	Right aligns the result (within the available space)|
|:^	Center aligns the result (within the available space)|
|:=	Places the sign to the left most position|
|:+	Use a plus sign to indicate if the result is positive or negative|
|:-	Use a minus sign for negative values only|
|: 	Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)|
|:,	Use a comma as a thousand separator|
|:_	Use a underscore as a thousand separator|
|:b	Binary format|
|:c	Converts the value into the corresponding Unicode character|
|:d	Decimal format|
|:e	Scientific format, with a lower case e|
|:E	Scientific format, with an upper case E|
|:f	Fix point number format|
|:F	Fix point number format, in uppercase format (show inf and nan as INF and NAN)|
|:g	General format|
|:G	General format (using a upper case E for scientific notations)|
|:o	Octal format|
|:x	Hex format, lower case|
|:X	Hex format, upper case|
|:n	Number format|
|:%	Percentage format|

## Example:
:<	Left aligns the result (within the available space
```python
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = f"We have {49:<8} chickens."
print(txt)
```
<img width="237" height="25" alt="image" src="https://github.com/user-attachments/assets/e13b543e-7bc9-4016-a892-7a033264cedb" />

:>	Right aligns the result (within the available space)
```python
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = f"We have {49:>8} chickens."
print(txt)
```
<img width="236" height="32" alt="image" src="https://github.com/user-attachments/assets/f473a97f-fbf7-4409-935d-1769a760d52c" />

:^	Center aligns the result (within the available space)
```python
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = f"We have {49:^8} chickens."
print(txt)
```
<img width="239" height="29" alt="image" src="https://github.com/user-attachments/assets/8f638df3-2050-405a-9fce-d7edb982a987" />

:=	Places the sign to the left most position
```python
#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = f"The temperature is {-5:=8} degrees celsius."
print(txt)
```
<img width="323" height="30" alt="image" src="https://github.com/user-attachments/assets/def13393-ae3c-426d-bef3-ae350eb0d8be" />

:+	Use a plus sign to indicate if the result is positive or negative
```python
#Use "+" to always indicate if the number is positive or negative:
txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."
print(txt)
```
<img width="472" height="37" alt="image" src="https://github.com/user-attachments/assets/82298062-ed15-4ec6-897e-482b620e5064" />

:- Use a minus sign for negative values only
```python
#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = f"The temperature is between {-3:-} and {7:-} degrees celsius."
print(txt)
```
<img width="462" height="42" alt="image" src="https://github.com/user-attachments/assets/c581e986-f074-4f1e-b2fc-2a9bc839c2eb" />

: Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
```python
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = f"The temperature is between {-3: } and {7: } degrees celsius."
print(txt)
```
<img width="474" height="32" alt="image" src="https://github.com/user-attachments/assets/0d379ce1-aa40-44f5-997f-514e384c0802" />

:, Use a comma as a thousand separator
```python
#Use "," to add a comma as a thousand separator:
txt = f"The universe is {13800000000:,} years old."
print(txt)
```
<img width="370" height="31" alt="image" src="https://github.com/user-attachments/assets/27be53b3-404d-4566-914f-1b5a9dece703" />

:_ Use a underscore as a thousand separator
```python
#Use "_" to add a underscore character as a thousand separator:
txt = f"The universe is {13800000000:_} years old."
print(txt)
```
<img width="369" height="28" alt="image" src="https://github.com/user-attachments/assets/4433d394-7ea0-43fe-9597-a191cd691b7e" />

:b Binary format
```python
#Use "b" to convert the number into binary format:
txt = f"The binary version of 5 is {5:b}"
print(txt)
```
<img width="275" height="28" alt="image" src="https://github.com/user-attachments/assets/00e81369-4ff9-4e82-b829-dd1493849e75" />

:d Decimal format
```python
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = f"We have {0b101:d} chickens."
print(txt)
```
<img width="177" height="32" alt="image" src="https://github.com/user-attachments/assets/d49bda87-b5cd-481d-9dc4-7abec765c412" />

:e Scientific format, with a lower case e
```python
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = f"We have {5:e} chickens."
print(txt)
```
<img width="268" height="35" alt="image" src="https://github.com/user-attachments/assets/3fe3e9fa-957f-4cca-b208-02c19976def3" />

:E Scientific format, with an upper case E
```python
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = f"We have {5:E} chickens."
print(txt)
```
<img width="191" height="27" alt="image" src="https://github.com/user-attachments/assets/221b25f8-10bc-44f2-9c8f-2f6d5c3031dc" />

:f Fix point number format
```python
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = f"The price is {45:.2f} dollars."
print(txt)
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = f"The price is {45:f} dollars."
print(txt)
```
<img width="276" height="51" alt="image" src="https://github.com/user-attachments/assets/cb89eae6-b38a-45bb-9787-d172078672c6" />

:F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
```python
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = f"The price is {x:F} dollars."
print(txt)
#same example, but with a lower case f:
txt = f"The price is {x:f} dollars."
print(txt)
```
<img width="229" height="45" alt="image" src="https://github.com/user-attachments/assets/caa5fd65-9663-4cf0-958e-6f442a89d9ca" />

:o Octal format
```python
#Use "o" to convert the number into octal format:
txt = f"The octal version of 10 is {10:o}"
print(txt)
```
<img width="266" height="26" alt="image" src="https://github.com/user-attachments/assets/ebfb2b5e-b924-4dea-9395-b98bc2c62aff" />

:x Hex format, lower case
```python
#Use "x" to convert the number into Hex format:
txt = f"The Hexadecimal version of 255 is {255:x}"
print(txt)
```
<img width="321" height="30" alt="image" src="https://github.com/user-attachments/assets/26f0a417-9c5c-4ae0-9a6f-02abdd5e1cbe" />

:X Hex format, upper case
```python
#Use "X" to convert the number into upper-case Hex format:
txt = f"The Hexadecimal version of 255 is {255:X}"
print(txt)
```
<img width="321" height="28" alt="image" src="https://github.com/user-attachments/assets/b541e27e-9e39-4f73-9da3-6e5e75cd5d1a" />

:% Percentage format
```python
#Use "%" to convert the number into a percentage format:
txt = f"You scored {0.25:%}"
print(txt)
#Or, without any decimals:
txt = f"You scored {0.25:.0%}"
print(txt)
```
<img width="195" height="54" alt="image" src="https://github.com/user-attachments/assets/41303320-8d78-4c6d-a0bb-f4df0cf918ef" />

## String format()
Before Python 3.6 we used the format() method to format strings.
The format() method can still be used, but f-strings are faster and the preferred way to format strings.
The next examples in this page demostrates how to format strings with the format() method.
The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

## Example:
Add a placeholder where you want to display the price:
```python
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
```
<img width="210" height="21" alt="image" src="https://github.com/user-attachments/assets/4ed76d77-774d-446e-92e3-1b344196b140" />

You can add parameters inside the curly brackets to specify how to convert the value:

## Example:
Format the price to be displayed as a number with two decimals:
```python
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
```
<img width="237" height="27" alt="image" src="https://github.com/user-attachments/assets/f18c6b32-9635-4f39-82a0-6392ed8928de" />

## Multiple Values
If you want to use more values, just add more values to the format() method:
```python
print(txt.format(price, itemno, count))
```

And add more placeholders:

## Example:
```python
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```
<img width="475" height="31" alt="image" src="https://github.com/user-attachments/assets/a52d7a5f-16cc-4dd5-9db2-578d8c95dbe2" />

## Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed placeholders:

## Example:
```python
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```
<img width="470" height="31" alt="image" src="https://github.com/user-attachments/assets/0bd65795-323b-4273-a0d2-7987aa560f6f" />

Also, if you want to refer to the same value more than once, use the index number:

## Example:
```python
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
```
<img width="352" height="27" alt="image" src="https://github.com/user-attachments/assets/662cd9e5-1880-4a8e-ad05-8adb6c2b9176" />

Also, if you want to refer to the same value more than once, use the index number:

## Example:
```python
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
```
<img width="352" height="35" alt="image" src="https://github.com/user-attachments/assets/f6663a04-34b4-460c-a6fc-0e32b3fd5161" />

## Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

## Example:
```python
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
```
<img width="280" height="27" alt="image" src="https://github.com/user-attachments/assets/2439be1d-07ee-4f40-bb59-ac22864209c7" />
