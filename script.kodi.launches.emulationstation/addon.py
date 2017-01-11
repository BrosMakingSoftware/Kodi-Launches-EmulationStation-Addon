import xbmcaddon
import xbmcgui

import os.path
import subprocess

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('name')
emulationstation_exec = addon.getSetting('emulationstation_exec').decode('utf-8')


if not os.path.isfile(emulationstation_exec):
   xbmcgui.Dialog().ok("Error launching EmulationStation", "The EmulationStation executable was not found." ,"Please change its location on the Addon-Configure section.", "File not found: " + emulationstation_exec)
   xbmcgui.Dialog().ok("Is EmulationStation installed?", "Please check that EmulationStation is installed and configured on this system before using this launcher, for instructions and downloads go to http://emulationstation.org/")

else:
    subprocess.call([emulationstation_exec])
