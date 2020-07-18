from PyQt5.QtWidgets import QDialog, QMessageBox,QTableWidgetItem
# from UI.loans.loanSearch import Ui_laonSearch
from UI.client.clientSearch import Ui_clientSearch
from alarm import alarmMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class client_search(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_search, self).__init__(parent)
        self.ui = Ui_clientSearch()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.Search.clicked.connect(self.Search)

        """ self.ui.loan.setColumnCount(5)
        self.ui.loan.setHorizontalHeaderLabels(['贷款号', '发放机构', '贷款金额', '已发放金额', '申请时间'])
        self.ui.client.setColumnCount(3)
        self.ui.client.setHorizontalHeaderLabels(['贷款号', '户主身份证', '户主姓名'])
        self.ui.pay.setRowCount(5)
        self.ui.pay.setHorizontalHeaderLabels(['支付号', '支付机构', '贷款号', '支付金额', '支付时间']) """

    def clear(self):
        self.ui.client.setRowCount(0)
        self.ui.loan.setRowCount(0)
        self.ui.account.setRowCount(0)

    def Search(self):
        choice = self.ui.choice.currentText()
        text = self.ui.text.text()



        if text == "":
            self.ui.ts.setText("! 搜索内容不能为空")
            return

            # for i in range(7) :
            #     for j in range(5):
            #         item = QTableWidgetItem("None")
            #         item.setTextAlignment(QtCore.Qt.AlignCenter)
            #         self.ui.client.setItem(i, j, item)

        self.ui.ts.setText("")
        cursor = self.db.cursor()
        sql1 = """"""
        sql2 = """"""
        sql3 = """"""

        if choice == "客户经理身份证":
            #搜索客户信息
            sql1 = """select * from client where sta_id_number REGEXP %s"""
            #搜索账户信息
            sql2 = """
                    select own.* from own, client 
                    where own.id_number = client.id_number and client.sta_id_number REGEXP %s 
                      """
            #搜索贷款信息
            sql3 = """
                    select apply.id_number, apply.loan_id, loans.amount, loans.amount_payed
                    from apply, loans, client
                    where apply.id_number = client.id_number and apply.loan_id = loans.loan_id and client.sta_id_number REGEXP %s
                """



        if choice == "户主身份证":
            sql2 = """
                    select * from own where id_number  REGEXP %s
                """

            sql1 = """
                    select * from client where id_number REGEXP %s
                    """

            sql3 = """
                    select apply.id_number, apply.loan_id, loans.amount, loans.amount_payed
                    from apply, loans
                    where apply.loan_id = loans.loan_id and apply.id_number REGEXP %s
                """

        if choice == "姓名":
            #搜索客户信息
            sql1 = """select * from client where name REGEXP %s"""
            #搜索账户信息
            sql2 = """
                    select own.* from own, client 
                    where own.id_number = client.id_number and client.name REGEXP %s 
                      """
            #搜索贷款信息
            sql3 = """
                    select apply.id_number, apply.loan_id, loans.amount, loans.amount_payed
                    from apply, loans, client
                    where apply.id_number = client.id_number and apply.loan_id = loans.loan_id and client.name REGEXP %s
                """
        
        if choice == "电话号码":
            #搜索客户信息
            sql1 = """select * from client where phonenumber REGEXP %s"""
            #搜索账户信息
            sql2 = """
                    select own.* from own, client 
                    where own.id_number = client.id_number and client.phonenumber REGEXP %s 
                      """
            #搜索贷款信息
            sql3 = """
                    select apply.id_number, apply.loan_id, loans.amount, loans.amount_payed
                    from apply, loans, client
                    where apply.id_number = client.id_number and apply.loan_id = loans.loan_id and client.phonenumber REGEXP %s
                """



        cursor.execute(sql1, [text])
        tab1 = cursor.fetchall()
        # print("1")
        cursor.execute(sql2, [text])
        tab2 = cursor.fetchall()
        # print("2")
        cursor.execute(sql3, [text])
        tab3 = cursor.fetchall()

        # print("3")
        self.printTable(tab1, tab2, tab3)

 #打印表格
    def printTable(self, tab1, tab2, tab3):
        self.clear()
        #打印户主信息
        for i in range(len(tab1)):
            self.ui.client.insertRow(i)
            for j in range(9):
                item = QTableWidgetItem(str(tab1[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.client.setItem(i, j, item)
            self.ui.client.setRowCount(i+1)


        #打印账户信息
        for i in range(len(tab2)):
            self.ui.account.insertRow(i)
            for j in range(3):
                item = QTableWidgetItem(str(tab2[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.account.setItem(i, j, item)

            self.ui.account.setRowCount(i + 1)

        # 打印贷款信息
        for i in range(len(tab3)):
            self.ui.loan.insertRow(i)
            for j in range(4):
                item = QTableWidgetItem(str(tab3[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.loan.setItem(i, j, item)

            self.ui.loan.setRowCount(i + 1)




