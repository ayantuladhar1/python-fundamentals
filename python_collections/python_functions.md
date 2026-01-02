What is a Function?
A function is a block of reusable code that runs only when called.

Syntax:
	def function_name(parameters):
	    statements
	    return value

Basic Function Example:
	def greet():
	    print("Hello, Welcome to Python")
	greet()
	
Function with Parameters:
	def add_numbers(a, b):
	    return a + b
	result = add_numbers(10, 20)
	print(result)
	
Function with Default Parameters:
	def country(name="USA"):
	    print("Country is:", name)
	country()
	country("Nepal")
	
Function Using If-Else:
	def check_even_odd(num):
	    if num % 2 == 0:
	        return "Even"
	    else:
	        return "Odd"
	print(check_even_odd(10))
	
Function Using List:
	def total_marks(marks):
	    return sum(marks)
	marks = [80, 90, 85]
	print(total_marks(marks))
