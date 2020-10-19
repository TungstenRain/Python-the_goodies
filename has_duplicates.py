"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 19: The Goodies in Think Python 2
    
    Note: Using Python 3.9.0
"""
def has_duplicates(a_list):
    """
        Determine if a list has duplicates

        a_list: list

        return: boolean; True if has duplicates, false otherwise
    """
    # initialize a list and sort it. This prevents modifying the original list
    b_list = list(a_list)
    b_list.sort()

    # check for adjacent elements that are equal
    for i in range(len(b_list) - 1):
        if b_list[i] == b_list[i+1]:
            return True
    return False

def has_duplicates_2(a_list):
    """
        Determine if a list has duplicates [using a dictionary]

        a_list: list

        return: boolean; True if has duplicates, false otherwise
    """
    d = {}
    for x in a_list:
        if x in d:
            return True
        d[x] = x
    return False

def has_duplicates_3(a_list):
    """
        Determine if a list has duplicates [using a set]

        a_list: list

        return: boolean; True if has duplicates, false otherwise
    """
    return len(set(a_list) < len(a_list))

    