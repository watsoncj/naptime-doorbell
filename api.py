#!/usr/bin/python
import RPi.GPIO as GPIO
import os
from flask import Flask, request, send_from_directory

CHANNEL = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)

ctrlPath = "/home/pi/naptime-doorbell/ctrl"
try:
  os.mkfifo(ctrlPath)
except OSError:
  pass

app = Flask(__name__)

@app.route("/api/enable", methods=['POST'])
def enable():
  ctrl = open(ctrlPath, 'w')
  ctrl.write('on\n')
  ctrl.close()
  return 'enabled'

@app.route("/api/disable", methods=['POST'])
def disable():
  ctrl = open(ctrlPath, 'w')
  ctrl.write('off\n')
  ctrl.close()
  return 'disabled'

@app.route("/api/status", methods=['GET'])
def status():
  status = GPIO.input(CHANNEL)
  if status:
    return 'disabled'
  else:
    return 'enabled'

@app.route('/')
def app_index():
  return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def app_public(path):
  return send_from_directory('public', path)

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
