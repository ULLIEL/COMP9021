'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''

import sys
from math import sqrt
def prime(n) :
    primes = [True]*(n+1)
    p = 2
    while p*p < n+1 :
        if primes[p] :
            for i in range(p*2,n+1,p) :
                primes[i] = False
        p += 1
    
    primes = [e for e in range(2,n+1) if primes[e]]
    return primes

def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number beween 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number beween 4 and 4.
    >>> f(14, 16)
    There is no prime number beween 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    '''
    
    R = []

    if a == b:
        if a == 1 or a == 2:
            print(f'There is a unique prime number beween {a} and {b}.') 
        elif a % 2 == 0:
            print(f'There is no prime number beween {a} and {b}.')
        else:
            print(f'There is a prime number beween {a} and {b}.')    
    else:
        for item in prime(b):
            if a <= item and b>=item:
                R.append(item)        

        if R == []:
            print(f'There is no prime number beween {a} and {b}.')
        else:
            print(f'There are {len(R)} prime numbers between {a} and {b}.')



if __name__ == '__main__':
    import doctest
    doctest.testmod()
