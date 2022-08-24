'''
Autors: 
    Bastián Escribano
    Daniel Catalán

Initialiced: 24-08-2022
'''

import Config as cfg
import system as sys
import time as t
import psutil


print("Opening program...")
myConfig = cfg.Config()
print("Programs to close: variable.programsToClose")
print("App running.")
while True:
    for programName in myConfig.programsToClose:
        for process in psutil.process_iter():
            if programName == process.name():
                process.kill()
                print(programName, " closed.")
        t.sleep(2.0)