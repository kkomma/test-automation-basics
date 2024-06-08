import re

def starts_with_vowel(s):
    return bool(re.match(r'^[aeiou].*', s))

def contains_vowel(s):
    return bool(re.search(r'.[aeiou]*', s))

s = 'Amazon Amazing'

print(starts_with_vowel(s.lower()))  # Returns: False
print(contains_vowel(s.lower()))    # Returns: True