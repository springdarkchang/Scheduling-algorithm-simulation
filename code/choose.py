from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import FileOperation
import window
import ProcessList
import Manage
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 245)
        QApplication.setStyle("Fusion")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(206, 30, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(206, 110, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "?????????????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????????????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "input1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "input2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "??????????????????"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "?????????????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.pushButton.clicked.connect(lambda: self.button(MainWindow))  # ????????????????????????button??????

    def button(self, MainWindow):
        file = self.comboBox.currentText()  # ??????????????????
        idea= self.comboBox_2.currentText()  # ??????????????????
        if file == "input1":
            FileOperation.file_num = 1
        elif file == "input2":
            FileOperation.file_num = 2
        if idea == "??????????????????":
            ProcessList.idea = 1
        elif idea == "?????????????????????":
            ProcessList.idea = 2
        Manage.t.before_prepare()
        self.m = QMainWindow()
        ui = window.ui
        ui.setupUi(self.m)
        self.m.show()  # ???????????????
        MainWindow.close()
        window.ui.printf("??????????????????:")
