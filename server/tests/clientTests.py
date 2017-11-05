#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  describ : Server test

  date : 15/07/2015

  author : bbst
"""

import os, sys
lib_path = os.path.abspath(os.path.join('../'))
sys.path.append(lib_path)

import logging
import socket

from server import *

def testClient():

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("", 1111))

  a = 0
  while 1:
    r = s.recv(9999999)
    print("Receive server message : %s" %r)
    a = a + 1
    if a == 20:
      s.close()
      break

#################################################
if __name__ == '__main__':

  # Create logger
  logger = logging.getLogger('serverTests')
  formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s')
  stream = logging.StreamHandler()
  stream.setLevel(logging.DEBUG)
  stream.setFormatter(formatter)
  logger.addHandler(stream)
  logger.setLevel(logging.DEBUG)

  logger.info("Running client")
  testClient()
  logger.info("Stoping client")