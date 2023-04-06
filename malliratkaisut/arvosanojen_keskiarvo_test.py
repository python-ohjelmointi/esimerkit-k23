'''
>>> from arvosanojen_keskiarvo import arvosanojen_keskiarvo

>>> arvosanojen_keskiarvo([1, 2])
1.5

>>> arvosanojen_keskiarvo([1, 3, 4, 5]) == 3.25  # funktion täytyy palauttaa arvo
True

>>> arvosanojen_keskiarvo([0, 1, 0, 3, 0, 4, 0, 5])
3.25
'''

import doctest
doctest.testmod(verbose=True)
