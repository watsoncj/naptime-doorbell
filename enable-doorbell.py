#!/usr/bin/python
import os

ctrlPath = "/home/pi/naptime-doorbell/ctrl"
try:
    os.mkfifo(ctrlPath)
except OSError:
    pass

ctrl = open(ctrlPath, 'w')
ctrl.write('on\n')
ctrl.close()
