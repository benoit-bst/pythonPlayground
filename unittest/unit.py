#!/usr/bin/python

import unittest

class classTests1(unittest.TestCase):

  def test1(self):
    self.assertEqual('FOO','FOO')

  def test2(self):
    self.assertTrue(True)
    self.assertFalse(False)

class classTests2(unittest.TestCase):

  def test1(self):
    self.assertEqual('FOO','FOO')

  def test2(self):
    self.assertTrue(True)
    self.assertFalse(False)

if __name__ == '__main__':
  unittest.main(verbosity=2)