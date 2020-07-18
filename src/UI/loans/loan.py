from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.loans.loans import Ui_loans
from UI.loans.add import loan_add
from UI.loans.delete import loan_delete
from UI.loans.payOk import loan_pay_ok
from UI.loans.search import loan_search

class loan_manage(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(loan_manage, self).__init__(parent)
        self.ui = Ui_loans()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.back.clicked.connect(self.back)
        self.ui.add.clicked.connect(self.add)
        self.ui.cut.clicked.connect(self.delete)
        self.ui.pay.clicked.connect(self.pay)
        self.ui.search.clicked.connect(self.search)


    def back(self):
        self.close()
        #self.parent.show()

    def add(self):
        w = loan_add(self)
        a = 1

    def delete(self):
        w = loan_delete(self)
        a = 1


    def pay(self):
        w = loan_pay_ok(self)
        a = 1


    def search(self):
        w = loan_search(self)

