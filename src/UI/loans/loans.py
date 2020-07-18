# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loans.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loans(object):
    def setupUi(self, loans):
        loans.setObjectName("loans")
        loans.resize(400, 300)
        loans.setStyleSheet("#loans{border-image:url(./1.jpg);}")
        self.add = QtWidgets.QPushButton(loans)
        self.add.setGeometry(QtCore.QRect(50, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.cut = QtWidgets.QPushButton(loans)
        self.cut.setGeometry(QtCore.QRect(260, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cut.setFont(font)
        self.cut.setObjectName("cut")
        self.pay = QtWidgets.QPushButton(loans)
        self.pay.setGeometry(QtCore.QRect(260, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pay.setFont(font)
        self.pay.setObjectName("pay")
        self.back = QtWidgets.QPushButton(loans)
        self.back.setGeometry(QtCore.QRect(150, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.search = QtWidgets.QPushButton(loans)
        self.search.setGeometry(QtCore.QRect(50, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search.setFont(font)
        self.search.setObjectName("search")

        self.retranslateUi(loans)
        QtCore.QMetaObject.connectSlotsByName(loans)

    def retranslateUi(self, loans):
        _translate = QtCore.QCoreApplication.translate
        loans.setWindowTitle(_translate("loans", "Dialog"))
        self.add.setText(_translate("loans", "增加贷款"))
        self.cut.setText(_translate("loans", "删除贷款"))
        self.pay.setText(_translate("loans", "支付贷款"))
        self.back.setText(_translate("loans", "返回"))
        self.search.setText(_translate("loans", "查询贷款"))
