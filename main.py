'''
Autors: 
    Bastián Escribano
    Daniel Catalán

Initialiced: 24-08-2022
'''

import Config as cfg
import system as sys
import time as t
from PyQt6.QtWidgets import QApplication, QWidget
import sys
import psutil

print("Opening program...")
myConfig = cfg.Config()
print("Programs to close: variable.programsToClose")
print("App running.")
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
while True:
    for programName in myConfig.programsToClose:
        if sys.detectProgram(programName):
            print(programName, "is running.")
        else:
            print(programName, "is not running")
        t.sleep(2.0)

        for process in psutil.process_iter():
            if programName == process.name():
                process.kill()
                print(programName, " closed.")
        t.sleep(2.0)
