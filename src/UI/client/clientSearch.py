# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientSearch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_clientSearch(object):
    def setupUi(self, clientSearch):
        clientSearch.setObjectName("clientSearch")
        clientSearch.resize(1188, 845)
        clientSearch.setStyleSheet("#clientSearch {border-image:url(./1.jpg);}")
        self.scrollArea = QtWidgets.QScrollArea(clientSearch)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 0, 1200, 1000))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2000, 1500))
        self.scrollAreaWidgetContents.setStyleSheet("#scrollAreaWidgetContents {border-image: url(:/1.jpg);}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Search = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Search.setGeometry(QtCore.QRect(750, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Search.setFont(font)
        self.Search.setStyleSheet("color:rgb(200, 84, 6)")
        self.Search.setObjectName("Search")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(530, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setObjectName("label")
        self.loan = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.loan.setGeometry(QtCore.QRect(50, 930, 1051, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loan.setFont(font)
        self.loan.setObjectName("loan")
        self.loan.setColumnCount(5)
        self.loan.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.loan.setHorizontalHeaderItem(4, item)
        self.loan.horizontalHeader().setDefaultSectionSize(205)
        self.ts = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ts.setGeometry(QtCore.QRect(380, 150, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ts.setFont(font)
        self.ts.setStyleSheet("color:red")
        self.ts.setText("")
        self.ts.setObjectName("ts")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(530, 540, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.account = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.account.setGeometry(QtCore.QRect(60, 580, 1051, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.account.setFont(font)
        self.account.setObjectName("account")
        self.account.setColumnCount(3)
        self.account.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.account.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account.setHorizontalHeaderItem(2, item)
        self.account.horizontalHeader().setDefaultSectionSize(250)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(520, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.text.setGeometry(QtCore.QRect(500, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setText("")
        self.text.setObjectName("text")
        self.client = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.client.setGeometry(QtCore.QRect(60, 250, 1051, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.client.setFont(font)
        self.client.setObjectName("client")
        self.client.setColumnCount(9)
        self.client.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.client.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.client.setHorizontalHeaderItem(8, item)
        self.client.horizontalHeader().setDefaultSectionSize(200)
        self.choice = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.choice.setGeometry(QtCore.QRect(360, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choice.setFont(font)
        self.choice.setObjectName("choice")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(530, 880, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(clientSearch)
        QtCore.QMetaObject.connectSlotsByName(clientSearch)

    def retranslateUi(self, clientSearch):
        _translate = QtCore.QCoreApplication.translate
        clientSearch.setWindowTitle(_translate("clientSearch", "Dialog"))
        self.Search.setText(_translate("clientSearch", "搜索"))
        self.label.setText(_translate("clientSearch", "客户搜索"))
        item = self.loan.verticalHeaderItem(0)
        item.setText(_translate("clientSearch", "1"))
        item = self.loan.verticalHeaderItem(1)
        item.setText(_translate("clientSearch", "2"))
        item = self.loan.verticalHeaderItem(2)
        item.setText(_translate("clientSearch", "3"))
        item = self.loan.verticalHeaderItem(3)
        item.setText(_translate("clientSearch", "4"))
        item = self.loan.verticalHeaderItem(4)
        item.setText(_translate("clientSearch", "5"))
        item = self.loan.horizontalHeaderItem(0)
        item.setText(_translate("clientSearch", "客户身份证"))
        item = self.loan.horizontalHeaderItem(1)
        item.setText(_translate("clientSearch", "贷款号"))
        item = self.loan.horizontalHeaderItem(2)
        item.setText(_translate("clientSearch", "贷款金额"))
        item = self.loan.horizontalHeaderItem(3)
        item.setText(_translate("clientSearch", "已发放金额"))
        self.label_3.setText(_translate("clientSearch", "客户账户信息："))
        item = self.account.verticalHeaderItem(0)
        item.setText(_translate("clientSearch", "1"))
        item = self.account.verticalHeaderItem(1)
        item.setText(_translate("clientSearch", "2"))
        item = self.account.verticalHeaderItem(2)
        item.setText(_translate("clientSearch", "3"))
        item = self.account.verticalHeaderItem(3)
        item.setText(_translate("clientSearch", "4"))
        item = self.account.verticalHeaderItem(4)
        item.setText(_translate("clientSearch", "5"))
        item = self.account.horizontalHeaderItem(0)
        item.setText(_translate("clientSearch", "客户身份证"))
        item = self.account.horizontalHeaderItem(1)
        item.setText(_translate("clientSearch", "账户号"))
        item = self.account.horizontalHeaderItem(2)
        item.setText(_translate("clientSearch", "最后访问时间"))
        self.label_2.setText(_translate("clientSearch", "客户信息："))
        item = self.client.verticalHeaderItem(0)
        item.setText(_translate("clientSearch", "1"))
        item = self.client.verticalHeaderItem(1)
        item.setText(_translate("clientSearch", "2"))
        item = self.client.verticalHeaderItem(2)
        item.setText(_translate("clientSearch", "3"))
        item = self.client.verticalHeaderItem(3)
        item.setText(_translate("clientSearch", "4"))
        item = self.client.verticalHeaderItem(4)
        item.setText(_translate("clientSearch", "5"))
        item = self.client.horizontalHeaderItem(0)
        item.setText(_translate("clientSearch", "身份证"))
        item = self.client.horizontalHeaderItem(1)
        item.setText(_translate("clientSearch", "客户经理身份证"))
        item = self.client.horizontalHeaderItem(2)
        item.setText(_translate("clientSearch", "姓名"))
        item = self.client.horizontalHeaderItem(3)
        item.setText(_translate("clientSearch", "电话"))
        item = self.client.horizontalHeaderItem(4)
        item.setText(_translate("clientSearch", "住址"))
        item = self.client.horizontalHeaderItem(5)
        item.setText(_translate("clientSearch", "联系人姓名"))
        item = self.client.horizontalHeaderItem(6)
        item.setText(_translate("clientSearch", "联系人电话"))
        item = self.client.horizontalHeaderItem(7)
        item.setText(_translate("clientSearch", "联系人邮件"))
        item = self.client.horizontalHeaderItem(8)
        item.setText(_translate("clientSearch", "联系人关系"))
        self.choice.setItemText(0, _translate("clientSearch", "户主身份证"))
        self.choice.setItemText(1, _translate("clientSearch", "客户经理身份证"))
        self.choice.setItemText(2, _translate("clientSearch", "姓名"))
        self.choice.setItemText(3, _translate("clientSearch", "电话号码"))
        self.label_4.setText(_translate("clientSearch", "客户贷款信息："))