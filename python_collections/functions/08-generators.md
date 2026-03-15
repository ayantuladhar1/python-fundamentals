# Python Generators
Generators are functions that can pause and resume their execution.
When a generator function is called, it returns a generator object, which is an iterator.
The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

## Example:
A simple generator function:
```python
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
```

## Output
1
2
3

Generators allow you to iterate over data without storing the entire dataset in memory.
Instead of using return, generators use the yield keyword.

## The yield Keyword
The yield keyword is what makes a function a generator.
With yield is encountered, the function's state is saved and the value is returned. The next time the generator is called, it continues from where it left off.

## Example:
Genrator that yield numbers:
```python
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
```

## Output
1
2
3
4
5

Unlike return, which terminates the function, yield pauses it and can be called multiple times.

## Generators Saves Memory
Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
For large datasets, generators save memory:

## Example:
Generator for large sequences:
```python
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
```

## Output
0
1
2

## Using next() with Generators
You can manually iterate through a generator using the next() function:

## Example:
```python
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
```

## Output
Emil
Tobias
Linus

When there are no more values to yield the generator raises a StopIteration execption:

## Example:
```python
def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))  # This will raise StopIteration
```

## Output
1
2
Traceback (most recent call last):
  File "./prog.py", line 8, in <module>
StopIteration

## Generator Expressions
Similar to list comprehensions, you can create generators using generator expressions with parantheses instead of square brackets:

## Example:
List comprehension vs generator expression:
```python
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
```

## Output
```list
[0, 1, 4, 9, 16]
<generator object <genexpr> at 0x...>
[0, 1, 4, 9, 16]
```

## Example:
Using a generator expression with sum:
```python
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)
```

## Output
285

## Fibonacci Sequence Generator
Generators can be used to create the Fibonacci sequence.
It can continue generating values indefinitely, without running out of memory:

## Example:
Generate 100 Fibonacci numbers:
```python
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))
```

## Output
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026


