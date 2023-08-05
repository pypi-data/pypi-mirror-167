import logging

class Logger(object):
    def __init__(self, name='logger', level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

class StreamLogger(Logger):
    def __init__(self, name='logger', level=logging.DEBUG):
        super().__init__(name, level)
        
        sh = logging.StreamHandler()
        self.logger.addHandler(sh)

class FileLogger(Logger):
    def __init__(self, name='logger', level=logging.DEBUG):
        super().__init__(name, level)

        fh = logging.FileHandler('%s.log' % name, 'w')
        self.logger.addHandler(fh)