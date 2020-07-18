# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteClient(object):
    def setupUi(self, deleteClient):
        deleteClient.setObjectName("deleteClient")
        deleteClient.resize(400, 300)
        deleteClient.setStyleSheet("#deleteClient{border-image:url(./1.jpg);}")
        self.label_5 = QtWidgets.QLabel(deleteClient)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.id = QtWidgets.QLineEdit(deleteClient)
        self.id.setGeometry(QtCore.QRect(160, 110, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(deleteClient)
        self.label.setGeometry(QtCore.QRect(20, 110, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DeleteBtn = QtWidgets.QPushButton(deleteClient)
        self.DeleteBtn.setGeometry(QtCore.QRect(160, 210, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteBtn.setFont(font)
        self.DeleteBtn.setAutoFillBackground(True)
        self.DeleteBtn.setObjectName("DeleteBtn")

        self.retranslateUi(deleteClient)
        QtCore.QMetaObject.connectSlotsByName(deleteClient)

    def retranslateUi(self, deleteClient):
        _translate = QtCore.QCoreApplication.translate
        deleteClient.setWindowTitle(_translate("deleteClient", "Dialog"))
        self.label_5.setText(_translate("deleteClient", "删除客户"))
        self.label.setText(_translate("deleteClient", "客户身份证号："))
        self.DeleteBtn.setText(_translate("deleteClient", "删除"))
