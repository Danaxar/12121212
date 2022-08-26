import Config as cfg
import time as t
from PyQt6.QtWidgets import QApplication, QWidget
import psutil

def killerProcess():
    print("Starting the killer...")
    myConfig = cfg.Config()
    print("Programs to close: variable.programsToClose")
    while True:
        for programName in myConfig.programsToClose:
            for process in psutil.process_iter():
                if programName == process.name():
                    process.kill()
                    print(programName, " closed.")
            t.sleep(2.0)
