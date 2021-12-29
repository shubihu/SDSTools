import logging


class LogMixin(object):
    @property
    def logger(self):
        name = '.'.join([self.__module__, self.__class__.__name__])
        FORMAT = '%(name)s:%(levelname)s:%(message)s'
        logging.basicConfig(format=FORMAT, level=logging.DEBUG)
        logger = logging.getLogger(name)
        return logger