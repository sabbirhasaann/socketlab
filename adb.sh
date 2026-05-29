#!/bin/bash
TARGET_IP="192.168.0.101"
CONNECT_PORT="36921"
REVERSE_PORT="36921"

adb devices
adb connect "${TARGET_IP}:${CONNECT_PORT}"
adb -s "$TARGET_IP:${REVERSE_PORT}" reverse tcp:8000 tcp:8000


# # Define a single variable for the full address
# DEVICE_ADDRESS="192.168.0.101:33452"

# # Use the variable
# adb devices
# adb connect "${DEVICE_ADDRESS}"
# adb -s "${DEVICE_ADDRESS}" reverse tcp:8000 tcp:8000

# chmod +x adb.sh
# That output just means the script was already executable!
# Because it already had the correct permissions (0775 means 
# you and your group have read, write, and execute permissions), 
# chmod simply kept it exactly as it was rather than changing anything.