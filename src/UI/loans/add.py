from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.loans.loanAdd import Ui_loanAdd
from alarm import alarmMessageBox
import datetime

class loan_add(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(loan_add, self).__init__(parent)
        self.ui = Ui_loanAdd()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.pushButton.clicked.connect(self.Create)


#申请贷款
    def Create(self):
        loan_id = self.ui.loan_id.text()
        amount = self.ui.amount.text()
        id1 = self.ui.id1.text()
        id2 = self.ui.id2.text()
        id3 = self.ui.id3.text()

        ready = True

#输入基本要求
        if loan_id == "":
            self.ui.ts1.setText("! id不能为空")
            ready = False
        else:
            self.ui.ts1.setText("")

        if amount == "":
            self.ui.ts2.setText("! 金额不能为空")
            ready = False
        elif not amount.isdigit():
            self.ui.ts2.setText("! 请填写数字")
            ready = False
        else:
            self.ui.ts2.setText("")

        if id1 == "":
            ready = False
            self.ui.ts3.setText("!申请人1不能为空")
        else:
            ready = True
            self.ui.ts3.setText("")



        if ready == False:
            alarmMessageBox(self,"失败")
            return

#判断Loan_id是否重复
        cursor = self.db.cursor()
        sql = """select * from loans where loan_id = %s"""
        cursor.execute(sql, [loan_id])
        ret = cursor.fetchone()

        if ret is not None:
            self.ui.ts1.setText("! id重复")
            #alarmMessageBox(self,"失败")
            ready = False

#判断id1是否存在
        sql = """select * from client where id_number = %s"""
        cursor.execute(sql, [id1])
        ret = cursor.fetchone()

        #print(ret)
        if ret is None:
            #print("fuck")
            #self.ui.ts3.setText("!申请人1不能为空")
            self.ui.ts3.setText("id不存在")
            #alarmMessageBox(self,"失败")
            ready = False


# 判断id2是否存在
        if id2 != "":
            sql = """select * from client where id_number = %s"""
            cursor.execute(sql, [id2])
            ret = cursor.fetchone()

            if ret is None:
                self.ui.ts4.setText("id不存在")
                #alarmMessageBox(self,"失败")
                ready = False

# 判断id3是否存在
        if id3 != "":
            sql = """select * from client where id_number = %s"""
            cursor.execute(sql, [id3])
            ret = cursor.fetchone()

            if ret is None:
                self.ui.ts5.setText("id不存在")
                #alarmMessageBox(self,"失败")
                ready = False

        if ready == False:
            alarmMessageBox(self,"失败")
            return

        try:
            sql = """select department.name from staff ,department where staff.dep_department_id = department.department_id and staff.id_number = %s"""
            cursor.execute(sql,[self.id_number])
            name = cursor.fetchone()

            sql = """select asset from sub_branch where name = %s"""
            #  print(name)
            cursor.execute(sql, [name])
            asset = cursor.fetchone()
            # print(asset)

            if asset[0] / 2 < float(amount):
                self.ui.ts2.setText("!金额过大，不能申请")
                return

            sql = """insert into loans value (%s,%s,%s,%s, %s)"""
            cursor.execute(sql, [loan_id, name, amount, "0", datetime.date.today()])

            sql = """insert into apply value (%s,%s)"""
            cursor.execute(sql,[loan_id,id1])

            if id2 != "":
                cursor.execute(sql, [loan_id, id2])
            if id3 != "":
                cursor.execute(sql, [loan_id, id3])

            alarmMessageBox(self,"成功")


        except:
            alarmMessageBox(self,"失败")


        self.db.commit()
        self.close()


