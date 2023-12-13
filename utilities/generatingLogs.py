import logging
#C:/Users/Srikanth Chelukala/PycharmProjects/practNinja
# logging.basicConfig(filename="../Logs/logfile.log.py",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
# log=logging.getLogger()
# log.info("this is our first log")

def log():
    logging.basicConfig(filename="../Logs/logfile.log.py",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
    logger=logging.getLogger()
    return logger

logger=log()
logger.info('info message give here')
