#!/usr/bin/python

import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

print("%s" %config.sections())

options = config.options(config.sections()[0])
for option in options:
  print("%s = %s" %(option, config.get(config.sections()[0], option)))