'''
Section 2: Concept Questions [19 marks]
2.2 Make a new test file and write comprehensive unit tests for the
function you wrote in 2.1. [12 marks]
'''

from Section_2_Answer import is_isogram

def test_is_isogram():
    # Test case 1: A string with all unique characters is an isogram
    assert is_isogram("isogram") == True, "Test case 1 failed"

    # Test case 2: A string with repeating characters is not an isogram
    assert is_isogram("hello") == False, "Test case 2 failed"

    # Test case 3: A string with repeating characters in different cases is not an isogram
    assert is_isogram("HeLlo") == False, "Test case 3 failed"

    print("All test cases passed")

test_is_isogram()

done