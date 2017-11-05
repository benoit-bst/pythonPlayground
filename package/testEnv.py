#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.stdout = sys.stderr
VIRTUALENV = "/tmp/data/app"
PROJECTDIR = os.path.dirname(__file__)
activate_this = os.path.join(VIRTUALENV, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECTDIR)
print("PROJECTDIR %s " %PROJECTDIR)
print("PROJECTDIR %s " %__file__)