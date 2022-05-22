from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import clock
import Manage
import ProcessList
import Job_request_thread
import CPU
import random
import FileOperation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 675)
        QApplication.setStyle("Fusion")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 481, 431))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 530, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 530, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 10, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(660, 90, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(790, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(920, 90, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(660, 150, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(920, 150, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(660, 210, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(710, 260, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(920, 210, 104, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(510, 330, 571, 251))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 600, 101, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(120, 590, 61, 31))
        self.textEdit_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 600, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 330, 231, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(650, 380, 231, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(650, 430, 231, 41))
        self.label_14.setObjectName("label_14")
        self.label_12.setFont(font)
        self.label_13.setFont(font)
        self.label_14.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if clock.Clock.num_start <5:
            self.pushButton.setEnabled(False)  # 如果初始进程数量小于5，则运行按钮不能点击
        if ProcessList.idea == 1:  # 如果选择时间片轮转法，则不显示三级队列的时间片
            self.label_12.setVisible(False)
            self.label_13.setVisible(False)
            self.label_14.setVisible(False)
        elif ProcessList.idea == 2:  # 如果选择多级反馈队列，则不显示就绪队列
            self.label_8.setVisible(False)
            self.tableWidget.setVisible(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "调度界面"))
        self.label.setText(_translate("MainWindow", "运行日志"))
        self.pushButton.setText(_translate("MainWindow", "启动"))
        self.pushButton_2.setText(_translate("MainWindow", "添加任务"))
        self.label_2.setText(_translate("MainWindow", "系统状态"))
        self.label_3.setText(_translate("MainWindow", "当前时间："))
        self.label_4.setText(_translate("MainWindow", "当前进程ID："))
        self.label_5.setText(_translate("MainWindow", "下一进程ID："))
        self.label_6.setText(_translate("MainWindow", "剩余指令数："))
        self.label_7.setText(_translate("MainWindow", "已用时间片："))
        self.label_8.setText(_translate("MainWindow", "就绪队列"))
        self.label_9.setText(_translate("MainWindow", "进程优先级："))
        self.label_12.setText(_translate("MainWindow", "一级队列时间片：3"))
        self.label_13.setText(_translate("MainWindow", "二级队列时间片：4"))
        self.label_14.setText(_translate("MainWindow", "三级队列时间片：5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "进程ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "优先级"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "进入时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "剩余指令数"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ir"))
        self.label_10.setText(_translate("MainWindow", "当前任务总数："))
        self.label_11.setText(_translate("MainWindow", "5<=任务数<=10"))
        self.pushButton.clicked.connect(lambda: self.button1())  # 启动按钮
        self.pushButton_2.clicked.connect(lambda: self.button2())  # 添加任务按钮
        self.textEdit_7.setText(str(clock.Clock.num_start))  # 初始进程数量

    def printf(self, mypstr):  # 填写运行日志
        self.textBrowser.append(mypstr)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后一行
        FileOperation.write_result(mypstr)
        QApplication.processEvents()

    def slotAdd(self):  # 向界面右侧添加数据
        self.textEdit.setText(str(clock.Clock.current))  # 添加当前时间
        self.textEdit_2.setText(str(CPU.cpu.ir))  # 添加当前进程ID
        self.textEdit_3.setText(str(CPU.cpu.pc))  # 添加下一进程ID
        try:  # 无进程运行，则显示0
            self.textEdit_4.setText(str(ProcessList.pro.running_processes.Priority))  # 添加进程优先级
            self.textEdit_5.setText(str(ProcessList.pro.running_processes.InstrucNum-ProcessList.pro.running_processes.ir))#添加剩余指令数
            self.textEdit_6.setText(str(ProcessList.pro.running_processes.stime))  # 添加已用时间片
        except:
            self.textEdit_4.setText("0")
            self.textEdit_5.setText("0")
            self.textEdit_6.setText("0")
        if ProcessList.idea == 1:
            self.table_add()
        if len(ProcessList.pro.ready_processes)>10:  # 只允许并发10个任务
            self.pushButton_2.setEnabled(False)  # 禁用添加任务按钮
        else:
            self.pushButton_2.setEnabled(True)
        QApplication.processEvents()  # 刷新界面

    def table_add(self):  # 向就绪队列表格中添加数据
        self.tableWidget.setRowCount(len(ProcessList.pro.ready_processes))  # 设置行数
        for i in range(len(ProcessList.pro.ready_processes)):
            item = QTableWidgetItem(str(ProcessList.pro.ready_processes[i].ProID))  # 显示进程ID
            self.tableWidget.setItem(i, 0, item)
            item = QTableWidgetItem(str(ProcessList.pro.ready_processes[i].Priority))  # 显示优先级
            self.tableWidget.setItem(i, 1, item)
            item = QTableWidgetItem(str(ProcessList.pro.ready_processes[i].InTimes))  # 显示进入时间
            self.tableWidget.setItem(i, 2, item)
            item = QTableWidgetItem(str(ProcessList.pro.ready_processes[i].InstrucNum-ProcessList.pro.ready_processes[i].ir))  # 显示剩余指令数
            self.tableWidget.setItem(i, 3, item)
            item = QTableWidgetItem(str(ProcessList.pro.ready_processes[i].ir))  # 显示当前指令
            self.tableWidget.setItem(i, 4, item)

    def button1(self):
        if self.pushButton.text() == "启动":
            self.pushButton.setEnabled(False)  # 运行中禁用启动按钮
            self.pushButton.setText("运行中")  # 改变按钮文字为“运行中”
            Manage.t.thread_start()  # 启动线程
        elif self.pushButton.text() == "运行结束":
            exit()  # 结束程序

    def button2(self):
        clock.Clock.num_start += 1  # 进程数量加1
        n=clock.Clock.current  # 获取当前时间
        str_num=random.randint(10,30)  # 随机生成指令数量
        self.textEdit_7.setText(str(clock.Clock.num_start))  # 显示当前进程数量
        FileOperation.write_new_jobs(clock.Clock.num_start,n,str_num)  # 将新任务写入文件
        Job_request_thread.j.new_EnReady(clock.Clock.num_start,n,str_num)  # 将新任务加入就绪队列
        if clock.Clock.num_start >=5:  # 如果进程数量大于5，则启用启动按钮
            if self.pushButton.text()=="启动":
                self.pushButton.setEnabled(True)
ui=Ui_MainWindow()
