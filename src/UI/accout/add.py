from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.createClient import  Ui_createClient
from UI.accout.accountAdd import Ui_addAccount

class account_add(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_add, self).__init__(parent)
        self.ui = Ui_addAccount()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.CreateBtn.clicked.connect(self.Create)

    def Create(self):
        id = self.ui.id.text()
        account_type = self.ui.account_type.text()
        account_id = self.ui.account_id.text()
        brance = self.ui.brance.text()
        start_date = self.ui.start_date.text()
        rate = self.ui.rate.text()
        currency_type = self.ui.currency_type.text()
        overdraft = self.ui.overdraft.text()

        if account_type != "1" and account_type != "2":         #账户类型错误
            QMessageBox.information(self, '提示', '请输入账户类型，1:储蓄账户，2：支票账户', QMessageBox.Close, QMessageBox.Close)
            return

        else:
            cursor = self.db.cursor()
            sql = """select account_type from own,account where own.account_number = account.account_number and  id_number = %s"""
            cursor.execute(sql, [id])
            ret = cursor.fetchall()
            #print(ret)
            if len(ret) >= 2 or len(ret) >= 1 and ret[0][0] == int(account_type):       #每个客户只能有一个储蓄账户和一个支票账户
                QMessageBox.information(self, '提示', '每个客户只能有一个储蓄账户和一个支票账户', QMessageBox.Close, QMessageBox.Close)
                return

            sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
            cursor.execute(sql, [id, self.id_number])
            ret = cursor.fetchone()

            if ret is None:
                QMessageBox.information(self, '提示', '创建失败,户主不是你的客户', QMessageBox.Close, QMessageBox.Close)

            else:
                sql = """select department.name from staff,department where staff.dep_department_id = department.department_id and staff.id_number = %s"""
                cursor.execute(sql,[self.id_number])
                sub_name = cursor.fetchone()        #获取支行名称
                #print(sub_name)

                if id is not None:
                    try:    #own ,account同时插入  修改支行余额
                        sql = """ insert into account value (%s,%s,%s,%s,%s,%s,%s,%s)"""
                        cursor.execute(sql,[account_type,account_id,brance,sub_name[0],start_date,rate,currency_type,overdraft])
                        #print("1")
                        self.db.commit()
                        sql = """insert into own value (%s,%s,%s)"""
                        #print("2")
                        cursor.execute(sql,[id,account_id,start_date])
                        QMessageBox.information(self, '提示', '创建成功', QMessageBox.Close, QMessageBox.Close)
                        
                        # 修改支行余额
                        sql = """update sub_branch set asset = asset + %s 
                                where name =  %s"""
                        cursor.execute(sql, [brance, sub_name[0]])

                        self.db.commit()
                        self.close()
                    except:
                        QMessageBox.information(self, '提示', '创建失败', QMessageBox.Close, QMessageBox.Close)
                else:
                    QMessageBox.information(self, '提示', '创建失败,id不能为空', QMessageBox.Close, QMessageBox.Close)

