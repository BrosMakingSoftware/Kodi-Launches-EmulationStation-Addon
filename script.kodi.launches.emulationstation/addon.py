import xbmc
import xbmcaddon
import xbmcgui

import os.path
import subprocess

__addon__ = xbmcaddon.Addon('script.kodi.launches.emulationstation')
__addonId__ = __addon__.getAddonInfo('id')
__addonName__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__localizedMessages__ = __addon__.getLocalizedString


def log(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s:v%s] %s' % (__addonId__, __version__, message.encode('utf-8')), level)


log("Starting Kodi-Launches-EmulationStation-Addon")


emulationstation_exec = __addon__.getSetting('emulationstation_exec').decode('utf-8')


if not os.path.isfile(emulationstation_exec):
   xbmcgui.Dialog().ok(__localizedMessages__(32000), __localizedMessages__(32001) ,__localizedMessages__(32002), __localizedMessages__(32003) + emulationstation_exec)
   xbmcgui.Dialog().ok(__localizedMessages__(32004), __localizedMessages__(32005))
   log("EmulationStation executable was not found on the specified location: " + emulationstation_exec, xbmc.LOGERROR)

else:
    log("Starting EmulationStation executable")
    subprocess.call([emulationstation_exec])
