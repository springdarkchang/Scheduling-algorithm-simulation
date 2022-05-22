import choose
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app2 = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = choose.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # 显示选择窗口
    sys.exit(app2.exec_())