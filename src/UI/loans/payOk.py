from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.loans.loanPayOk import Ui_loanPayOk
from alarm import alarmMessageBox
from UI.loans.pay import loan_pay

class loan_pay_ok(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(loan_pay_ok, self).__init__(parent)
        self.ui = Ui_loanPayOk()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.Ok.clicked.connect(self.Ok)

    def Ok(self):
        loan_id = self.ui.loan_id.text()

        # 贷款号为空
        if loan_id == "":
            self.ui.ts.setText("! 不能为空")
            return

        cursor = self.db.cursor()
        sql = """select amount, amount_payed from loans where loan_id = %s"""
        cursor.execute(sql, [loan_id])
        ret = cursor.fetchone()
        # print(ret)

        # 贷款号错误
        if ret is None:
            self.ui.ts.setText("! 贷款号错误")
            return

        self.ui.ts.setText("")

        self.loan_id = loan_id
        w = loan_pay(self)





