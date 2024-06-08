def generate_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substrings.append(string[i:j])
    return substrings

# Example usage
string = "Hello"
substrings = generate_substrings(string)
print(substrings)