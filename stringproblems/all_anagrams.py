from collections import defaultdict

def find_all_anagrams(strings):
    anagrams = defaultdict(list)
    
    for string in strings:
        # sorted_string = ''.join(sorted(string))
        sorted_string = ''.join(sorted(string))
        anagrams[sorted_string].append(string)
        print('map', anagrams)
    
    return [values for values in anagrams.values() if len(values) > 1]

# Example usage
strings = ["cat", "dog", "tac", "god", "act"]
all_anagrams = find_all_anagrams(strings)
print(all_anagrams)