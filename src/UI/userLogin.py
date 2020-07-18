# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 262)
        Dialog.setStyleSheet("#Dialog{border-image:url(./1.jpg);}")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(170, 80, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(170, 140, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setObjectName("password")
        self.LoginBtn = QtWidgets.QPushButton(Dialog)
        self.LoginBtn.setGeometry(QtCore.QRect(170, 210, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginBtn.setFont(font)
        self.LoginBtn.setAutoFillBackground(True)
        self.LoginBtn.setObjectName("LoginBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "用户登录"))
        self.label_3.setText(_translate("Dialog", "身份证号："))
        self.label_4.setText(_translate("Dialog", "密码："))
        self.LoginBtn.setText(_translate("Dialog", "Login"))
