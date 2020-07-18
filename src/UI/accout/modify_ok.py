from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.accout.accountModifyOk import Ui_modifyAccountOk
from UI.accout.modify import account_modify_ok

class account_modify(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_modify, self).__init__(parent)
        self.ui = Ui_modifyAccountOk()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.OkBtn.clicked.connect(self.Ok)

    def Ok(self):
        account_id = self.ui.id_2.text()
        client_id = self.ui.id.text()

        if account_id == "" or client_id == "":     #输入为空
            QMessageBox.information(self, '提示', '请输入完整', QMessageBox.Close, QMessageBox.Close)
            return

        cursor = self.db.cursor()
        sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
        cursor.execute(sql, [client_id, self.id_number])
        result = cursor.fetchone()

        if result is None:      #不属于自己的客户
            QMessageBox.information(self, '提示', '该id不属于您的客户', QMessageBox.Close, QMessageBox.Close)
            return

        sql = """ select * FROM own WHERE account_number = %s and id_number = %s"""
        cursor.execute(sql, [account_id, client_id])
        result2 = cursor.fetchone()

        if result2 is None:
            QMessageBox.information(self, '提示', '该客户没有此账户', QMessageBox.Close, QMessageBox.Close)
            return

        self.account_id = account_id
        self.client_id = client_id
        w = account_modify_ok(self)







