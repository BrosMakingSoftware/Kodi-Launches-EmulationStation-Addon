# Kodi Launches EmulationStation Addon
Addon for Kodi to launch EmulationStation.

## Usage
Use this Addon on Kodi if you want to launch EmulationStation from it using a nice interface created with original images taken from the program itself and games. It works on any platform where Kodi and EmulationStation can be installed (Linux, Windows, MacOS).

**Note:**  
This Addon is just a launcher, so it assumes that you already have installed and configured EmulationStation on your system. It will not assist you to install or configure EmulationStation or download roms or bios for it, you need to provide them.


![Addon-Selected-Information.jpg](/Addon-Screenshots/Addon-Selected-Information.jpg)


## Installation

#### Prerequisites
First, you need to install Kodi, to download and install it go to https://kodi.tv/  
After that you need to install and configure EmulationStation, to download and get instructions based on your operating system, go to http://emulationstation.org/gettingstarted.html and to configure EmulationStation go to http://emulationstation.org/gettingstarted.html#config (basically what you need to do is to edit XML files to set the roms paths for each system and set the location of the emulator-manager you want to use, for example *RetroArch*, and add your roms).

#### Steps
1. Download the Addon:   
   For now this Addon is not registered on any official or unofficial Kodi repositories yet, hopefully it would be in the future. For now the way to install this Addon is to install it from a zip file.  
   Download the zip file here: https://github.com/BrosMakingSoftware/Kodi-Launches-EmulationStation-Addon/archive/master.zip

2. Start Kodi and navigate to `Settings -> Add-ons -> Install from zip file`, on the file browser look for the zip file you downloaded on the previous step and select it. Installation is going to start and Kodi will show a notification when this is done.   
   **Note:** If preference is not checked, Kodi will ask you to allow installations from zip files as a security measure. Change your preferences to allow installations from zip files and continue with the installation. Also please notice that this options can be displayed on different paths depending of the Skin you are using. The path used above is a generic one that may or may not be on your Skins, but in any case it is not hard to find.

3. Once the Addon is installed, navigate to `Program Add-ons` and you will see EmulationStation listed there.   

   ![Addon-Selected.jpg](/Addon-Screenshots/Addon-Selected.jpg)

4. Before running the Addon, you need to set the location of the EmulationStation executable, the default location is set to `C:\Program Files (x86)\EmulationStation\emulationstation.exe`, this is assuming you are using Windows and you installed it on the default location, but if your executable is not on this path, or you are using Linux or MacOS, you can choose your own location by going to the Addon-Settings by selecting the EmulationStation Addon, bringing up the contextual menu by right-clicking it (or pressing the `Guide` button on a remote, or pressing `C` or `Start` keys on a keyboard) and selecting `Settings` or `Configure`.   

   ![Addon-Settings.jpg](/Addon-Screenshots/Addon-Settings.jpg)

   The next window will show you the `EmulationStation executable` property that you can select and change by navigating on the file browser to select your location. For Linux users, if you installed EmulationStation using an installer, you can try to look at `/usr/local/bin/emulationstation` first, otherwise select your custom location. If you provided an executable that doesn't exist anymore, the next time you try to run it the Addon will show you an error message suggesting you to go to the Addon-Settings and change it.   

   ![Addon-Settings-Edit-Executable.jpg](/Addon-Screenshots/Addon-Settings-Edit-Executable.jpg)

5. Enjoy!
