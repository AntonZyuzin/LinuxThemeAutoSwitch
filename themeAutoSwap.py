#!usr/bin/python3.8
from datetime import datetime
import os
import time

lightDate_hours = 8
lightDate_mins = 0
darkDate_hours = 23
darkDate_mins = 0

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
    nowTimeMin, nextEventTime = times[0], times[1]
    if nextEventTime < nowTimeMin:
        print('время ожидания: ', 1440 - nowTimeMin + nextEventTime, ' мин')
        time.sleep((1440 - nowTimeMin + nextEventTime) * 60)
    else:
        print('время ожидания: ', nextEventTime - nowTimeMin, ' мин')
        time.sleep((nextEventTime - nowTimeMin) * 60)
    update(nextEventTime)


def nowTheme():
    if darkDate > realTime() > lightDate:
        switch(light_gtk_theme_command, light_icon_theme_command, light_shell_theme_command)
        os.system('notify-send "theme changed to light"')

    else:
        switch(dark_gtk_theme_command, dark_icon_theme_command, dark_shell_theme_command)
        os.system('notify-send "theme changed to dark"')

def realTime():
    nowTime = str(datetime.now())
    print(nowTime)
    nowTimeMin = int(nowTime[11:13]) * 60 + int(nowTime[14:16])
    return nowTimeMin

def nextEvent():
    nowTimeMin = realTime()
    nextEventTime = lightDate
    if lightDate > nowTimeMin:
        nextEventTime = lightDate
    elif darkDate > nowTimeMin > lightDate:
        nextEventTime = darkDate
    return [nowTimeMin, nextEventTime]


def switch(cmd1, cmd2, cmd3):
    # os.system(cmd1)
    # os.system(cmd2)
    # os.system(cmd3)
    time.sleep(60)


def update(nextEventTime):
    if nextEventTime == lightDate:
        os.system('notify-send "theme changed to light"')
        switch(light_gtk_theme_command, light_icon_theme_command, light_shell_theme_command)
    elif nextEventTime == darkDate:
        os.system('notify-send "theme changed to dark"')
        switch(dark_gtk_theme_command, dark_icon_theme_command, dark_shell_theme_command)
    checkSleepTime()


if darkDate > lightDate and darkDate != lightDate:
    nowTheme()
    checkSleepTime()
else:
    print("TIME ERROR")
