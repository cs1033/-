from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.modifyClient import modifyClient


class client_modify_ok(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_modify_ok, self).__init__(parent)
        self.ui = modifyClient()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()
        self.client_id = parent.client_id

        self.ui.ModifyBtn.clicked.connect(self.Modify)
        cursor = self.db.cursor()
        sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
        cursor.execute(sql, [self.client_id, self.id_number])
        result = cursor.fetchone()
        id, self.id_number, name, phone, addr, conname, conphone, conemial, conrelation = result
        self.ui.id.setText(id)
        self.ui.addr.setText(addr)
        self.ui.name.setText(name)
        self.ui.phone.setText(phone)
        self.ui.contactRelation.setText(conrelation)
        self.ui.contactPhone.setText(conphone)
        self.ui.contactEmail.setText(conemial)
        self.ui.contactName.setText(conname)


    def Modify(self):
        addr = self.ui.addr.text()
        name =  self.ui.name.text()
        phone =  self.ui.phone.text()
        conrelation =  self.ui.contactRelation.text()
        conphone = self.ui.contactPhone.text()
        conemial = self.ui.contactEmail.text()
        conname = self.ui.contactName.text()

        try:
            cursor = self.db.cursor()
            sql = """ UPDATE client SET  name = %s ,phonenumber = %s,addr = %s,contact_name = %s,contact_phonenumber = %s,contact_email = %s,contact_relationship = %s WHERE id_number= %s"""
            cursor.execute(sql, [name,phone,addr,conname,conphone,conemial,conrelation,self.client_id])
            result = cursor.fetchone()
            self.db.commit()
            QMessageBox.information(self, '提示', '修改成功', QMessageBox.Close, QMessageBox.Close)
            self.close()

        except:
            QMessageBox.information(self, '提示', '错误', QMessageBox.Close, QMessageBox.Close)
            self.close()


