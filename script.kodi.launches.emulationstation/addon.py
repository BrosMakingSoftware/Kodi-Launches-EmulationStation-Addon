# Kodi modules
import xbmc
import xbmcaddon
import xbmcgui

# Python modules
import platform
import os.path
import subprocess
import json

# Getting constants
__addon__ = xbmcaddon.Addon('script.kodi.launches.emulationstation')
__addonId__ = __addon__.getAddonInfo('id')
__addonName__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__localizedMessages__ = __addon__.getLocalizedString


# Method to print logs on a standard way
def log(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s:v%s] %s' % (__addonId__, __version__, message.encode('utf-8')), level)
# end of log

# Starting the Addon
log("Starting " + __addonName__)

# Var to hold  the path where the EmulationStation executable is
executable = ""

# Var to hold the path where Xterm for linux installations
xterm = ""

# Var to hold launch command
launch = []

# We are going to ask on which platform this is running so we can load the default executable location for it
if platform.system() == "Windows":
    # If the platform is Windows
    executable = __addon__.getSetting('windowsExecutable').decode('utf-8')
    log("Loaded Windows executable location from Settings: " + executable)
    launch = [executable]
else:
    # Otherwise it is Linux because EmulationStation currently runs on Windows, Debians and RetroPie
    executable = __addon__.getSetting('linuxExecutable')
    log("Loaded Linux executable location from Settings: " + executable)
    xterm = __addon__.getSetting('xtermExecutable')
    log("Load xterm executable location from Settings: " + xterm)
    # Verify that the xterm path is still valid
    if not os.path.isfile(xterm):
        # This message prints something like: Xterm executable was not found, go to Addon-Configure and change it
        xbmcgui.Dialog().ok(__localizedMessages__(32013), __localizedMessages__(32014) ,__localizedMessages__(32015), __localizedMessages__(32003) + xterm)
        # Log the error
        log("xterm executable was not found on this specified location: " + xterm, xbmc.LOGERROR)
    launch = [xterm, "-fullscreen" ,"-e", executable]
# When you choose an executable from Kodi when changing Addon Settings, Kodi forces you to select an executable that exists, but we want to validate
# if the executable exists anyways, just in case the default value doesn't work or the settings were manually changed
if not os.path.isfile(executable):
    # This message prints something like: EmulationStation executable was not found, go to Addon-Configure and change it
    xbmcgui.Dialog().ok(__localizedMessages__(32000), __localizedMessages__(32001) ,__localizedMessages__(32002), __localizedMessages__(32003) + executable)
    # This message prints something like: Please check that EmulationStation is installed
    xbmcgui.Dialog().ok(__localizedMessages__(32004), __localizedMessages__(32005))
    # Log the error
    log("EmulationStation executable was not found on this specified location: " + executable, xbmc.LOGERROR)

else:
    # Var to hold current display sleep timer
    displayoff = ""

    # Var to hold current computer sleep timer
    shutdowntime = ""

    log("Starting EmulationStation executable: " + executable)
    if __addon__.getSetting('powersaving') == "true":
        log("Turning off powersavings")
        displayoff = str(json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"powermanagement.displaysoff"},"id":1}'))["result"]["value"])
        log("Current display off time: " + displayoff)
        shutdowntime = str(json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"powermanagement.shutdowntime"},"id":1}'))["result"]["value"])
        log("Current shutdown time: " + shutdowntime)
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.displaysoff","value":0},"id":1}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.shutdowntime","value":0},"id":1}')
    if __addon__.getSetting('workaround') == "true":
        log("Applying workaround for windows stacking order")
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method": "Input.ExecuteAction", "params": {"action":"togglefullscreen"},"id":1}')
    subprocess.call(launch)
    if __addon__.getSetting('powersaving') == "true":
        log("Returning powersaving settings to inital value")
        # Before reenabling powersavings, send Down key to Kodi to wake up. Otherwise computer goes to sleep as soon as parameter is set
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
        
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.displaysoff","value":'+displayoff+'},"id":1}')
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.shutdowntime","value":'+shutdowntime+'},"id":1}')
    if __addon__.getSetting('workaround') == "true":
	log("Removing workaround for windows stacking order")
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method": "Input.ExecuteAction", "params": {"action":"togglefullscreen"},"id":1}')
