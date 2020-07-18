from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.createClient import  Ui_createClient


class client_create(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_create, self).__init__(parent)
        self.ui = Ui_createClient()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.CreateBtn.clicked.connect(self.Create)

    def Create(self):
        id = self.ui.id.text()
        name = self.ui.name.text()
        phone = self.ui.phone.text()
        addr = self.ui.addr.text()
        contactName = self.ui.contactName.text()
        contactEmail = self.ui.contactEmail.text()
        contactPhone = self.ui.contactPhone.text()
        contactRelation = self.ui.contactRelation.text()


        cursor = self.db.cursor()
        sql = """ insert into client value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        if id is not None:
            try:
                cursor.execute(sql,[id,self.id_number,name,phone,addr,contactName,contactPhone,contactEmail,contactRelation])
                QMessageBox.information(self, '提示', '创建成功', QMessageBox.Close, QMessageBox.Close)
                self.db.commit()
                self.close()
            except:
                QMessageBox.information(self, '提示', '创建失败', QMessageBox.Close, QMessageBox.Close)
        else:
            QMessageBox.information(self, '提示', '创建失败,id不能为空', QMessageBox.Close, QMessageBox.Close)

