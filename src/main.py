from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5 import QtCore
from UI.loginDatabase import Ui_loginDatabase
from login import LoginDialog
from db import *

debug = False


class MainWindow(QMainWindow):
    " The Entrance of the Main window"

    def __init__(self):
        super().__init__()
        # 主窗口需要有一个UI界面，我们使用TablePage作为主窗口显示的UI界面
        self.ui = Ui_loginDatabase()
        self.ui.setupUi(self)

        # 初始化配置
        self.initBinding()

        #self.ui.login
        #self.ui.setStyleSheet("#loginDatabase{border-image:url(./1.jpg);}")
        self.show()
        #self.ui.label.setStyleSheet("color:red;")




    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.LoginBtn.clicked.connect(self.Login)



    # all the function to bind with
    def Login(self):
        #dialog = LoginDialog(self)
        #dialog.exec_()
        ipaddr = self.ui.ipaddr.text()
        dbname = self.ui.database.text()
        username = self.ui.username.text()
        password = self.ui.password.text()


        self.db = db_login(username, password, ipaddr, dbname)
        #self.db = db_login("root", "19991016L", ipaddr, "bank")

        if self.db == None:
            QMessageBox.information(self, '提示', '登录失败!', QMessageBox.Close, QMessageBox.Close)
        else:
            QMessageBox.information(self, '提示', '登录成功!', QMessageBox.Close, QMessageBox.Close)
            self.close()
            dialog = LoginDialog(self)
            #dialog.exec_()


if __name__ == "__main__":
    import sys
    #print('start')    
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())