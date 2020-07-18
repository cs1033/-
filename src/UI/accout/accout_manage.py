from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.accout.accountManage import Ui_accountManage
from UI.accout.add import account_add
from UI.accout.delete import account_delete
from UI.accout.modify_ok import account_modify
from UI.accout.search import account_search
from alarm import alarmMessageBox

class account_manage(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_manage, self).__init__(parent)
        self.ui = Ui_accountManage()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.back.clicked.connect(self.back)
        self.ui.add.clicked.connect(self.add)
        self.ui.cut.clicked.connect(self.delete)
        self.ui.modify.clicked.connect(self.modify)
        self.ui.search.clicked.connect(self.search)


    def back(self):
        self.close()
        self.parent.show()

    def add(self):
        w = account_add(self)

    def delete(self):
        alarmMessageBox(self, "若是支票账户，需要先付清透支额！")
        w = account_delete(self)


    def modify(self):
        w = account_modify(self)
        a = 1

    def search(self):
        w = account_search(self)

