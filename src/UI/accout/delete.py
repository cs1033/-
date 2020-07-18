from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.accout.accountDelete import Ui_deleteAccount


class account_delete(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(account_delete, self).__init__(parent)
        self.ui = Ui_deleteAccount()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.DeleteBtn.clicked.connect(self.Delete)


    def Delete(self):
        account_id = self.ui.id.text()
        client_id = self.ui.id_2.text()
        #print(type(id),id)

        cursor = self.db.cursor()
        sql = """ select * FROM client WHERE id_number = %s and sta_id_number = %s"""
        cursor.execute(sql, [client_id, self.id_number])
        result = cursor.fetchone()
        #print(result)

        if result is not  None:
            sql = """ select * FROM own WHERE account_number = %s and id_number = %s"""
            cursor.execute(sql, [account_id,client_id])
            result2 = cursor.fetchone()

            if result2 is None:
                QMessageBox.information(self, '提示', '该客户没有此账户', QMessageBox.Close, QMessageBox.Close)
            else:
                try:
                    sql = """select brance from account 
                            where account_number = %s"""
                    cursor.execute(sql, [account_id])
                    brance = cursor.fetchone()   # 获取待删除账户余额

                    sql = """ DELETE FROM own WHERE account_number = %s"""
                    cursor.execute(sql, [account_id])
                    sql = """ DELETE FROM account WHERE account_number = %s"""
                    cursor.execute(sql, [account_id])
                    QMessageBox.information(self, '提示', '删除成功', QMessageBox.Close, QMessageBox.Close)
                    self.db.commit()
                    sql = """select department.name from staff,department where staff.dep_department_id = department.department_id and staff.id_number = %s"""
                    cursor.execute(sql, [self.id_number])
                    sub_name = cursor.fetchone()        #获取支行名称

                    # 修改支行余额
                    sql = """update sub_branch set asset = asset - %s 
                            where name =  %s"""
                    cursor.execute(sql, [brance, sub_name[0]])
                    self.db.commit()




                    self.close()

                except:
                    QMessageBox.information(self, '提示', '删除失败', QMessageBox.Close, QMessageBox.Close)

        else:
            QMessageBox.information(self, '提示', '该id不属于您的客户', QMessageBox.Close, QMessageBox.Close)


