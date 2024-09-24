#Download&Install Python
    https://www.python.org/downloads/
    Verify PATH variable C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python3xx\
    Check if installed: cmd terminal -> python --version

cmd:
C:\Users\YOUR_USER>python
Python 3.12.6 (tags/v3.12.6, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
*Python is running*

#Key Features of Python
Dynamic and Interpreted: 
    Python doesn't require explicit type declarations, meaning variables can hold different types of values, and type checking happens at runtime, not during compilation.
Flexible Syntax: 
    Python uses indentation to define code blocks (like functions and loops), instead of curly braces ({}). This makes the code cleaner but requires careful attention to indentation.
Case-Sensitive: 
    Python treats variables like a and A as different. Variable names must be consistent.
Using the Python Interpreter:
    You can quickly test Python code using the Python interpreter, which allows you to type code and see the results immediately. To start the interpreter, run python3 in the terminal.

Example:
    a = 6
    print(a + 2)  # Outputs: 8
    a = "hello"
    print(a + str(len(a)))  # Outputs: hello5


Python Files and Modules:
    Python scripts have the .py extension. 
    You can run them from the command line using python3 filename.py. 
    Modules are reusable Python files that can be imported into other scripts.

Example:
    import sys

    def main():
        print('Hello', sys.argv[1])

    if __name__ == '__main__':
        main()
    This script takes a command-line argument and prints it after "Hello".


Functions:
    Functions in Python are defined using the def keyword. 
    They can take parameters and return values. 
    A docstring (triple-quoted string) can be used to describe what the function does.

Example:
    def repeat(s, exclaim):
    """
    Repeats the string s three times. Adds exclamation marks if exclaim is True.
    """
    result = s * 3  # Repeats the string three times
    if exclaim:
        result += '!!!'
    return result


Indentation and Syntax:
    Python uses indentation (4 spaces is standard) to define code blocks. 
    Mixing spaces and tabs can cause errors. Pay close attention to consistent indentation.
    Comments start with # and continue to the end of the line.


Runtime Error Handling:
    Python doesn’t catch all errors at the time of writing or compiling. 
    It only raises errors when code is executed. For instance, if a function is misspelled, the error will only occur when the code tries to run that specific function.

Example:
if name == 'Guido':
    print(repeeeet(name))  # Will only raise an error if executed


Importing and Modules:
    You can reuse code by importing modules. Modules have their own namespace, preventing conflicts between names in different files. You can either import an entire module or specific functions from it.
    
Example:
    import sys
    sys.exit()  # Exits the program


Getting Help in Python:
Python provides built-in tools to explore its functions and modules:
help(function_name) shows the documentation for any function or module.
dir(object) lists all the attributes and methods of an object.

Example:
    help(len)  # Shows how the len() function works
    dir(str)  # Lists all methods available for strings


Type Annotations:
Python 3 introduced type hints, which help clarify what types are expected for function arguments and return values, though they are optional and not enforced.

Example:
    def is_positive(n: int) -> bool:
        return n > 0


Variable Naming:
Since Python doesn’t require you to declare types explicitly, it’s important to use clear and meaningful variable names to keep track of what each variable represents. 
For example, use name for a single name, and names for a list of names.