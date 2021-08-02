import cx_Freeze
import sys

base =  None
if sys.platform =="win32":
    base  =  "Win32GUI"
shortcut_table  = [
    ("Desktop Shortcut",
     "DesktopFolder ",
     "Snakes Lunch Party",
     "TARGETDIR",
     "[TARGETDIR]\snakegame.exe",
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = { 'data ': msi_data}

excutables = [ cx_Freeze.Executable(script="snakgame.py", icon="saanp.ico", base= base)]

cx_Freeze.setup(
 version = "1.0",
 description = " Pygame Snake Lunch Game",
 author = "HarryBoy",
 name= "Snake Lunch Party",
 options= { "build.exe": { "packages" : ["pygame","os","random"],
                           "include files" : ['avengersback.mp3', 'gameover.png', 'harrypotter.mp3','saanp.ico','snakeback.jpg','snakehome.png']},
                           "bdist_msi": bdist_msi_options,
            },
 excutables = executables

 
)

