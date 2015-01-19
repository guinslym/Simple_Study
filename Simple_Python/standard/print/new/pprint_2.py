#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pformat
from pprint_data import data
import logging

logging.basicConfig(level=logging.DEBUG,
    format="%(levelname)-8s %(message)s",
    )
logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())