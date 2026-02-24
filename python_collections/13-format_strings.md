# String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

<img width="935" height="354" alt="image" src="https://github.com/user-attachments/assets/bf1f78f3-9789-4478-a155-485b7b49a050" />

But we can combine strings and numbers using f-string or the format() method.

## F-Strings
F-String was introduced in Python 3.6 and now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal and add curly brackets {} as placeholders for variables and other operations.

<img width="940" height="384" alt="image" src="https://github.com/user-attachments/assets/1c67926f-1a12-493c-9c01-430d82f07177" />
<img width="363" height="46" alt="image" src="https://github.com/user-attachments/assets/a90801d3-854f-4be3-857d-2688e5a20b16" />

## Placeholders and Modifiers
A placeholder can contain variables, operations, functions and modifiers to format the value.

<img width="934" height="360" alt="image" src="https://github.com/user-attachments/assets/c7d1c7a7-c552-4114-b453-56d35f9afae6" />
<img width="1103" height="134" alt="image" src="https://github.com/user-attachments/assets/6df17182-a941-4a2a-8409-7326b9632dbe" />

A placeholder can include a modifier to format the value.
A modifier is included by adding a colon: followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

<img width="960" height="384" alt="image" src="https://github.com/user-attachments/assets/48297cb6-d23b-4679-be91-6552550ce21f" />
<img width="1137" height="151" alt="image" src="https://github.com/user-attachments/assets/a00a4e3f-ff07-4094-b7f1-9b0704bb8886" />

A placeholder can contain Python code, like math operations:

<img width="941" height="360" alt="image" src="https://github.com/user-attachments/assets/e0f52392-0d20-4229-a42e-b69bf19fe7aa" />
<img width="1141" height="78" alt="image" src="https://github.com/user-attachments/assets/c3284bf3-4eb2-4a80-908a-b9ce7c6320ab" />
