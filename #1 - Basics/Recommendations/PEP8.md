--Indentation:
    Use 4 spaces per indentation level. Never mix spaces and tabs.

--Maximum Line Length:
    Limit lines to 79 characters.
    For docstrings and comments, the limit is 72 characters.
    Use parentheses or \ for breaking long lines.

--Blank Lines:
    Use 2 blank lines to separate functions and class definitions at the top level.
    Use 1 blank line between methods within a class.

--Imports:
    Place all imports at the top of the file.
    Import one module per line:

        import os
        import sys

--Organize imports into three groups: standard library, third-party libraries, and local imports, separated by blank lines.
--Avoid wildcard imports (from module import *).

--Spaces Around Operators and Commas:
    -Add spaces around operators like =, ==, +, -, etc.

        x = 10
        y = x + 2

    -Do not add spaces before commas, periods, or parentheses:

        func(x, y)

--Comments:
    -Keep comments short and relevant, explaining what and why something is done.

    -Use capital letters and a space after # for single-line comments:

            # This is a comment

--For docstrings, use triple quotes """ to describe functions, classes, and methods:

        def add(a, b):
            """Adds two numbers and returns the result."""
            return a + b
        
--Variable and Function Names:
    -Use snake_case for variable and function names:

        my_variable = 10
        def my_function():
            pass

    -Use CamelCase for class names:

        class MyClass:
            pass
        Use UPPERCASE_WITH_UNDERSCORES for constants:

        MAX_SIZE = 100

--Function Structure:
    -If a function doesn’t explicitly return a value, end it with return None:

        def my_function():
            return None
        
--Expressions and Conditions:
    -Avoid overly complex inline expressions. Break logic into clear lines.

        if (x > 5 and
            y > 10):
            do_something()

--List Comprehensions:
    -Use list comprehensions where appropriate, but prioritize readability:
    # Good
        squares = [x**2 for x in range(10)]
    # Bad (not readable)
        squares = [x**2 for x in range(10) if x % 2 == 0 else None]

--Module Imports and Namespaces:
    -Use fully qualified names when importing modules to avoid namespace conflicts:

        import sys
        sys.exit()