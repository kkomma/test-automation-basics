def testSuite(tests):
    # Simulate test suite behavior
    # For this example, tests 3 and 5 fail when run together
    if 3 in tests and 5 in tests:
        return False
    return True

def find_failing_pair(tests):
    # Iterate over all pairs of tests
    for i in range(1, len(tests)):
        for j in range(i + 1, len(tests) + 1):
            # Call testSuite with the current pair of tests
            if not testSuite(tests[i - 1:j]):
                # If the pair fails, return the test numbers
                return (tests[i - 1], tests[j - 1])
    # If no failing pair is found, return None
    return None

# Test cases
tests = [1, 2, 3, 4, 5, 6]

# Test 1: Find failing pair
failing_pair = find_failing_pair(tests)
assert failing_pair == (3, 5), "Test 1 failed"

# Test 2: No failing pair
tests = [1, 2, 3, 4, 6]
failing_pair = find_failing_pair(tests)
assert failing_pair is None, "Test 2 failed"

# Test 3: Edge case - empty list
tests = []
failing_pair = find_failing_pair(tests)
assert failing_pair is None, "Test 3 failed"

print("All tests passed!")