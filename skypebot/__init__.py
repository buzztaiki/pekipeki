#-*- coding:utf-8 -*-

__version__ = '0.1.0'
__author__ = '@shomah4a'
__license__ = 'LGPL'

import time


def main():
    u'''
    メイン
    '''

    from skypebot import skype

    skp = skype.init()

    while 1:
        time.sleep(100)


