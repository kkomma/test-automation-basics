import os

# Get all the methods in the os module
all_methods = [method_name for method_name in dir(os) if callable(getattr(os, method_name))]

# Print the list of methods
for method_name in all_methods:
    print("=" * 50)
    print(method_name)
    method_docstring = getattr(os, method_name).__doc__
    print(method_docstring)