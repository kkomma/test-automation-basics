import copy

class APFSFile:
    def __init__(self, name, data):
        self.name = name
        self.data = data

def clone_file(original_file):
    return copy.copy(original_file)

# Test case
original_file = APFSFile("test_file.txt", "This is some test data.")
cloned_file = clone_file(original_file)

print("Original File Data:", original_file.data)
print("Cloned File Data:", cloned_file.data)
print("Files are identical:", original_file.data == cloned_file.data)
print("Files are the same object:", original_file is cloned_file)
