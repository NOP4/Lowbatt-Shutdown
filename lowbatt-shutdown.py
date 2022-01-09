#!/usr/bin/env python3
import psutil
import os

# Source: https://github.com/NOP4/Lowbatt-Shutdown.git

#####################################
# WARNING                           #
# THIS PROGRAM NEEDS TO RUN AS ROOT #
#####################################
# This program shutdown computer when low battery is reached

# INSTALLATION
# If necessary, install psutil: sudo pip install psutil
# Copy script where you like, for example /usr/local/bin and set it as executable: chmod +x /usr/local/bin/lowbatt-shutdown.py
# Test program as root to ensure it can access battery value. It should display battery level.
# Add program to crontab to run every minute: run "crontab -e" and add this line (removing the starting #):
# * * * * * /usr/local/bin/lowbatt-shutdown.py

# CONFIGURATION
# Change this setting to your liking
LOWBATT_SHUTDOWN = 20

# DO NOT CHANGE PAST THIS POINT
battery = psutil.sensors_battery()

print("Current charge: " + str(int(battery.percent)) + "%")

if (battery.percent < LOWBATT_SHUTDOWN):
    os.system("shutdown /s /t 1")

