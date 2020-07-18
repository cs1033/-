from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.userLogin import Ui_Dialog
from homePage import homePage

from db import db_login

class LoginDialog(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"
    def __init__(self, parent):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.LoginBtn.clicked.connect(self.login)

        self.parent = parent
        self.db = parent.db
        self.show()
    
    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        self.id = username
        self.id_number = username

        cursor = self.db.cursor()
        sql = """ select password FROM staff WHERE id_number = %s"""
        cursor.execute(sql, [self.id])
        result = cursor.fetchone()
        #print(result)

        if result[0] == None:
            QMessageBox.information(self, '提示', '用户id错误', QMessageBox.Close, QMessageBox.Close)
        elif result[0] == password:
            QMessageBox.information(self, '提示', '登录成功', QMessageBox.Close, QMessageBox.Close)
            self.close()
            w = homePage(self)
        else:
            QMessageBox.information(self, '提示', '密码错误', QMessageBox.Close, QMessageBox.Close)
