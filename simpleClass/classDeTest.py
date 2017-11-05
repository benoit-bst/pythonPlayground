import os
import sys

class ClassDeTest(object):
  """docstring for ClassDeTest"""

  def __init__(self, val1, val2):
    self.val1 = val1
    self.val2 = val2

  # fonction 1
  def function1(self, val1=None):
    self.val1 = val1
    print "function test"
