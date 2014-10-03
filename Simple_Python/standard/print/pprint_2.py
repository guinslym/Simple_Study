#coding:utf8
from pprint import pformat
import logging

data=[(1,{"a":"1","b":"2","c":"3"}),
      (2, {"d":"4","e":"5","f":"6","g":"7",
          "h":"8","i":"9"
          }),
      (3, {"d":"4","e":"5","f":"6","g":"7",
          "h":"8","i":"9"
          })
          ]
logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)-8s %(message)s",
                    )
logging.debug("Logging pformatted data")
formatted=pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
