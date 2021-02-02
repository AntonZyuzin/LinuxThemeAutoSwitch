#!usr/bin/python3.8
from datetime import datetime, date
import os
import time

lightDate_hours = 7
lightDate_mins = 0
darkDate_hours = 20
darkDate_mins = 0

lightDate = [15, 15]
darkDate = [15, 20]
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
    nowTime = str(datetime.now())
    hours = int(nowTime[11:13])
    min = int(nowTime[14:16])
    nextEventTime = []
    if lightDate[0] < darkDate[0]:
        nextEventTime = lightDate
    elif lightDate[0] == darkDate[0]:
        if lightDate[1] < darkDate[1]:
            nextEventTime = lightDate
        elif lightDate[1] == darkDate[1]:
            print("TIME ERROR")
        elif lightDate[1] > darkDate[1]:
            nextEventTime = darkDate
    elif lightDate[0] > darkDate[0]:
        nextEventTime = darkDate
    nextEventTimeMin = nextEventTime[0] * 60 + nextEventTime[1]
    nowTimeMin = hours * 60 + min  # переводим время в минуты, чтобы посчитать время то следующей смены тем
    waitingTime = nextEventTimeMin - nowTimeMin
    if nextEventTimeMin < nowTimeMin:
        waitingTime += 1440
    print(waitingTime)
    return waitingTime * 60


def update():
    nowTime = str(datetime.now())
    hours = int(nowTime[11:13])
    min = int(nowTime[14:16])
    nowDate = [hours, min]
    if nowDate == lightDate:
        #        os.system(light_gtk_theme_command)
        #        os.system(light_icon_theme_command)
        #        os.system(light_shell_theme_command)
        os.system('notify-send "theme changed to light"')
    elif nowDate == darkDate:
        #        os.system(dark_gtk_theme_command)
        #        os.system(dark_icon_theme_command)
        #        os.system(dark_shell_theme_command)
        os.system('notify-send "theme changed to dark"')
    print(hours, min)
    time.sleep(checkSleepTime())
    update()


update()
