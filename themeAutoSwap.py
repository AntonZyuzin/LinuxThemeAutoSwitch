#!usr/bin/python3.8
from datetime import datetime
import os
import time

lightDate_hours = 8
lightDate_mins = 0
darkDate_hours = 17
darkDate_mins = 37

lightDate = lightDate_hours * 60 + lightDate_mins
darkDate = darkDate_hours * 60 + darkDate_mins

light_gtk_theme = 'WhiteSur-light'
light_icon_theme = 'BigSur'
light_shell_theme = 'WhiteSur-light'
dark_gtk_theme = 'WhiteSur-dark'
dark_icon_theme = 'BigSur-black'
dark_shell_theme = 'WhiteSur-dark'

light_gtk_theme_command = 'gsettings set org.gnome.desktop.interface gtk-theme "' + light_gtk_theme + '"'
light_icon_theme_command = 'gsettings set org.gnome.desktop.interface icon-theme "' + light_icon_theme + '"'
light_shell_theme_command = 'gsettings set org.gnome.shell.extensions.user-theme name "' + light_shell_theme + '"'
dark_gtk_theme_command = 'gsettings set org.gnome.desktop.interface gtk-theme "' + dark_gtk_theme + '"'
dark_icon_theme_command = 'gsettings set org.gnome.desktop.interface icon-theme "' + dark_icon_theme + '"'
dark_shell_theme_command = 'gsettings set org.gnome.shell.extensions.user-theme name "' + dark_shell_theme + '"'


def checkSleepTime():
    times = nextEvent()
    nowTimeMin = times[0]
    nextEventTime = times[1]

    if nextEventTime < nowTimeMin:
        print('время ожидания: ', 1440 - nowTimeMin + nextEventTime, ' мин')
        time.sleep((1440 - nowTimeMin + nextEventTime) * 60)
    else:
        print('время ожидания: ', nextEventTime - nowTimeMin, ' мин')
        time.sleep((nextEventTime - nowTimeMin) * 60)


def nextEvent():
    nowTime = str(datetime.now())
    nextEventTime = lightDate
    nowTimeMin = int(nowTime[11:13]) * 60 + int(nowTime[14:16])
    if darkDate > lightDate > nowTimeMin:
        nextEventTime = lightDate
    elif lightDate == darkDate:
        print("TIME ERROR")
    elif darkDate > nowTimeMin > lightDate:
        nextEventTime = darkDate
    return [nowTimeMin, nextEventTime]


def update():
    checkSleepTime()
    if nextEvent() == lightDate:
        #        os.system(light_gtk_theme_command)
        #        os.system(light_icon_theme_command)
        #        os.system(light_shell_theme_command)
        os.system('notify-send "theme changed to light"')
        time.sleep(60)
    elif nextEvent() == darkDate:
        #        os.system(dark_gtk_theme_command)
        #        os.system(dark_icon_theme_command)
        #        os.system(dark_shell_theme_command)
        os.system('notify-send "theme changed to dark"')
        time.sleep(60)
    update()


update()

