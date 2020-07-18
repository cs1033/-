# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountModifyClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("#Dialog {border-image:url(./1.jpg);}")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(160, 110, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(10, 230, 161, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setAutoFillBackground(True)
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(Dialog)
        self.delete_2.setGeometry(QtCore.QRect(200, 230, 181, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_2.setFont(font)
        self.delete_2.setAutoFillBackground(True)
        self.delete_2.setObjectName("delete_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "修改账户关联信息"))
        self.label.setText(_translate("Dialog", "客户身份证号："))
        self.add.setText(_translate("Dialog", "增加关联"))
        self.delete_2.setText(_translate("Dialog", "取消关联"))
