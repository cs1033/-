# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loanPayOk.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loanPayOk(object):
    def setupUi(self, loanPayOk):
        loanPayOk.setObjectName("loanPayOk")
        loanPayOk.resize(441, 252)
        loanPayOk.setStyleSheet("#loanPayOk {border-image:url(./1.jpg);}")
        self.loan_id = QtWidgets.QLineEdit(loanPayOk)
        self.loan_id.setGeometry(QtCore.QRect(130, 100, 151, 31))
        self.loan_id.setObjectName("loan_id")
        self.label_2 = QtWidgets.QLabel(loanPayOk)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(loanPayOk)
        self.label.setGeometry(QtCore.QRect(170, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setObjectName("label")
        self.Ok = QtWidgets.QPushButton(loanPayOk)
        self.Ok.setGeometry(QtCore.QRect(270, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet("color:rgb(85, 0, 0)")
        self.Ok.setObjectName("Ok")
        self.ts = QtWidgets.QLabel(loanPayOk)
        self.ts.setGeometry(QtCore.QRect(290, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ts.setFont(font)
        self.ts.setStyleSheet("color:red")
        self.ts.setText("")
        self.ts.setObjectName("ts")

        self.retranslateUi(loanPayOk)
        QtCore.QMetaObject.connectSlotsByName(loanPayOk)

    def retranslateUi(self, loanPayOk):
        _translate = QtCore.QCoreApplication.translate
        loanPayOk.setWindowTitle(_translate("loanPayOk", "Dialog"))
        self.label_2.setText(_translate("loanPayOk", "贷款号："))
        self.label.setText(_translate("loanPayOk", "支付贷款"))
        self.Ok.setText(_translate("loanPayOk", "确定"))
