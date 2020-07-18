from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.accout.accountModify import Ui_Dialog
import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from UI.accout.modify_client import modify_clinet

class account_modify_ok(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_modify_ok, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

#继承父类的信息
        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()
        self.client_id = parent.client_id
        self.account_id = parent.account_id

#按键设置
        self.ui.ModifyBtn.clicked.connect(self.Modify)
        self.ui.modify.clicked.connect(self.modifyClient)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        self.showMessage()
        self.showTable()

#显示账户的基本信息
    def showMessage(self):
        cursor = self.db.cursor()
        sql = """ select account_type,currency_type,rate,brance,overdraft FROM account WHERE account_number = %s"""
        cursor.execute(sql, [self.account_id])
        result = cursor.fetchone()
        # print(result)
        account_type, currency_type, rate, brance, overdraft = result
        self.ui.account_id.setText(self.account_id)
        self.ui.account_type.setText(str(account_type))
        self.ui.overdraft.setText(str(overdraft))
        self.ui.currency_type.setText(str(currency_type))
        self.ui.rate.setText(str(rate))
        self.ui.brance.setText(str(brance))
        self.account_type = account_type


#显示账户的户主
    def showTable(self):
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['id', '姓名'])
        cursor = self.db.cursor()
        sql = """ select own.id_number ,client.name  from own ,client where own.id_number = client.id_number and own.account_number = %s"""
        cursor.execute(sql, [self.account_id])
        tabs = cursor.fetchall()
        currentRowCount = 0
        for tab in tabs:
            self.ui.tableWidget.insertRow(currentRowCount)

            item0 = QTableWidgetItem(str(tab[0]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item1 = QTableWidgetItem(str(tab[1]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)

            self.ui.tableWidget.setItem(currentRowCount, 0, item0)  # 列1
            self.ui.tableWidget.setItem(currentRowCount, 1, item1)  # 列2
            currentRowCount += 1
            self.ui.tableWidget.setRowCount(currentRowCount)


#修改账户的基本信息
    def Modify(self):
       currency_type,rate,brance,overdraft = self.ui.currency_type.text(),self.ui.rate.text(),self.ui.brance.text(),self.ui.overdraft.text()
       try:
           cursor = self.db.cursor()
           
           # 获取待删除账户余额 
           sql = """select brance from account 
                    where account_number = %s"""
           cursor.execute(sql, [self.account_id])
           pre_brance = cursor.fetchone()   
           # print("1")
           #获取支行名称
           sql = """select department.name from staff,department where staff.dep_department_id = department.department_id and staff.id_number = %s"""
           cursor.execute(sql, [self.id_number])
           sub_name = cursor.fetchone()     
           # print("2")

           sql = """ UPDATE account SET currency_type = %s,rate = %s, brance = %s ,overdraft = %s  WHERE account_number = %s"""
           cursor.execute(sql, [currency_type,rate,brance,overdraft, self.account_id])
           sql = """ UPDATE own SET last_date =  %s WHERE account_number = %s and id_number = %s"""
           cursor.execute(sql, [ datetime.date.today(),self.account_id,self.id_number])
           
           # print(pre_brance[0], brance)
           # 修改支行余额
           sql = """update sub_branch set asset = asset - %s + %s
                    where name =  %s"""
           cursor.execute(sql, [str(pre_brance[0]), str(brance), sub_name[0]])
           self.db.commit()
           QMessageBox.information(self, '提示', '修改成功', QMessageBox.Close, QMessageBox.Close)
           self.close()

       except:
           QMessageBox.information(self, '提示', '错误', QMessageBox.Close, QMessageBox.Close)
           self.close()

#不显示户主信息
    def closeClient(self):
        self.ui.tableWidget.setColumnCount(0)

#修改账户关联的户主
    def modifyClient(self):
        w = modify_clinet(self)
        #self.showTable()

