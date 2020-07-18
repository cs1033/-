from PyQt5.QtWidgets import QDialog, QMessageBox,QTableWidgetItem
from UI.accout.accountSearch import Ui_accountSearch
from alarm import alarmMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

class account_search(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_search, self).__init__(parent)
        self.ui = Ui_accountSearch()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.Search.clicked.connect(self.Search)

        self.ui.account.setColumnCount(7)
        self.ui.account.setHorizontalHeaderLabels(['账户类型', '账户号', '余额', '所属支行', '开户日期', '透支额度/利率 ', '货币类型'])
        self.ui.client.setColumnCount(4)
        self.ui.client.setHorizontalHeaderLabels(['账户号', '户主身份证', '户主姓名', '最近访问时间'])

    def clear(self):
        self.ui.client.setRowCount(0)
        self.ui.account.setRowCount(0)


    def Search(self):
        choice = self.ui.choice.currentText()
        text = self.ui.text.text()

        # self.ui.account.setColumnCount(7)
        # self.ui.account.setHorizontalHeaderLabels(['账户类型', '账户号', '余额', '所属支行', '开户日期', '透支额度/利率 ',  '货币类型'])
        # self.ui.client.setColumnCount(4)
        # self.ui.client.setHorizontalHeaderLabels(['账户号', '户主身份证', '户主姓名', '最近访问时间'])

        if text == "":
            self.ui.ts.setText("! 搜索内容不能为空")
            return

            # for i in range(7) :
            #     for j in range(5):
            #         item = QTableWidgetItem("None")
            #         item.setTextAlignment(QtCore.Qt.AlignCenter)
            #         self.ui.client.setItem(i, j, item)


        cursor = self.db.cursor()
        sql1 = """"""
        sql2 = """"""

        if choice == "账户号":
            #搜索账户信息
            sql1 = """select * from account where account_number REGEXP %s"""
            #搜索户主信息
            sql2 = """select own.account_number, client.id_number, client.name, own.last_date from own, client 
                    where client.id_number = own.id_number and  account_number REGEXP %s """

        if choice == "户主身份证":
            sql2 = """
                    select own.account_number, client.id_number, client.name, own.last_date from own, client 
                    where client.id_number = own.id_number and  own.id_number REGEXP %s 
                """

            sql1 = """
                    select account_type, own.account_number, brance, sub_bank_name, start_date, rate, currency_type, overdraft   
                    from own , account 
                    where own.account_number = account.account_number and own.id_number REGEXP %s
                    """

        cursor.execute(sql1, [text])
        tab1 = cursor.fetchall()
        cursor.execute(sql2, [text])
        tab2 = cursor.fetchall()


        self.printTable(tab1, tab2)


 #打印表格
    def printTable(self,tab1,tab2):
        self.clear()

        #打印账户信息
        for i in range(len(tab1)):
            self.ui.account.insertRow(i)
            for j in range(7):
                item = QTableWidgetItem(str(tab1[i][j]))
                if j == 0:
                    if tab1[i][j] == 1:
                        item = QTableWidgetItem("储蓄账户")
                    if tab1[i][j] == 2:
                        item = QTableWidgetItem("支票账户")
                if j == 5:
                    if tab1[i][0] == 2:
                        item = QTableWidgetItem(str(tab1[i][7]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.account.setItem(i, j, item)

            self.ui.account.setRowCount(i+1)


        #打印户主信息
        for i in range(len(tab2)):
            self.ui.client.insertRow(i)
            for j in range(4):
                item = QTableWidgetItem(str(tab2[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.client.setItem(i, j, item)

            self.ui.client.setRowCount(i + 1)






