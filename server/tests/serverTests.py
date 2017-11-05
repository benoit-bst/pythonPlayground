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

from server import *

def testServer():
  classServer = Server("160.111.65.62", 1111, 10)
  classServer.run()

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

  logger.info("Running server")
  testServer()
  logger.info("Stoping server")