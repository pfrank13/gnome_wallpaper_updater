#!/usr/bin/env bash

wget -O /tmp/latest_wallpaper "$1"

# export DBUS_SESSION_BUS_ADDRESS environment variable
PID=$(pgrep -u pfrank gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

gsettings set org.gnome.desktop.background picture-options "$2"
gsettings set org.gnome.desktop.background picture-uri "file:///tmp/latest_wallpaper"