#!/usr/bin/python

class ClassTests1():

  def multTest1(self, val1, val2):
    ''' return multiplication

    Examples:

    >>> a = 1
    >>> b = 2
    >>> class1 = ClassTests1()
    >>> c = class1.multTest1(a, b)
    >>>
    '''

    return val1 * val2

  def addTest2(self, val1, val2):
    ''' return addition

    Examples:

    >>> a = 1
    >>> b = 2
    >>> class1 = ClassTests1()
    >>> c = class1.addTest2(a, b)
    >>>
    '''

    return val1 + val2

def _test():
  import doctest
  doctest.testmod()

if __name__ == "__main__":
  _test()
