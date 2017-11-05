#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

class Logger:
  """
  Class : Logger

  describ :
  Logger is a pimp logging which build on
  logging and colorlog librairy

  5 level's message exist with different color:
  DEBUG    | A quirky message only developers care about
  INFO     | Curious users might want to know this
  WARNING  | Something is wrong and any user should be informed
  ERROR    | Serious stuff, this is red for a reason
  CRITICAL | OH NO everything is on fire

  colors:
  red
  cyan
  green
  black
  white
  yellow
  blue
  purple

  mode:
  Release
  Debub
  """

  # Logger list color exist
  loggerColorList = ['red', 'cyan', 'green', 'black', 'white', 'yellow', 'blue', 'purple']

  # Logger list mode exist
  loggerModeList = ['Release', 'Debug']

  def __init__(self, loggerName, loggerInfoColor='green', loggerMode='Release'):
    """
    Constructor
    :param loggerName str: logger name
    :param loggerInfoColor str: logger color
    :param loggerMode str: logger mode
    """
    if loggerMode == 'Release':
        self.loggerLevel = logging.INFO
    else:
      self.loggerLevel = logging.DEBUG
    logging.root.setLevel(self.loggerLevel)
    formatter = ColoredFormatter(
          "%(white)s%(asctime)s%(reset)s [%(log_color)s%(name)s%(reset)s] %(log_color)s%(levelname)-8s%(reset)s . %(log_color)s%(message)s%(reset)s",
          datefmt=None,
          reset=True,
          log_colors={
              'DEBUG':    loggerInfoColor,
              'INFO':     loggerInfoColor,
              'WARNING':  'yellow',
              'ERROR':    'red',
              'CRITICAL': 'red,bg_white',
          },
          secondary_log_colors={},
          style='%'
    )

    self.stream = logging.StreamHandler()
    self.stream.setLevel(self.loggerLevel)
    self.stream.setFormatter(formatter)
    self.log = logging.getLogger(loggerName)
    self.log.setLevel(self.loggerLevel)
    self.log.addHandler(self.stream)

    self.loggerInfoColor = loggerInfoColor
    self.loggerMode = loggerMode

  def logFile(self, handlerPath, sizeFile=1000000):
    """
    Active writing log
    :param handlerPath str: log path
    :param sizeFile int: size of log file in Byte
    """
    self.fileHandler = RotatingFileHandler(handlerPath, 'a', sizeFile, 1)
    self.fileHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s . %(message)s')
    self.fileHandler.setFormatter(formatter)
    self.log.addHandler(self.fileHandler)

  def newColor(self, loggerInfoColor='green'):
    """
    Logger color change
    :param loggerInfoColor str: logger color
    """
    self.loggerInfoColor = loggerInfoColor
    formatter = ColoredFormatter(
        "%(white)s%(asctime)s%(reset)s [%(log_color)s%(name)s%(reset)s] %(log_color)s%(levelname)-8s%(reset)s . %(log_color)s%(message)s%(reset)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    self.loggerInfoColor,
            'INFO':     self.loggerInfoColor,
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    self.stream.setFormatter(formatter)
    self.log.addHandler(self.stream)

  def setMode(self, loggerMode='Release'):
    """
    Logger mode change
    :param loggerMode str: logger mode
    """
    if loggerMode == 'Release':
        self.loggerLevel = logging.INFO
    else:
        self.loggerLevel = logging.DEBUG
    self.loggerMode = loggerMode
    self.log.setLevel(self.loggerLevel)

  def info(self, msg, *args, **kwargs):
    """
    Info Message
    """
    self.log.info(msg, *args, **kwargs)

  def debug(self, msg, *args, **kwargs):
    """
    Debug Message
    """
    self.log.debug(msg, *args, **kwargs)

  def warn(self, msg, *args, **kwargs):
    """
    Warn Message
    """
    self.log.warn(msg, *args, **kwargs)

  def error(self, msg, *args, **kwargs):
    """
    Error Message
    """
    self.log.error(msg, *args, **kwargs)

  def critical(self, msg, *args, **kwargs):
    """
    Critical Message
    """
    self.log.critical(msg, *args, **kwargs)
