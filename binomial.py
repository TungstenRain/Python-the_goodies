"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 19: The Goodies in Think Python 2
    
    Note: Using Python 3.9.0
"""
def binomial_coeff(n, k):
    """
        Compute the binomial coefficient "n choose k".
        
        n: number of trials
        k: number of successes
        
        return: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

def binomial_coefficient(n, k):
    """
        Compute the binomial coefficient "n choose k". [refactored to use nested conditional expressions]
        
        n: number of trials
        k: number of successes
        
        return: int
    """
    return binomial_coefficient(n-1, k) + binomial_coefficient(n-1, k-1) if k != 0 and n != 0 else (1 if k == 0 else 0)


def main():
    print(binomial_coeff(17, 8))
    print(binomial_coefficient(17, 8))

if __name__ == "__main__":
    main()