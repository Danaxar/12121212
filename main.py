'''
Autors: 
    Bastián Escribano
    Daniel Catalán

Initialiced: 24-08-2022
'''

import Config as cfg
from PyQt6 import QtCore, QtWidgets
from killer import killerProcess
import sys
import threading

# Functions
def hilo1():
    killerProcess()

# Global variables
t1 = threading.Thread(name="Hilo1", target=hilo1)

# Classes
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.power = -1  # Off
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(419, 335)
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 171, 71))
        self.pushButton.setObjectName("startButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 113, 32))
        self.pushButton_2.setObjectName("cancelButton")
        self.pushButton.clicked.connect(self.buttonClickedStart)
        self.pushButton_2.clicked.connect(self.buttonClickedCancel)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "be-productive"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))

    def buttonClickedStart(self):
        self.power = self.power * (-1)
        if self.power == 1:
            killerProcess(self.power)
            error_dialog.showMessage('Started!')
            print('Killer started!')
            #hilo1()
        else:
            killerProcess(self.power)
            error_dialog.showMessage('Stopped.')
            #print('Killer stopped.')
            
            

    def buttonClickedCancel(self):
        exit()

if __name__ == "__main__":
    print("App running.")
    #t1.start()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    error_dialog = QtWidgets.QErrorMessage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
    
print("Program finished.")
