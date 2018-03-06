# #-*- coding: utf-8 -*-

import logging
import logging.handlers
import os



def get_logger():
    print "== import GW log module =="
    logger = logging.getLogger('gw_logger')
    fileMaxByte = 1024 * 1024 * 100 #       100MB   로그 파일 크기
    fileHandler = logging.handlers.RotatingFileHandler('./log/local_gate_way.log', maxBytes=fileMaxByte, backupCount=10)
    streamHandler = logging.StreamHandler()
    fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    fileHandler.setFormatter(fomatter)


    # try:
    exec_status = os.environ['exec_status']

    # except Exception as e:
    #     print("exec_status ");
    #     pass





    if  exec_status == 'fore':
        logger.addHandler(streamHandler)
        streamHandler.setFormatter(fomatter)





    return logger

MY_LOGGER = get_logger()

def Ilog(message):
    MY_LOGGER.info(message)

def Dlog(message):
    print MY_LOGGER
    MY_LOGGER.debug(message)

def Wlog(message):
    MY_LOGGER.warning(message)










