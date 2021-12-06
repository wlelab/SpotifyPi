#!/bin/bash


apt -y install chromium-browser
apt -y install python3
apt -y install python3-pip
apt -y install libwidevinecdm0

pip3 install websockets
pip3 install pyautogui


mkdir -p /home/pi/bin
mkdir -p /home/pi/.config/lxsession/LXDE-pi/

cp -f spotifypi_service.py /home/pi/bin/
cp -f start_spotifypi_service.sh /home/pi/bin/
cp -f start_kiosk.sh /home/pi/bin/
cp -b autostart /home/pi/.config/lxsession/LXDE-pi/autostart

chmod 777 /home/pi/bin/spotifypi_service.py
chmod 777 /home/pi/bin/start_spotifypi_service.sh
chmod 777 /home/pi/bin/start_kiosk.sh
chmod 777 /home/pi/.config/lxsession/LXDE-pi/autostart
