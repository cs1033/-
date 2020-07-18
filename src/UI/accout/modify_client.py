from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.accout.accountModifyClient import Ui_Dialog
from alarm import alarmMessageBox
import datetime

class modify_clinet(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(modify_clinet, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()
        self.client_id = parent.client_id
        self.account_type = parent.account_type
        self.account_id = parent.account_id

        self.ui.add.clicked.connect(self.add)
        self.ui.delete_2.clicked.connect(self.delete)

#添加关联客户
    def add(self):
        id = self.ui.id.text()

        if id is "":
            alarmMessageBox(self,"id不能为空")
            return

        #查询客户是否存在
        cursor = self.db.cursor()
        sql = """ select * from client where id_number = %s"""
        cursor.execute(sql, [id])
        ret = cursor.fetchall()

        if ret is None:
            alarmMessageBox(self,"该客户不存在！")
            return

        # 每个客户只能有一个储蓄账户和一个支票账户
        sql = """select account_type from own,account where own.account_number = account.account_number and  id_number = %s"""
        cursor.execute(sql, [id])
        ret = cursor.fetchall()
        # print(ret)
        if len(ret) >= 2 or len(ret) >= 1 and ret[0][0] == int(self.account_type):
            alarmMessageBox(self,"每个客户只能有一个储蓄账户和一个支票账户 或者你已经是该账户的户主")
            return

        #加入
        try:
            sql = """insert into own value (%s,%s,%s)"""
            cursor.execute(sql, [id,self.account_id,datetime.date.today()])
            alarmMessageBox(self,"加入成功！")
        except:
            alarmMessageBox(self,"加入失败！")

        self.db.commit()
        self.parent.closeClient()
        self.parent.showTable()
        self.close()


#删除账户户主
    def delete(self):
        id = self.ui.id.text()

        if id is "":
            alarmMessageBox(self, "id不能为空")
            return

        cursor = self.db.cursor()
        sql = """select *  FROM own WHERE id_number = %s and account_number = %s"""
        cursor.execute(sql, [id, self.account_id])
        ret = cursor.fetchone()
        #print(ret,ret is None)

        if ret is None:
            alarmMessageBox(self,"该客户不是此账户的户主！")
            return

        try:
            cursor = self.db.cursor()
            sql = """DELETE FROM own WHERE id_number = %s and account_number = %s"""
            cursor.execute(sql, [id, self.account_id])
            alarmMessageBox(self, "删除成功！")
        except:
            alarmMessageBox(self, "删除失败！")

        self.db.commit()
        self.parent.closeClient()
        self.parent.showTable()
        self.close()







