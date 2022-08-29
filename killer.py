import Config as cfg
import time as t
import psutil

def killerProcess(activation):
    print("Starting the killer...")
    myConfig = cfg.Config()
    print("Programs to close:", myConfig.programsToClose)
    while activation == 1:
        t.sleep(2.0)
        for programName in myConfig.programsToClose:
            for process in psutil.process_iter():
                if programName == process.name():
                    process.kill()
                    print(programName, " closed.")
    print("Killer closed")
