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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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
        error_dialog.showMessage('Started!')
        killerProcess()
    def buttonClickedCancel(self):
        exit()

def hilo1():
    killerProcess()

if __name__ == "__main__":
    print("App running.")
    t1 = threading.Thread(name="Hilo1", target=hilo1)
    t1.start()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    error_dialog = QtWidgets.QErrorMessage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
    
print("Program finished.")
