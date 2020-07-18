from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.deleteClient import Ui_deleteClient


class client_delete(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_delete, self).__init__(parent)
        self.ui = Ui_deleteClient()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.DeleteBtn.clicked.connect(self.Delete)

    def Delete(self):
        id = self.ui.id.text()
        #print(type(id),id)

        cursor = self.db.cursor()
        sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
        cursor.execute(sql, [id, self.id_number])
        result = cursor.fetchone()
        #print(result)

        if result is not  None:
            sql = """ DELETE FROM client WHERE id_number = %s and sta_id_number = %s"""
            try:
                cursor.execute(sql, [id,self.id_number])
                #re = cursor.fetchone()
                #print(re)
                QMessageBox.information(self, '提示', '删除成功', QMessageBox.Close, QMessageBox.Close)
                self.db.commit()
                self.close()

            except:
                QMessageBox.information(self, '提示', '删除失败', QMessageBox.Close, QMessageBox.Close)

        else:
            QMessageBox.information(self, '提示', '该id不属于您的客户', QMessageBox.Close, QMessageBox.Close)


