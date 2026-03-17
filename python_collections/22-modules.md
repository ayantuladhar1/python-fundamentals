# Python Modules
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

## Create a Module
To create a module just save the code you want in a file with the file expression .py:

## Example:
Save this code in a file named mymodule.py
```python
def greeting(name):
  print("Hello, " + name)
```

## Use a Module
Now we can use the module we just created, by using the import statement:

## Example:
Import the module named mymodule, and call the freeting function:
```python
import mymodule
mymodule.greeting("Jonathan")
```
<img width="144" height="35" alt="image" src="https://github.com/user-attachments/assets/9cb61075-9af7-462f-a213-654a429afc09" />

Note: When using a function from a module, use the syntax module_name.function_name.

## Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

## Example:
Save thos code on the file mymodule.py
```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

## Example:
Import the module named mymodule, and access the person1 dictionary:
```python
import mymodule

a = mymodule.person1["age"]
print(a)
```

## Output
<img width="28" height="20" alt="image" src="https://github.com/user-attachments/assets/6bb4aa94-a7e3-420d-bf2c-a714dab45ec0" />

## Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

## Renaming a Module
You can create an alias when you import a module, by using the as keyword:

## Example:
Create an alias for mymodule called mx:
```python
import mymodule as mx
a = mx.person1["age"]
print(a)
```
<img width="27" height="21" alt="image" src="https://github.com/user-attachments/assets/a2affea6-3e5d-4406-9247-d8e55fad10b6" />

## Built-in Modules
There are several built-in modules in Python, which you can import whenver you like.

## Example:
Import and use the platform module:
```python
import platform

x = platform.system()
print(x)
```
<img width="72" height="28" alt="image" src="https://github.com/user-attachments/assets/227949b7-b465-4e9a-941a-4901474c02e5" />

## Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module.
The dir() function:

## Example:
List all the defined names belonging to the platform modeule:
```python
import platform

x = dir(platform)
print(x)
```

## Output
```list
['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES', 'WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package __', '__spec__', '__version__', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_perse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_aliases', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']
```
