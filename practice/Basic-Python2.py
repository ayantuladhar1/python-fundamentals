#Function to compare between two values
def compares(a,b):
    if a > b:
        print('From: method outside the main method: a is greater than b')
    elif a < b:
        print('a is less than b')
    else:
        print('a is equal')

def add(a1,b1):
    return a1+b1


# Below is the main method
if __name__ =='__main__':
    print('Hello World')
    a = 30
    b = 20
    compares(a,b)
    x= add(a,b)
    print("From main method compare:" , x) #It adds up a=30 + b=20 and prints the result as 50

    #ll is a list
    ll = [1,2,3]
    for x in ll: #for loop
        print("Printing from List", x)

    print('EMPTY')
    #To print max value of the list using for loop
    l1 =[1,2,3,6,4,5]
    max = l1[0]
    for x in l1:
        if x>max:
            max = x
    print("Printing max value of the list", max)

    #To print min value of the list using for loop
    min = l1[0]
    for x in l1:
        if x<min:
            min = x
    print("Printing min value of the list", min)

    #Below for loop prints all the elements inside l1 [1,2,3,6,4,5]
    for i in range(0,len(l1)):
        print("All the elements in l1", i)

    # Below for loop prints all the elements inside l2 [10,20,30,40,50,11,23,25,47]
    l2 = [10,20,30,40,50,11,23,25,47]
    for i in range(0, len(l2)):
        print("All the elements in l2", i, l2[i])

    #To check odd or even numbers using if else statements
    x = 11
    if x % 2 == 0:
        print("If/else", 'even')
    else:
        print("If/else", 'odd')

    #To check odd or even numbers using for each loop and if else statement
    for each in l2:
        if each % 2 == 0:
           print("For each loop",'even', each)
        if each % 2 == 1:
            print("For each loop",'odd', each)

    #To display even and odd elements from the list
    l2 = [10, 20, 30, 40, 50, 11, 23, 25, 47]
    for i in range (0,len(l2)):
        if i % 2 == 0: #For even calculations
            print ("For i in range loop", l2[i])

    #Slicing elements from the list
    l2 = [10, 20, 30, 40, 50, 11, 23, 25, 47]
    print('**********************************')
    print ('  0   1   2   3   4   5   6   7   8')
    print(l2)
    print(' -9  -8  -7  -6  -5  -4  -3  -2  -1')
    print('**********************************')
    print("Slicing 1st to 3rd element:", l2[0:4])
    print("Slicing up to 4th element:", l2[:4])
    print("Slicing from beginning element to the end:", l2[0:])
    print("Slicing 1st to 9th element:", l2[0:9])
    print("Slicing the last element:", l2[-1])
    print("Slicing the 2nd last element:", l2[-2])
    print("Slicing from the 5th element to last element(exclusive):", l2[-5:-1])
    print("Slicing from the 5th element to last element(inclusive):", l2[-5:])

    #Slicing String
    message = 'Hello World'
    print('*********************************************')
    print('  0   1   2   3   4   5   6   7   8   9   10')
    print('  H   e   l   l   o       W   o   r   l   d')
    print(' -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1')
    print('*********************************************')
    print("Slicing string from 1st element to 7th(last exclusive):", message[1:7])
    print("Length of the message:", len(message))
    print("Slicing string from 6th element to end:", message[6:])
    print("Slicing string from beginning element to 5th element(last exclusive):", message[0:5])

    print(' ')

    #For loop to print everything inside variable message
    for x in message:
        print("From for loop", x)
    print('')

    #For i in range loop to calculate odd indexes
    for i in range (0,len(message)):
            if i % 2 == 1:
                print(message[i], i)

    S1= [5, 4, 6, 8, 1, 9, 4]
    print (S1[:7])
    print(S1[0:])
    print(S1[0:5])
    print(len(S1))
    print(S1[5])

    dmap = {'a':1, 'b':2, 'c':3}
    dmap['d'] =4
    print (dmap)

    dmap['d'] = dmap['d']+1
    print(dmap)

    d={}
    dmap['d'] =50
    print(dmap)

    letter = ['a','b','c','d','a','c','c','d','d']
    output = {'a':2, 'b':1, 'c':3, 'd':3}
    counter = 0
    counter1=0
    for x in letter:
        if x == 'a':
            counter += 1
        if x == 'a':
            counter1+= 1
    print (counter, counter1)

    counters = {}

    for x in letter:
        if x in counters:
            counters[x] = counters[x]+1
        else:
            counters[x] = 1 #{'a': 1}
    print("From counters", counters)

    message = 'Hello World'
    counters ={}
    for x in message:
        if x in counters:
            counters[x] = counters[x]+1
        else:
            counters[x] = 1
    print(counters)

    line = 'hello world hi world hi usa hi nepal'
    words = line.split(' ')
    print (words)
    counters = {}
    for x in words:
        if x in counters:
            counters[x] = counters[x]+1
        else:  counters[x] = 1
    print (counters)

    max_word =''
    max_freq=0
    for x in counters.keys():
        if counters[x]>max_freq:
            max_freq = counters[x]
            max_word=x
    print("max-freq", max_word)

    min_word = ''
    min_freq = 100
    for x in counters.keys():
        if counters[x] < min_freq:
            min_freq = counters[x]
            min_word = x
    print("min-freq", min_word)

    min_freq = 100
    for x in counters.keys():
        if counters[x] < min_freq:
            min_freq = counters[x]

    for x in counters.keys():
        if counters[x] == min_freq:
            print(x)

    max_val = float('inf')  # Positive infinity
    min_val = float('-inf')  # Negative infinity
    max_freq= float('-inf')
    for x in counters.keys():
        if counters[x] > max_val:
            max_freq=counters[x]

    max_words  = []
    for x in counters.keys():
        if counters[x] == max_freq:
            max_words.append(x)
    print(max_words)

    dict = {'a':1, 'b':2, 'c':3}
    counters = {}
    for key in dict.keys():
        value = dict.get(key)
        counters[value] = key
    print(counters)
    #output = {1:'a', 2:'b', 3:'c'}

    counters = {}
    for x in dict.keys():
        counters[x]=dict.get(x)*dict.get(x)
    print("From dict", counters)
    # output = {'a': 1, 'b': 4, 'c': 9}

    def add(a):
        return a + 10
    print(add(5))
    #output 15
    f = lambda a:a+10
    print(f(5))
    # output 15
    f1 = lambda a,b: a+b
    print(f1(5,5))
    #output 10

    input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    x = 'eat'
    y = sorted(x)
    print (y)

    y1 = "".join(y)
    print (y1)



    d={}
    for x in input:
        sorted_word = "".join(sorted(x))
        if sorted_word not in d: #{'aet': [eat]}
            d[sorted_word] = [x]
        else:
            d[sorted_word].append(x) #{'aet': [eat, tea, ate], 'ant':[tan, nat]}
    print (d.values())
    #Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


#Write a Python function to convert two lists into a dictionary.
#Input: Keys=['a', 'b', 'c'], Values=[1, 2, 3]
#Output: {'a': 1, 'b': 2, 'c': 3}
    d1= {}
    InputKeys=['a', 'b', 'c']
    Values=[1, 2, 3]
    for i in range(len(InputKeys)):
        k = InputKeys[i]
        v = Values[i]
        d1[k] = v
    print(d1)

'''Write a Python function to find common keys in two dictionaries.
Input: {'a': 1, 'b': 2, 'c':5}, {'b': 3, 'c': 4} 
Output: ['b' , 'c']'''

Output = []
d1 = {'a': 1, 'b': 2, 'c':5}
d2 = {'b': 3, 'c': 4}
for x in d1.keys():
    if x in d2.keys():
     Output.append(x)
print(Output)

'''Write a Python function to remove all duplicate characters in a given string while preserving the order of the remaining characters.
Input: "programming"
Output: "progamin"'''

Input = "programming"
#Output: "progamin"
Output = []
for ch in Input:
        if ch not in Output:
            Output.append(ch)
print(Output)
Output = "".join(Output)
print(Output)

'''Find the First Non-Repeating Character
Write a Python function to find the first non-repeating character in a given string and return its index.
Input: "swiss"
Output: 1 (for 'w' in "swiss")'''

input = "swiss"
output = {}
for ch in input:
    if ch not in output:
        output[ch] = 1
    else:
        output[ch] += 1
print(output)
#{'s': 3, 'w': 1, 'i': 1}
result =""
for x in input:
    freq=output[x]
    if freq ==1:
        result = x
print(result)

'''Write a Python function to flatten a nested list.
Input: [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]'''

input= [[1, 2], [3, 4], [5]]
output = []
for x in input:
    for y in x:
        output.append(y)
print(output)