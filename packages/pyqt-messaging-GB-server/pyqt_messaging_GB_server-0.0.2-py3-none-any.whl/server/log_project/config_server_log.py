import sys
import os
import logging
import logging.handlers
from Project_to_OOP.common.variables import LOGGING_LEVEL, ENCODING

sys.path.append('../')

SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH+'/logs/', 'server.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding=ENCODING, interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

logger = logging.getLogger('server_dist')
logger.addHandler(STREAM_HANDLER)
logger.addHandler(LOG_FILE)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Критическая ошибка')
    logger.error('Ошибка')
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')
