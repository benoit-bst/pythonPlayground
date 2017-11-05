#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  describ : Tests du Logger

  date : 15/07/2015

  author : bbst
"""

import os, sys
lib_path = os.path.abspath(os.path.join('../src'))
sys.path.append(lib_path)

import toolkit

log = toolkit.Logger('LoggerTests', 'green')
log.logFile('/local/test.log', 10000)

log.debug("A quirky message only developers care about")
log.info("Curious users might want to know this")
log.warn("Something is wrong and any user should be informed")
log.error("Serious stuff, this is red for a reason")
log.critical("OH NO everything is on fire")

log.newColor('red')
log.debug("red message")
log.info("red message")

log.newColor('cyan')
log.debug("cyan message")
log.info("cyan message")

log.newColor('green')
log.debug("green message")
log.info("green message")

log.newColor('black')
log.debug("black message")
log.info("black message")

log.newColor('white')
log.debug("white message")
log.info("white message")

log.newColor('yellow')
log.debug("yellow message")
log.info("yellow message")

log.newColor('blue')
log.debug("blue message")
log.info("blue message")

log.info("Passage de Release")
log.setMode('Release')
log.debug("Debug message")
log.info("Info message")