# Naptime Doorbell

Raspberry Pi project to disable a doorbell during naptime.

Hardware:
Raspberry Pi (Model A used for this project but any will work)
Jumper wires (female to female type)
5v relay ([this](http://www.amazon.com/SunFounder-Channel-Shield-Arduino-Raspberry/dp/B00E0NTPP4/) one works)

![component image](naptime-doorbell.jpg)

```
git clone git@github.com:watsoncj/naptime-doorbell.git
screen sudo naptime-doorbell/naptime-doorbell.py
# use ctrl-a ctrl-d to exit
# `screen -r` to re-attach
```

Example Crontab:

```
# m h  dom mon dow   command
30 12 * * * /home/pi/naptime-doorbell/disable-doorbell.py
30 16 * * * /home/pi/naptime-doorbell/enable-doorbell.py
```

