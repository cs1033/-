# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import QDialog, QMessageBox,QMainWindow
from UI.table import Ui_TablePage
from UI.client.client_manage import client_manage
from UI.accout.accout_manage import account_manage
from UI.loans.loan import loan_manage
from UI.business import business

class homePage(QMainWindow):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(homePage, self).__init__(parent)
        self.ui = Ui_TablePage()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()


        # 将主界面按钮点击动作绑定到函数
        self.ui.clientManage.clicked.connect(self.clientManage)
        self.ui.accountManage.clicked.connect(self.accountManage)
        self.ui.loanManage.clicked.connect(self.loanManage)
        self.ui.business.clicked.connect(self.business)

        #self.ui.SearchBtn.clicked.connect(self.renderTable)

        # 将菜单点击动作绑定到函数
        #self.ui.actionLogin.triggered.connect(self.Login)

        self.ui.actionLogout.triggered.connect(self.LogOut)

        #print("0")
        cursor = self.db.cursor()
        sql = """select dep_department_id,name from staff where id_number = %s """
        #print("1")
        cursor.execute(sql, [self.parent.id_number])
        #print("2")
        result = cursor.fetchone()
        #print(result)
        name = cursor.fetchone()
        #print(name)

        sql = """select name,department_name from department where department_id = %s """
        cursor.execute(sql, [result[0]])
        #print("5")
        welcome = cursor.fetchone()
        #print(welcome)
        self.ui.welcome.setText("欢迎您： "+welcome[0]+"-"+welcome[1]+"-"+result[1])
        #print("7")


    def clientManage(self):
        #self.close()
        w = client_manage(self)
        #w.exec_()


    def LogOut(self):
        self.close()
        self.parent.show()


    def accountManage(self):
        w = account_manage(self)

    def loanManage(self):
        w = loan_manage(self)
    
    def business(self):
        w = business(self)






