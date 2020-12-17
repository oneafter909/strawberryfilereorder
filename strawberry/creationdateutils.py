#!/usr/bin/python3
import os
import time
import datetime

class Date:
    def getDateFromFile(path):
        x = time.ctime(os.path.getmtime(path))
        return x

    def getMonth(path):
        x = time.ctime(os.path.getmtime(path))
        y=datetime.datetime.strptime(x, '%a %b %d %H:%M:%S %Y')
        return y.month
    def getDay(path):
        x = time.ctime(os.path.getmtime(path))
        y=datetime.datetime.strptime(x, '%a %b %d %H:%M:%S %Y')
        return y.day
    def getYear(path):
        x = time.ctime(os.path.getmtime(path))
        y=datetime.datetime.strptime(x, '%a %b %d %H:%M:%S %Y')
        return y.year
