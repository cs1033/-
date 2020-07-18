from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.loans.loanPay import Ui_loanPay
from alarm import alarmMessageBox
import random
import datetime

class loan_pay(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(loan_pay, self).__init__(parent)
        self.ui = Ui_loanPay()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()
        self.loan_id = parent.loan_id

        self.showMessage()
        self.ui.Ok.clicked.connect(self.Ok)

#展示贷款和贷款人信息
    def showMessage(self):
        loan_id = self.loan_id

        cursor = self.db.cursor()
        sql = """select * from loans where loan_id = %s"""
        cursor.execute(sql, [loan_id])
        loan_id,bank,amount,amount_payed, loan_date = cursor.fetchone()

        self.ui.loan_id.setText(loan_id)
        self.ui.amount.setText(str(amount))
        self.ui.amount_payed.setText(str(amount_payed))
        self.ui.bank.setText(bank)

        sql = """select client.id_number,client.name from apply , client where apply.id_number = client.id_number and apply.loan_id = %s"""
        cursor.execute(sql,[loan_id])
        ret = cursor.fetchall()
        #print(ret)

        self.ui.client_id.setText(ret[0][0])
        self.ui.client_name.setText(ret[0][1])

#支付贷款
    def Ok(self):
        pay = self.ui.pay.text()
        loan_id = self.loan_id

        cursor = self.db.cursor()
        sql = """select amount, amount_payed ,name from loans where loan_id = %s"""
        cursor.execute(sql, [loan_id])
        amount, amount_payed, name = cursor.fetchone()

        #print("1")
        try:
            now = float(pay)
            if amount_payed + now > amount:
                self.ui.ts.setText("! 超出需要支付的金额")
                return
            if now <= 0:
                self.ui.ts.setText("! 请输入正数")
                return
            self.ui.ts.setText("")
            pay_id = ""

            #print("2")
        #随机生成pay_id
            while True:
                pay_id = str(random.randint(1000, 10000000))
                #print(pay_id,type(pay_id))
                sql = """select * from pay where pay_id = %s"""
                cursor.execute(sql, [pay_id])
                ret = cursor.fetchone()
                #print(ret)

                if ret is None:
                    break
            #print("3")
            sql = """insert into pay value (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, [pay_id, name, loan_id, now, datetime.date.today()])
            #print("4")
            sql = """UPDATE loans SET  amount_payed = %s  WHERE loan_id = %s"""
            cursor.execute(sql, [str(now+amount_payed), loan_id])
            
            #获取支行名称
            sql = """select name from loans where loan_id = %s"""
            cursor.execute(sql, [loan_id])
            sub_name = cursor.fetchone()    
            # 修改支行余额
            sql = """update sub_branch set asset = asset - %s 
                    where name =  %s"""
            cursor.execute(sql, [pay, sub_name[0]])    
            self.db.commit()
            alarmMessageBox(self, "支付成功！\n" + str(datetime.date.today()) + "\n支付号:" + pay_id + "\n本次支付金额：" + str(now) + "\n总支付金额:" +  str(now + amount_payed)  + "\n未支付金额:" + str(amount - now - amount_payed))
            self.close()





  #不是浮点数
        except ValueError:
            self.ui.ts.setText("! 请输入正数")
            return




