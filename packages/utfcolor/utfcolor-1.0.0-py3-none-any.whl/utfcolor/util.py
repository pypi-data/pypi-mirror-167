import logging
from datetime import datetime

def createFilename()->str:
    '''create a unique filename from the given parameters and time'''
    return(datetime.now().strftime('%d%m%y%H%M%S') + ".png")

def getLogger(name: str, level: str) -> logging.Logger:
    '''create a new logging object'''
    logging.basicConfig(level=level)
    return(logging.getLogger(name))