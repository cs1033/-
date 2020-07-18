from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.modifyClientOk import Ui_Dialog
from UI.client.modify_client_ok import client_modify_ok

class client_modify(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_modify, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.OkBtn.clicked.connect(self.Ok)

    def Ok(self):
        id = self.ui.id.text()
        #print(type(id),id)

        cursor = self.db.cursor()
        sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
        cursor.execute(sql, [id, self.id_number])
        result = cursor.fetchone()
        #print(result)

        if result is not  None:
            self.client_id = id
            w = client_modify_ok(self)

            #self.close()


        else:
            QMessageBox.information(self, '提示', '该id不属于您的客户', QMessageBox.Close, QMessageBox.Close)


