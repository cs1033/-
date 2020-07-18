from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.client.clientManage import  Ui_clientManage
from UI.client.create_client import client_create
from UI.client.delete_client import client_delete
from UI.client.modify_client import client_modify
from UI.client.search import client_search

class client_manage(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(client_manage, self).__init__(parent)
        self.ui = Ui_clientManage()
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
        w = client_create(self)

    def delete(self):
        w = client_delete(self)

    def modify(self):
        w = client_modify(self)
        #print("end modify")
        #self.show()


#todo :增加client_search
    def search(self):
        w = client_search(self)
