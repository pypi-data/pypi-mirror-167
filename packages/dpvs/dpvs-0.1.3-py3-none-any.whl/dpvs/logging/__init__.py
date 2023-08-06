import logging


__all__ = ['get_logger']

loggers = {}

def get_logger(name=None, message_only=True, formatter=None, level='INFO', path=''):
    if name in loggers: return loggers.get(name)
    logger = logging.getLogger(name or __name__)
    logger.setLevel(logging._nameToLevel[level])
    if message_only:
        if formatter is not None:
            formatter = logging.Formatter(formatter)
        else:
            formatter = logging.Formatter('%(name)s :: %(asctime)s ::  %(message)s', "%H:%M")
        if path:
            log = logging.FileHandler(path,mode='w')
        else:
            log = logging.StreamHandler()
        log.setFormatter(formatter)
        logger.addHandler(log)
        # propagate=False: disable message spawned by child logger pass to parent logger
        logger.propagate = False        
        loggers[name] = logger
    return logger
