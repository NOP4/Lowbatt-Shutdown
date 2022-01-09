## Description
This program shutdown computer when low battery is reached. Found it safer that relying on some window manager setting.

## Installation
If necessary, install psutil: ```sudo pip install psutil```

Copy script where you like, for example in ```/usr/local/bin``` and set it as executable: ```chmod +x /usr/local/bin/lowbatt-shutdown.py```

Test program as **root** to ensure it can access battery value. It should display battery level.

Add program to crontab to run every minute: run ```crontab -e``` and add this line:
```* * * * * /usr/local/bin/lowbatt-shutdown.py```

## Configuration
Change this setting to your liking
```
LOWBATT_SHUTDOWN = 20
```
