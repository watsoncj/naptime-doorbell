import os
from flask import Flask, request

ctrlPath = "/home/pi/naptime-doorbell/ctrl"
try:
    os.mkfifo(ctrlPath)
except OSError:
    pass


app = Flask(__name__)

@app.route("/enable", methods=['POST'])
def enable():
  ctrl = open(ctrlPath, 'w')
  ctrl.write('on\n')
  ctrl.close()

@app.route("/disable", methods=['POST'])
def disable():
  ctrl = open(ctrlPath, 'w')
  ctrl.write('off\n')
  ctrl.close()

if __name__ == "__main__":
    app.run()
