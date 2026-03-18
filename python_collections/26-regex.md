# Python RegEx
A RegEx, or Regular Expression is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

## RegEx Module
Python has built-in package called re, which can be used to work with Regular Expressions.

Import the re module
```python
import re
```

## RegEx in Python
When you have imported the re module, you can start using regular expressions:

## Example:
Search the string to see if it starts with "The" and ends with "Spain":
```python
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
```
<img width="197" height="35" alt="image" src="https://github.com/user-attachments/assets/e825c9b2-452f-4439-883d-d598cfde8c55" />

## RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:
|Function| Description|
|--------|------------|
|findall| Returns a list containing all matches|
|search| Returns a Match object if there is a match anywhere in the string|
|split| Returns a list where the string has been split at each match|
|sub| Replaces one or many matches with a string|

## Metacharacters
Metacharacters are characters with a special meaning:
|Character| Description| Example|
|---------|------------|--------|
|[]|	A set of characters	|"[a-m]"	|
|"backslash"|	Signals a special sequence (can also be used to escape special characters)|	"\d"	|
|.|	Any character (except newline character)|	"he..o"	|
|^|	Starts with	|"^hello"	|
|$|	Ends with	|"planet$"	|
|star|	Zero or more occurrences| "he.*o"	|
|+|	One or more occurrences	|"he.+o"	|
|?|	Zero or one occurrences	|"he.?o"	|
|{}|	Exactly the specified number of occurrences	|"he.{2}o"	|
|type	|Either or	|"falls/stays"|	
|()|	Capture and group	 	 |

## Example:
[] = A set of characters	"[a-m]"
```python
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)
```
<img width="317" height="40" alt="image" src="https://github.com/user-attachments/assets/169ed97c-7237-4d47-b5cd-c743ce215f2e" />  

"backslash" = Signals a special sequence (can also be used to escape special characters)	"\d"
```python
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)
```
<img width="102" height="35" alt="image" src="https://github.com/user-attachments/assets/d94c0571-ab9c-4e2f-ba21-df38c60ef3fd" />

. = Any character (except newline character)	"he..o"
```python
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)
```
<img width="93" height="32" alt="image" src="https://github.com/user-attachments/assets/81046a17-d38b-4af7-ac1a-039b78a2a2c3" />

^ =	Starts with	"^hello"
```python
import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
```
<img width="323" height="30" alt="image" src="https://github.com/user-attachments/assets/827b7720-4b95-4c88-a926-69a888e877d6" />

$ =	Ends with	"planet$"
```python
import re
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
```
<img width="309" height="39" alt="image" src="https://github.com/user-attachments/assets/9ee16970-d6b4-4f3b-b708-28e6e3e683cd" />

star =	Zero or more occurrences	"he.*o"
```python
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)
```
<img width="85" height="26" alt="image" src="https://github.com/user-attachments/assets/baf74c97-fe1f-40be-ad47-3a206f27c0d6" />

plus = One or more occurrences	"he.+o"
```python
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)
```
<img width="85" height="31" alt="image" src="https://github.com/user-attachments/assets/2322fc7a-90be-4f40-9c07-43bc8ef42852" />

? =	Zero or one occurrences	"he.?o"
```python
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
```
<img width="26" height="33" alt="image" src="https://github.com/user-attachments/assets/52194c97-97d9-42a0-a47b-3de1e1934bf8" />

{} = Exactly the specified number of occurrences	"he.{2}o"
```python
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)
```
<img width="85" height="29" alt="image" src="https://github.com/user-attachments/assets/b99ea221-3ccb-44b2-a967-16feaa3a62b1" />  

type = Either or	"falls/stays"
```python
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="304" height="60" alt="image" src="https://github.com/user-attachments/assets/5b78bd53-e112-4b6c-ba04-8976f0d8eb2f" />

## Flags 
You can add flags to the pattern when using regular expressions.
|Flag| Shorthand| Description|
|----|----------|------------|
|re.ASCII|	re.A|	Returns only ASCII matches|	
|re.DEBUG|		|Returns debug information|
|re.DOTALL|	re.S|	Makes the . character match all characters (including newline character)|
|re.IGNORECASE|	re.I|	Case-insensitive matching|
|re.MULTILINE|	re.M|	Returns only matches at the beginning of each line|
|re.NOFLAG|		|Specifies that no flag is set for this pattern|
|re.UNICODE|	re.U|	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches|
|re.VERBOSE|	re.X|	Allows whitespaces and comments inside patterns. Makes the pattern more readable|

## Example:
re.ASCII, re.A = Returns only ASCII matches
```python
import re
txt = "Åland"
#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))
#Without the flag, the example would return all character:
print(re.findall("\w", txt))
#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))
```
<img width="230" height="86" alt="image" src="https://github.com/user-attachments/assets/5306b68b-e76b-4c78-872d-1e09b691cd48" />

re.DEBUG = Returns debug information
```python
import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.DEBUG))
```
<img width="385" height="412" alt="image" src="https://github.com/user-attachments/assets/e42bba66-2b07-41ec-93c0-c6f16576c715" />

re.DOTALL, re.S	= Makes the . character match all characters (including newline character)
```python
import re
txt = """Hi
my
name
is
Sally"""
#Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))
#This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt))
#Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S))
```
<img width="101" height="82" alt="image" src="https://github.com/user-attachments/assets/955a483b-3a42-4647-970b-4d20e4b2fa2a" />

re.IGNORECASE, re.I = Case-insensitive matching
```python
import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE))
#Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I))
```
<img width="80" height="52" alt="image" src="https://github.com/user-attachments/assets/3709fed4-d92a-41cf-8d04-b044a5235faa" />

re.MULTILINE, re.M = Returns only matches at the beginning of each line
```python
import re
txt = """There
aint much
rain in 
Spain"""
#Search for the sequence "ain", at the beginning of a line:
print(re.findall("^ain", txt, re.MULTILINE))
#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^ain", txt))
#Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M))
```
<img width="70" height="76" alt="image" src="https://github.com/user-attachments/assets/c723a555-d64a-4065-b853-852901fd21f3" />

re.UNICODE, re.U = Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches
```python
import re
txt = "Åland"
#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))
#Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))
```
<img width="226" height="61" alt="image" src="https://github.com/user-attachments/assets/163bbda8-9081-4fa8-a92f-cf097023f1ca" />

re.VERBOSE, re.X = Allows whitespaces and comments inside patterns. Makes the pattern more readable
```python
import re
text = "The rain in Spain falls mainly on the plain"
#Find and return words that contains the phrase "ain":
pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""
print(re.findall(pattern, text, re.VERBOSE))
#The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text))
#Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X))
```
<img width="327" height="91" alt="image" src="https://github.com/user-attachments/assets/5438b79c-fc13-4abd-acc8-d97cd502f6d6" />

## Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
|Character| Description| Example|
|---------|------------|--------|
|\A|	Returns a match if the specified characters are at the beginning of the string|	"\AThe"|	
|\b|	Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")|	r"\bain" r"ain\b"|	
|\B|	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")| r"\Bain" r"ain\B"|
|\d|	Returns a match where the string contains digits (numbers from 0-9)|	"\d"|	
|\D|	Returns a match where the string DOES NOT contain digits|	"\D"|	
|\s|	Returns a match where the string contains a white space character|	"\s"|	
|\S|	Returns a match where the string DOES NOT contain a white space character| "\S"|
|\w|	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)| "\w"|	
|\W|	Returns a match where the string DOES NOT contain any word characters|	"\W"|	
|\Z|	Returns a match if the specified characters are at the end of the string|	"Spain\Z"|

## Example
\A = Returns a match if the specified characters are at the beginning of the string	eg."\AThe"
```python
import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
```
<img width="208" height="58" alt="image" src="https://github.com/user-attachments/assets/68fdb4c4-09ec-4a99-8265-4e6eec205214" />

\b	= Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string"), eg.	r"\bain" and r"ain\b"
```python
import re
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="77" height="55" alt="image" src="https://github.com/user-attachments/assets/b8bc7d73-f654-4dde-8496-a20ad0e17b1d" />

```python
import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="293" height="57" alt="image" src="https://github.com/user-attachments/assets/5e37ee3c-f4a4-47fc-86f2-09a8f9461531" />

\B = Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string"), eg.	r"\Bain" r"ain\B"
```python
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="302" height="61" alt="image" src="https://github.com/user-attachments/assets/f870233c-f442-433b-89b3-e32bc31f5ffb" />

```python
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="78" height="49" alt="image" src="https://github.com/user-attachments/assets/81ffc67e-7923-4d06-ac37-aeaba4190711" />

\d = Returns a match where the string contains digits (numbers from 0-9), eg. "\d"
```python
import re
txt = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="79" height="48" alt="image" src="https://github.com/user-attachments/assets/f3349db0-c72e-403d-a97f-bfbcec0ea9fd" />

\D = Returns a match where the string DOES NOT contain digits, eg. "\D"
```python
import re
txt = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="750" height="52" alt="image" src="https://github.com/user-attachments/assets/26a97938-7c26-4e2c-88ea-c2081fda3a14" />

\s = Returns a match where the string contains a white space character, eg.	"\s"\
```python
import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="302" height="58" alt="image" src="https://github.com/user-attachments/assets/5e29ef64-4cce-4279-a077-286b167f9ab4" />

\S = Returns a match where the string DOES NOT contain a white space character, eg. "\S"
```python
import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="630" height="59" alt="image" src="https://github.com/user-attachments/assets/4adf620e-f123-4a93-8e39-8a5896db226e" />

\w = Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character), eg. "\w"
```python
import re
txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="626" height="56" alt="image" src="https://github.com/user-attachments/assets/a19ba386-316f-47c6-b6c1-79479722f3f8" />

\W = Returns a match where the string DOES NOT contain any word characters, eg. "\W"
```python
import re
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="302" height="63" alt="image" src="https://github.com/user-attachments/assets/c087fe2c-78a5-45c6-96c4-0a3876454ce3" />

\Z = Returns a match if the specified characters are at the end of the string, eg. "Spain\Z"
```python
import re
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
```
<img width="201" height="60" alt="image" src="https://github.com/user-attachments/assets/63ebae13-d6c3-49d0-a458-28059f96d999" />

## Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:
|Set| Description|
|---|------------|
|[arn]|	Returns a match where one of the specified characters (a, r, or n) is present|	
|[a-n]|	Returns a match for any lower case character, alphabetically between a and n|	
|[^arn]|	Returns a match for any character EXCEPT a, r, and n|	
|[0123]|	Returns a match where any of the specified digits (0, 1, 2, or 3) are present|
|[0-9]|	Returns a match for any digit between 0 and 9|	
|[0-5][0-9]|	Returns a match for any two-digit numbers from 00 and 59|
|[a-zA-Z]|	Returns a match for any character alphabetically between a and z, lower case OR upper case|
|[+]|	In sets, +, *, ., type, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string|

## Example:
[arn]	= Returns a match where one of the specified characters (a, r, or n) is present
```python
import re
txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="300" height="56" alt="image" src="https://github.com/user-attachments/assets/54e4f22a-a7d5-496c-86c8-44daed8a4f2d" />

[a-n] =	Returns a match for any lower case character, alphabetically between a and n
```python
import re
txt = "The rain in Spain"
#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="453" height="56" alt="image" src="https://github.com/user-attachments/assets/2952fa7e-cc78-4900-9e66-c915c3b62cb6" />

[^arn] =	Returns a match for any character EXCEPT a, r, and n
```python
import re
txt = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="499" height="60" alt="image" src="https://github.com/user-attachments/assets/0b6d51ba-7962-468a-929c-07b234b5faa5" />

[0123] = Returns a match where any of the specified digits (0, 1, 2, or 3) are present
```python
import re
txt = "The rain in Spain"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="73" height="53" alt="image" src="https://github.com/user-attachments/assets/37784c16-44d6-4c42-8daf-d64736158027" />

[0-9] =	Returns a match for any digit between 0 and 9
```python
import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="296" height="48" alt="image" src="https://github.com/user-attachments/assets/d9fbfb1a-8b58-48fa-b2bc-1051490eec93" />

[0-5][0-9] = Returns a match for any two-digit numbers from 00 and 59
```python
import re
txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="295" height="59" alt="image" src="https://github.com/user-attachments/assets/f95286f6-5d69-438c-8f2f-c7ff478d1e76" />

[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
```python
import re
txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="583" height="55" alt="image" src="https://github.com/user-attachments/assets/e56a7cb4-35b9-4cff-9df0-7b01bd569239" />

[+] = In sets, +, *, ., type, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
```python
import re
txt = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="83" height="52" alt="image" src="https://github.com/user-attachments/assets/a7f89d49-a8c7-49da-a45d-a201aa3f8c5e" />

## The findall() Function
The findall() function returns a list containing all matches.

## Example:
Print a list of all matches:
```python
import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
```
<img width="114" height="37" alt="image" src="https://github.com/user-attachments/assets/a725abd6-a023-4a98-bfa6-598809e48e07" />

The list contains the matches in the order they are found.
If no mataches are found, an empty list is returned:

## Example:
Return an empty list if no match was found:
```python
import re
txt = "The rain in Spain"
#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
```
<img width="81" height="52" alt="image" src="https://github.com/user-attachments/assets/423c1f83-aa96-4dbe-9c72-dd1b835185a8" />

## The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:

## Example:
Search for the first white-space character in the string:
```python
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
```
<img width="514" height="35" alt="image" src="https://github.com/user-attachments/assets/7ab5a002-d0d5-4628-961e-effa8dad41d7" />

If no matches are found, the value None is returned:

## Example:
Make a search that returns no match:
```python
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
```
<img width="40" height="29" alt="image" src="https://github.com/user-attachments/assets/f13bba5e-e951-4355-a45b-62f68b4ba834" />

## The split() Function
The split() function returns a list where te string has been split at each match:

## Example:
Split at each white-space character:
```python
import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
```
<img width="263" height="36" alt="image" src="https://github.com/user-attachments/assets/ba80a41d-324a-416a-b412-b90feef9be8d" />

You can control the number of occurrences by specifying the maxsplit parameter:

## Example: 
Split the string only at first occurence:
```python
import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
```
<img width="221" height="32" alt="image" src="https://github.com/user-attachments/assets/af632fe3-993f-4d23-9aa5-c3717efb0be4" />

## The sub() Function
The sub() function replaces the matches with the text of your choice:

## Example:
Replace every white-space character with the number 9:
```python
import re
#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
```
<img width="169" height="28" alt="image" src="https://github.com/user-attachments/assets/a5391e04-f3cb-45d3-b65b-b3a13a10749b" />

You can control the number of replacements by specifying the count parameter:

## Example:
Replace the first 2 occurrences:
```python
import re
#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
```
<img width="163" height="32" alt="image" src="https://github.com/user-attachments/assets/a4355517-5944-4b5b-8433-ed07a37930e7" />

## Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match object.

## Example:
Do a search that will return a Match Object:
```python
import re
#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
```
<img width="431" height="28" alt="image" src="https://github.com/user-attachments/assets/689e1a45-8e13-4b97-8a08-4c3cb839eb0e" />

The Match object has properties and methods used to retrieve information about the search, and the result:
.span() = returns a tuple containing the start, and end positions of the match.
.string() = returns the string passed into the function
.group() = returns the part of the string where there was a match

## Example:
Print the position (start - and - end position) of the first match occurence.
The regular expression looks for any words that starts with an upper case "S":
```python
import re
#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
```
<img width="75" height="25" alt="image" src="https://github.com/user-attachments/assets/4c4010ee-4eae-43fb-95d4-1a80fb1fbf45" />

## Example:
Print the string passed into the function:
```python
import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
```
<img width="55" height="29" alt="image" src="https://github.com/user-attachments/assets/dc71f1fd-b4f5-46d7-a1ee-4f248096dc70" />

## Example
Print the part of the string where there was a match.
The regular expression lokks for any words that starts with an upper case "S":
```python
import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
```
<img width="53" height="31" alt="image" src="https://github.com/user-attachments/assets/b950db54-ea44-434c-b794-1235996cea8e" />

Note: If there is no match, the value None will be returned, instead of the Match Object.
