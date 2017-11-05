#!/usr/bin/python
# -*- coding: utf-8 -*-

# = env in bash
import os

if __name__ == '__main__':

	for key, value in os.environ.items():
		print("key %s - value %s" %(key, value))
