import os
import functools
import logging
import datetime

DEFAULT_LOG_PATH = os.path.abspath('..')+'/logs/logs.log'

logger = logging.getLogger('gradient_logger')
logging.basicConfig(filename=DEFAULT_LOG_PATH,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )


class GradientLogger(object):
    def __init__(self):
        self.logger = logging.getLogger('gradient_logger')

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.debug("{0} - {1} - {2} - {3}".format(
                    fn.__name__, args, kwargs, datetime.datetime.now()
                ))
                result = fn(*args, **kwargs)
                # self.logger.debug(result)
                return result
            except Exception as ex:
                self.logger.debug("Exception {0}".format(ex))
                raise ex
            return result
        return decorated

