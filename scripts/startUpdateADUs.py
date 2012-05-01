#! /usr/bin/env python

import sys
import logging
import logging.handlers

try:
  import config.updateadus as configModule
except ImportError:
  import updateadus as configModule

import socorro.lib.ConfigurationManager as configurationManager
import socorro.cron.updateADUs as updateADUs
import socorro.lib.util as sutil

try:
  config = configurationManager.newConfiguration(
      configurationModule=configModule, applicationName="Update ADUs 0.1")
except configurationManager.NotAnOptionError, x:
  print >>sys.stderr, x
  print >>sys.stderr, "for usage, try --help"
  sys.exit()

logger = logging.getLogger("updateADUs")
logger.setLevel(logging.DEBUG)

sutil.setupLoggingHandlers(logger, config)
sutil.echoConfig(logger, config)

try:
  updateADUs.update_adus(config)
finally:
  logger.info("done.")

