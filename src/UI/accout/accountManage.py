# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountManage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_accountManage(object):
    def setupUi(self, accountManage):
        accountManage.setObjectName("accountManage")
        accountManage.resize(400, 300)
        accountManage.setStyleSheet("#accountManage{border-image:url(./1.jpg);}")
        self.modify = QtWidgets.QPushButton(accountManage)
        self.modify.setGeometry(QtCore.QRect(40, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.modify.setFont(font)
        self.modify.setObjectName("modify")
        self.cut = QtWidgets.QPushButton(accountManage)
        self.cut.setGeometry(QtCore.QRect(250, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cut.setFont(font)
        self.cut.setObjectName("cut")
        self.search = QtWidgets.QPushButton(accountManage)
        self.search.setGeometry(QtCore.QRect(250, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.back = QtWidgets.QPushButton(accountManage)
        self.back.setGeometry(QtCore.QRect(140, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.add = QtWidgets.QPushButton(accountManage)
        self.add.setGeometry(QtCore.QRect(40, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add.setFont(font)
        self.add.setObjectName("add")

        self.retranslateUi(accountManage)
        QtCore.QMetaObject.connectSlotsByName(accountManage)

    def retranslateUi(self, accountManage):
        _translate = QtCore.QCoreApplication.translate
        accountManage.setWindowTitle(_translate("accountManage", "Dialog"))
        self.modify.setText(_translate("accountManage", "修改"))
        self.cut.setText(_translate("accountManage", "销户"))
        self.search.setText(_translate("accountManage", "查询"))
        self.back.setText(_translate("accountManage", "返回"))
        self.add.setText(_translate("accountManage", "开户"))
