'''Section 2: Concept Questions [19 marks]
2.1 Write an function that takes in an input and checks to see
if it's an isogram. The function should return True or False.
'''
#To create this function I first defined a function called is_isogram 
#and passed it a parameter that accepts a proposed string. I then assigned
#a variable to 

def is_isogram(str_input):
    unique_letters = set()

    for letters in str_input:
        lowercase_letter = letters.lower()
        if lowercase_letter in unique_letters:
            return False
        unique_letters.add(lowercase_letter)

    return True

    done