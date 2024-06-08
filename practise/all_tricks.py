from datetime import datetime
import subprocess

date_string = "2022-09-15"
date_format = "%Y-%m-%d"

date_object = datetime.strptime(date_string, date_format)
print(date_object)

date_string = "15012021"
date_format = "%d%M%Y"

date_object = datetime.strptime(date_string, date_format)
print(date_object)

a = [1, 2, 2, 3, 2, 4, 2]
print(a.count(2))

# Array methods in Python

# append() - Adds an element to the end of the array
a.append(5)
print(a)  # Output: [1, 2, 2, 3, 2, 4, 2, 5]

# insert() - Inserts an element at the specified position
a.insert(2, 6)
print(a)  # Output: [1, 2, 6, 2, 3, 2, 4, 2, 5]

# remove() - Removes the first occurrence of the specified element
a.remove(2)
print(a)  # Output: [1, 6, 2, 3, 2, 4, 2, 5]

# pop() - Removes the element at the specified position (or the last element if no position is specified) and returns it
removed_element = a.pop(3)
print(removed_element)  # Output: 3
print(a)  # Output: [1, 6, 2, 2, 4, 2, 5]

# clear() - Removes all elements from the array
a.clear()
print(a)  # Output: []

# index() - Returns the index of the first occurrence of the specified element
a = [1, 2, 2, 3, 2, 4, 2]
index = a.index(3)
print(index)  # Output: 3

# count() - Returns the number of occurrences of the specified element
count = a.count(2)
print(count)  # Output: 4

# sort() - Sorts the elements in ascending order
a.sort()
print(a)  # Output: [1, 2, 2, 2, 2, 3, 4]

# reverse() - Reverses the order of the elements
a.reverse()
print(a)  # Output: [4, 3, 2, 2, 2, 2, 1]

# copy() - Returns a copy of the array
b = a.copy()
print(b)  # Output: [4, 3, 2, 2, 2, 2, 1]


s='hello world 123'
# String methods in Python
# capitalize() - Converts the first character of a string to capital (uppercase) letter
capitalized_string = s.capitalize()
print(capitalized_string)  # Output: "Hello world"
# lower() - Converts all characters of a string to lowercase
lowercase_string = s.lower()
print(lowercase_string)  # Output: "hello world"
# upper() - Converts all characters of a string to uppercase
uppercase_string = s.upper()
print(uppercase_string)  # Output: "HELLO WORLD"
# swapcase() - Swaps the case of all characters in a string
swapped_case_string = s.swapcase()
print(swapped_case_string)  # Output: "HELLO WORLD"
# title() - Converts the first character of each word in a string to capital (uppercase) letter
title_string = s.title()
print(title_string)  # Output: "Hello World"
# strip() - Removes leading and trailing whitespace characters from a string
stripped_string = s.strip()
print(stripped_string)  # Output: "hello world"
# lstrip() - Removes leading whitespace characters from a string
left_stripped_string = s.lstrip()
print(left_stripped_string)  # Output: "hello world"
# rstrip() - Removes trailing whitespace characters from a string
right_stripped_string = s.rstrip()
print(right_stripped_string)  # Output: "hello world"
# split() - Splits a string into a list of substrings based on a delimiter
split_string = s.split()
print(split_string)  # Output: ['hello', 'world']
# join() - Joins the elements of a list into a string using a specified delimiter
joined_string = '-'.join(split_string)
print(joined_string)  # Output: "hello-world"
# replace() - Replaces all occurrences of a specified substring with another substring
replaced_string = s.replace('world', 'universe')
print(replaced_string)  # Output: "hello universe"

# Import the necessary modules

# Define the command to run Valgrind
# valgrind_command = ["valgrind", "--leak-check=full", "--show-leak-kinds=all", "--track-origins=yes", "python", "/Users/veeranica/Desktop/pyt/coding/test-automation-basics/practise/all_tricks.py"]

# # Run Valgrind and capture the output
# valgrind_output = subprocess.check_output(valgrind_command, stderr=subprocess.STDOUT)

# # Print the Valgrind output
# print(valgrind_output.decode())