'''
Created on June 28, 2016

@author: Jay <smile665@gmail.com>
'''

import logging


class PhotoLogger:
    ''' The common logger for this project. '''

    logger = None

    def __init__(self, logfile='photo.log', level=logging.INFO,
                 name='photo-face'):
        FORMAT = '%(asctime)-15s  %(message)s'
        logging.basicConfig(filename=logfile, format=FORMAT, level=level)
        self.logger = logging.getLogger(name=name)

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    mylogger = PhotoLogger().getLogger()
    mylogger.info('hello')
