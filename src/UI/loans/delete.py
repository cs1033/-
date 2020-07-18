from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.loans.loanDelete import Ui_loanDelete
from alarm import alarmMessageBox

class loan_delete(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(loan_delete, self).__init__(parent)
        self.ui = Ui_loanDelete()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.Delete.clicked.connect(self.Delete)


    def Delete(self):
        loan_id = self.ui.loan_id.text()

#贷款号为空
        if loan_id == "":
            self.ui.ts.setText("! 不能为空")
            return


        cursor = self.db.cursor()
        sql = """select amount, amount_payed from loans where loan_id = %s"""
        cursor.execute(sql,[loan_id])
        ret = cursor.fetchone()
        #print(ret)

#贷款号错误
        if ret is None:
            self.ui.ts.setText("! 贷款号错误")
            return

        self.ui.ts.setText("")
        amount,amount_payed = ret

#贷款未发放
        if 0 == amount_payed:
            try:
                sql = """delete from apply where loan_id = %s"""
                cursor.execute(sql,[loan_id])
                sql = """delete from loans where loan_id = %s"""
                cursor.execute(sql,[loan_id])
                alarmMessageBox(self,"贷款未发放，删除成功")
            except:
                alarmMessageBox(self,"失败")


        self.db.commit()


