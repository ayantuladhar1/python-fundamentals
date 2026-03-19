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
|:+		Use a plus sign to indicate if the result is positive or negative|
|:-		Use a minus sign for negative values only|
|: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)|
|:,		Use a comma as a thousand separator|
|:_		Use a underscore as a thousand separator|
|:b		Binary format|
|:c		Converts the value into the corresponding Unicode character|
|:d		Decimal format|
|:e		Scientific format, with a lower case e|
|:E		Scientific format, with an upper case E|
|:f		Fix point number format|
|:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)|
|:g		General format|
|:G		General format (using a upper case E for scientific notations)|
|:o		Octal format|
|:x		Hex format, lower case|
|:X		Hex format, upper case|
|:n		Number format|
|:%		Percentage format|
