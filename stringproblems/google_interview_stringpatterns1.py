import itertools

# A permutation is an act of arranging objects or numbers in order. 
# Combinations are the way of selecting objects or numbers from a group of objects or collections, 
# in such a way that the order of the objects does not matter.
# An example of permutations is the number of 2 letter words that can be formed by using the letters in a word say, GREAT; 5P_2 = 5!/(5-2)! 
# An example of combinations is in how many combinations we can write the words using the vowels of the word GREAT; 5C_2 =5!/[2! (5-2)!]
# The formula for permutations is: nPr = n!/(n-r)! The formula for combinations is: nCr = n!/[r! (n-r)!]

# Example 1: Generate all permutations of a string
def generate_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

# Example 2: Find all subsequences of a string
def find_subsequences(s):
    subsequences = []
    for r in range(len(s) + 1):
        for sub in itertools.combinations(s, r):
            subsequences.append(''.join(sub))
    return subsequences

# Example 3: Find a specific subsequence in a string
def find_subsequence(s, sub):
    len_sub = len(sub)
    for i in range(len(s) - len_sub + 1):
        if s[i:i + len_sub] == sub:
            return True
    return False

# Example 4: Find all permutations of a string that contain a specific subsequence
def find_permutations_with_subsequence(s, sub):
    permutations = generate_permutations(s)
    return [p for p in permutations if find_subsequence(p, sub)]

# Example 5: Find all subsequences of a string that are palindromes
def find_palindromic_subsequences(s):
    subsequences = find_subsequences(s)
    return [sub for sub in subsequences if sub == sub[::-1]]

# Example 6: Find all subsequences of a string that are anagrams
def find_anagram_subsequences(s):
    subsequences = find_subsequences(s)
    return [sub for sub in subsequences if sorted(sub) == sorted(s)]

# Example 7: Find all subsequences of a string that are palindromes and anagrams
def find_palindromic_anagram_subsequences(s):
    subsequences = find_subsequences(s)
    return [sub for sub in subsequences if sub == sub[::-1] and sorted(sub) == sorted(s)]

import unittest
from google_interview_stringpatterns1 import *

class TestStringPatterns(unittest.TestCase):

    def test_generate_permutations(self):
        print('generate_permutations', generate_permutations('abc'))
        self.assertEqual(generate_permutations('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(generate_permutations(''), [''])

    def test_find_subsequences(self):
        print('find_subsequences',find_subsequences('abc'))
        self.assertEqual(find_subsequences('abc'), ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'])
        self.assertEqual(find_subsequences(''), [''])

    # def test_find_subsequence(self):
    #     self.assertTrue(find_subsequence('abc', 'a'))
    #     self.assertTrue(find_subsequence('abc', 'ab'))
    #     self.assertFalse(find_subsequence('abc', 'd'))

    # def test_find_permutations_with_subsequence(self):
    #     self.assertEqual(find_permutations_with_subsequence('abc', 'a'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #     self.assertEqual(find_permutations_with_subsequence('abc', 'ab'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #     self.assertEqual(find_permutations_with_subsequence('abc', 'd'), [])

    # def test_find_palindromic_subsequences(self):
    #     self.assertEqual(find_palindromic_subsequences('abcba'), ['', 'a', 'b', 'c', 'a', 'b', 'c', 'b', 'a', 'aa', 'aba', 'aca', 'aba', 'aca', 'aba', 'abcba'])
    #     self.assertEqual(find_palindromic_subsequences('abc'), ['', 'a', 'b', 'c'])

    # def test_find_anagram_subsequences(self):
    #     self.assertEqual(find_anagram_subsequences('abc'), ['', 'a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #     self.assertEqual(find_anagram_subsequences(''), [''])

    # def test_find_palindromic_anagram_subsequences(self):
    #     self.assertEqual(find_palindromic_anagram_subsequences('abcba'), ['', 'a', 'b', 'c', 'a', 'b', 'c', 'b', 'a', 'aa', 'aba', 'aca', 'aba', 'aca', 'aba', 'abcba'])
    #     self.assertEqual(find_palindromic_anagram_subsequences('abc'), ['', 'a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()