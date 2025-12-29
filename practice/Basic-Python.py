#Function to compare between two values
def compare(a,b):
    if a > b:
        print("a is greater than b")
    elif a < b:
        print ("b is greater than a")
    else:
        print ("a is equal")

def add (a,b):
    return a+b

if __name__ == '__main__':
    compare(2, 5)
    print(add (2, 5))

#List
#To print all the elements in the list
ll = [1, 2 ,3]
for x in ll:
    print ("All elements in list", ll)

#To print max value of list using loop
max_list = ll[0]
for x in ll:
    if x > max_list:
        max_list = x
print ("Max value is:", max_list)


#To print min value of list using loop
min_list = ll[0]
for x in ll:
    if x < min_list:
        min_list = x
print ("Min value is:", min_list)

#Below for loop to print all the elements inside ll
for i in range(0, len(ll)):
    print ("All indexes with their elements in list using for i loop", i, ll[i])

#Print each number using a for loop
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print (numbers[i])

#Print all the sum of all numbers
numbers = [3, 5, 7, 9]
total = 0
for x in numbers:
    total = total + x
print(total)

print('*******')

#To count even or odd numbers
numbers = [2, 7, 4, 9, 12 ,15]
even_count = 0
odd_count = 0
for x in numbers:
    if x % 2 == 0:
        even_count += 1
    elif x % 2 == 1:
        odd_count += 1
print (even_count)
print (odd_count)

#To display even or odd numbers
numbers = [2, 7, 4, 9, 12 ,15]
for x in numbers:
    if x % 2 == 0:
        print ('Even', x)
    else:
        print ('Odd', x)