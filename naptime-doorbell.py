#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import signal
import os

ctrlPath = "/home/pi/naptime-doorbell/ctrl"
try:
    os.mkfifo(ctrlPath)
except OSError:
    pass

CHANNEL = 4

def clean_exit(signal, frame):
  GPIO.cleanup(CHANNEL)
  sys.exit(0)
signal.signal(signal.SIGINT, clean_exit)

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)
GPIO.output(CHANNEL, 0) # initial state is enabled

while True:
    rp = open(ctrlPath, 'r')
    response = rp.read()
    if response == 'on\n':
      print "ctrl: enabled"
      GPIO.output(CHANNEL, 0)
    else:
      print "ctrl: disabled"
      GPIO.output(CHANNEL, 1)
