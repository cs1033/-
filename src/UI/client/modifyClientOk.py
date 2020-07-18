# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyClientOk.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("#Dialog{border-image:url(./1.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 110, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OkBtn = QtWidgets.QPushButton(Dialog)
        self.OkBtn.setGeometry(QtCore.QRect(150, 210, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OkBtn.setFont(font)
        self.OkBtn.setAutoFillBackground(True)
        self.OkBtn.setObjectName("OkBtn")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(150, 110, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "客户身份证号："))
        self.OkBtn.setText(_translate("Dialog", "确定"))
        self.label_5.setText(_translate("Dialog", "修改客户"))
