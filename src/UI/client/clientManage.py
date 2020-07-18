# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientManage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_clientManage(object):
    def setupUi(self, clientManage):
        clientManage.setObjectName("clientManage")
        clientManage.resize(427, 272)
        clientManage.setStyleSheet("#clientManage{border-image:url(./1.jpg);}")
        self.add = QtWidgets.QPushButton(clientManage)
        self.add.setGeometry(QtCore.QRect(40, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.modify = QtWidgets.QPushButton(clientManage)
        self.modify.setGeometry(QtCore.QRect(40, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.modify.setFont(font)
        self.modify.setObjectName("modify")
        self.cut = QtWidgets.QPushButton(clientManage)
        self.cut.setGeometry(QtCore.QRect(250, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cut.setFont(font)
        self.cut.setObjectName("cut")
        self.search = QtWidgets.QPushButton(clientManage)
        self.search.setGeometry(QtCore.QRect(250, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.back = QtWidgets.QPushButton(clientManage)
        self.back.setGeometry(QtCore.QRect(140, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back.setFont(font)
        self.back.setObjectName("back")

        self.retranslateUi(clientManage)
        QtCore.QMetaObject.connectSlotsByName(clientManage)

    def retranslateUi(self, clientManage):
        _translate = QtCore.QCoreApplication.translate
        clientManage.setWindowTitle(_translate("clientManage", "Dialog"))
        self.add.setText(_translate("clientManage", "新增客户"))
        self.modify.setText(_translate("clientManage", "修改客户"))
        self.cut.setText(_translate("clientManage", "删除客户"))
        self.search.setText(_translate("clientManage", "查询"))
        self.back.setText(_translate("clientManage", "返回"))
