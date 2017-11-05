#!/usr/bin/python

# """Created on 29 July 2012 @author : Benoit Brisset
# """

# class classDeTest(object):
#   # """
#   # Short doc for the class concern
#   # """

#   def function1(self, arg1, arg2):
#     """return (arg1 / arg2) + arg3

#     Explication de ce que fait la fonction
#     """
#     return (arg1 / arg2) + arg3

def functionAlone1(arg):
  """
  test function doc
  """
  return 0


if __name__ == '__main__':
  import doctest
  doctest.testmod()