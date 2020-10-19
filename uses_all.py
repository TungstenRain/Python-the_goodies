"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 19: The Goodies in Think Python 2
    
    Note: Using Python 3.9.0
"""
def uses_all(word, required):
    """
        Determines if each letter in required is in the word

        word: string
        required: string

        return: boolean; True if each letter in required is in the word, False otherwise
    """
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_2(word, required):
    """
        Determines if each letter in required is in the word [Refactored using all]

        word: string
        required: string

        return: boolean; True if each letter in required is in the word, False otherwise
    """
    return all(letter in required for letter in word)

def main():
    word = "Monty"
    required = "Monty"
    required2 = "Python"

    print(uses_all(word, required))
    print(uses_all(word, required2))
    print(uses_all_2(word, required))
    print(uses_all_2(word, required2))

if __name__ == "__main__":
    main()