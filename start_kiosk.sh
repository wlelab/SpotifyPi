#!/bin/bash

export DISPLAY=:0

while true;
do

  sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
  sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

  sleep 1

  /usr/bin/chromium-browser \
    --kiosk \
    --noerrdialogs\
    --disable-infobars \
    https://open.spotify.com

done