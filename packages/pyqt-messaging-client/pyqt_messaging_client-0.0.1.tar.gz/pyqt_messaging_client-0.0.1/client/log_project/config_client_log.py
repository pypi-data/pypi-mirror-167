import sys
import os
import logging

from Project_to_OOP.common.variables import ENCODING, LOGGING_LEVEL

sys.path.append('../')

CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH+'/logs/', 'client.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.FileHandler(PATH, encoding=ENCODING)
LOG_FILE.setFormatter(CLIENT_FORMATTER)

logger = logging.getLogger('client')
logger.addHandler(STREAM_HANDLER)
logger.addHandler(LOG_FILE)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Критическая ошибка')
    logger.error('Ошибка')
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')