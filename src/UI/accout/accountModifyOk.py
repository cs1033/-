# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountModifyOk.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modifyAccountOk(object):
    def setupUi(self, modifyAccountOk):
        modifyAccountOk.setObjectName("modifyAccountOk")
        modifyAccountOk.resize(400, 300)
        modifyAccountOk.setStyleSheet("#modifyAccountOk {border-image:url(./1.jpg);}")
        self.id = QtWidgets.QLineEdit(modifyAccountOk)
        self.id.setGeometry(QtCore.QRect(150, 110, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(modifyAccountOk)
        self.label_5.setGeometry(QtCore.QRect(140, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(modifyAccountOk)
        self.label.setGeometry(QtCore.QRect(10, 110, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OkBtn = QtWidgets.QPushButton(modifyAccountOk)
        self.OkBtn.setGeometry(QtCore.QRect(150, 230, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OkBtn.setFont(font)
        self.OkBtn.setAutoFillBackground(True)
        self.OkBtn.setObjectName("OkBtn")
        self.label_2 = QtWidgets.QLabel(modifyAccountOk)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.id_2 = QtWidgets.QLineEdit(modifyAccountOk)
        self.id_2.setGeometry(QtCore.QRect(150, 160, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_2.setFont(font)
        self.id_2.setText("")
        self.id_2.setObjectName("id_2")

        self.retranslateUi(modifyAccountOk)
        QtCore.QMetaObject.connectSlotsByName(modifyAccountOk)

    def retranslateUi(self, modifyAccountOk):
        _translate = QtCore.QCoreApplication.translate
        modifyAccountOk.setWindowTitle(_translate("modifyAccountOk", "Dialog"))
        self.label_5.setText(_translate("modifyAccountOk", "修改账户"))
        self.label.setText(_translate("modifyAccountOk", "客户身份证号："))
        self.OkBtn.setText(_translate("modifyAccountOk", "确定"))
        self.label_2.setText(_translate("modifyAccountOk", "账户号"))
