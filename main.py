'''
Autors: 
    Bastián Escribano
    Daniel Catalán

Initialiced: 24-08-2022
'''

import Config as cfg
import system as sys
import time as t
#import os

print("Opening program...")
myConfig = cfg.Config()
print("Programs to close: variable.programsToClose")
print("App running.")
while True:
    for programName in myConfig.programsToClose:
        if sys.detectProgram(programName):
            print(programName, "is running.")
        else:
            print(programName, "is not running")
        t.sleep(2.0)