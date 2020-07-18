# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loanDelete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loanDelete(object):
    def setupUi(self, loanDelete):
        loanDelete.setObjectName("loanDelete")
        loanDelete.resize(467, 286)
        loanDelete.setStyleSheet("#loanDelete{border-image:url(./1.jpg);}")
        self.label = QtWidgets.QLabel(loanDelete)
        self.label.setGeometry(QtCore.QRect(190, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loanDelete)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loan_id = QtWidgets.QLineEdit(loanDelete)
        self.loan_id.setGeometry(QtCore.QRect(150, 110, 151, 31))
        self.loan_id.setObjectName("loan_id")
        self.ts = QtWidgets.QLabel(loanDelete)
        self.ts.setGeometry(QtCore.QRect(310, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ts.setFont(font)
        self.ts.setStyleSheet("color:red")
        self.ts.setText("")
        self.ts.setObjectName("ts")
        self.Delete = QtWidgets.QPushButton(loanDelete)
        self.Delete.setGeometry(QtCore.QRect(310, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Delete.setFont(font)
        self.Delete.setStyleSheet("color:rgb(85, 0, 0)")
        self.Delete.setObjectName("Delete")
        self.label_3 = QtWidgets.QLabel(loanDelete)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:blue")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(loanDelete)
        QtCore.QMetaObject.connectSlotsByName(loanDelete)

    def retranslateUi(self, loanDelete):
        _translate = QtCore.QCoreApplication.translate
        loanDelete.setWindowTitle(_translate("loanDelete", "Dialog"))
        self.label.setText(_translate("loanDelete", "删除贷款"))
        self.label_2.setText(_translate("loanDelete", "贷款号："))
        self.Delete.setText(_translate("loanDelete", "删除"))
        self.label_3.setText(_translate("loanDelete", "(提示：不能删除处于发放中的贷款)"))
