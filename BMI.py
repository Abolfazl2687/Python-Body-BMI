from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from pymsgbox import alert

class Ui_MainWindow(object):
    
    def contact(self):
        os.system("start http://t.me/Abooee2687 ")
            
    def start(self):
        
        self.listWidget.clear()
        
        vazn = self.vazn.text()
        ghad = self.ghad.text()
            
        bmi1 = int(vazn) / (int(ghad) ** 2)
        
        bmi = round(bmi1 * 10000 , 1)
        
        if bmi < 16.0:
            text = "کمبود وزن بسیار شدید"
        elif 16.0 <= bmi <= 16.9:
            text = "کمبود وزن شدید"
        elif 17.0 <= bmi <= 18.4:
            text = "کمبود وزن"
        elif 18.5 <= bmi <= 24.9:
            text = "وزن طبیعی"
        elif 25.0 <= bmi <= 29.9:
            text = "اضافه وزن"
        elif 30.0 <= bmi <= 34.9:
            text = "چاقی درجه 1"
        elif 35 <= bmi <= 39.9:
            text = "چاقی درجه 2"
        elif bmi >= 40.0:
            text = "چاقی درجه 3"
            
            
        self.listWidget.addItem("\n \n BMI = "+str(bmi)+"  \n \n  "+text)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hesabkon = QtWidgets.QPushButton(self.centralwidget)
        self.hesabkon.setGeometry(QtCore.QRect(290, 440, 210, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.hesabkon.setFont(font)
        self.hesabkon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hesabkon.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.hesabkon.setObjectName("hesabkon")
        self.vazn = QtWidgets.QLineEdit(self.centralwidget)
        self.vazn.setGeometry(QtCore.QRect(50, 120, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vazn.setFont(font)
        self.vazn.setObjectName("vazn")
        self.ghad = QtWidgets.QLineEdit(self.centralwidget)
        self.ghad.setGeometry(QtCore.QRect(450, 120, 290, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ghad.setFont(font)
        self.ghad.setText("")
        self.ghad.setObjectName("ghad")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 231, 51))
        self.label.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 210, 470, 210))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.contactpro = QtWidgets.QPushButton(self.centralwidget)
        self.contactpro.setGeometry(QtCore.QRect(674, 10, 111, 31))
        self.contactpro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contactpro.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.contactpro.setObjectName("contactpro")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.hesabkon.clicked.connect(self.start)
        self.contactpro.clicked.connect(self.contact)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Abolfazl"))
        self.hesabkon.setText(_translate("MainWindow", "محاسبه"))
        self.vazn.setPlaceholderText(_translate("MainWindow", "   وزن خود را وارد کنید ..."))
        self.ghad.setPlaceholderText(_translate("MainWindow", "   قد خود را وارد کنید ..."))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">B.M.I</span></p></body></html>"))
        self.contactpro.setText(_translate("MainWindow", "contact programmer"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
