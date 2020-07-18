# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pylab as mpl     #import matplotlib as mpl

from PyQt5.QtWidgets import QDialog, QMessageBox,QTableWidgetItem
from UI.Ui_business import Ui_business
from alarm import alarmMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class business(QDialog):
    "A dialog class for Ui_LoginDialog, who can show itself"

    def __init__(self, parent):
        super(business, self).__init__(parent)
        self.ui = Ui_business()
        self.ui.setupUi(self)

        self.parent = parent
        self.db = parent.db
        self.id_number = parent.id_number
        self.show()

        self.ui.statistics.clicked.connect(self.statistics)

        

    def clear(self):
        self.ui.client_num.setRowCount(0)
        self.ui.loan.setRowCount(0)
        self.ui.save.setRowCount(0)

    def statistics(self):
        choice = self.ui.choice.currentText()
        
        cursor = self.db.cursor()
        sql1 = """"""
        sql2 = """"""
        sql3 = """SELECT sub_branch.name, count(client.id_number ) FROM client,  staff, department, sub_branch
                WHERE client.sta_id_number = staff.id_number and staff.dep_department_id = department.department_id and department.name = sub_branch.name
                group by sub_branch.name
                """

        if choice == "本月":
            #搜索支行贷款业务
            sql1 = """SELECT name, sum(amount  ) FROM loans WHERE DATE_FORMAT( loan_date, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )
                    group by name
                    """
            #搜索储蓄业务
            sql2 = """SELECT sub_bank_name, sum(brance ) FROM account WHERE DATE_FORMAT(start_date, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' ) and account_type = 1
                        group by sub_bank_name
                      """
        
        if choice == "本季度":
            #搜索支行贷款业务
            sql1 = """SELECT name, sum(amount  ) FROM loans 
                    WHERE QUARTER(loan_date) = QUARTER(now())
                    group by name
                    """
            #搜索储蓄业务
            sql2 = """SELECT sub_bank_name, sum(brance ) FROM account 
                        WHERE QUARTER(start_date) = QUARTER(now()) and account_type = 1
                        group by sub_bank_name
                      """

        if choice == "本年":
            #搜索支行贷款业务
            sql1 = """SELECT name, sum(amount  ) FROM loans 
                    WHERE YEAR(loan_date) = YEAR(now())
                    group by name
                    """
            #搜索储蓄业务
            sql2 = """SELECT sub_bank_name, sum(brance ) FROM account 
                        WHERE YEAR(start_date) = YEAR(now()) and account_type = 1
                        group by sub_bank_name
                      """

        

        cursor.execute(sql1)
        tab1 = cursor.fetchall()
        # print("1")
        cursor.execute(sql2)
        tab2 = cursor.fetchall()
        # print("2")
        cursor.execute(sql3)
        tab3 = cursor.fetchall()

        # print("3")
        self.printTable(tab1, tab2, tab3)
        self.printGraph(tab1, tab2, tab3)

 #打印表格
    def printTable(self, tab1, tab2, tab3):
        self.clear()
        #打印贷款信息
        for i in range(len(tab1)):
            self.ui.loan.insertRow(i)
            for j in range(2):
                item = QTableWidgetItem(str(tab1[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.loan.setItem(i, j, item)
            self.ui.loan.setRowCount(i+1)


        #打印储蓄信息
        for i in range(len(tab2)):
            self.ui.save.insertRow(i)
            for j in range(2):
                item = QTableWidgetItem(str(tab2[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.save.setItem(i, j, item)

            self.ui.save.setRowCount(i + 1)

        # 打印user number
        for i in range(len(tab3)):
            self.ui.client_num.insertRow(i)
            for j in range(2):
                item = QTableWidgetItem(str(tab3[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.client_num.setItem(i, j, item)

            self.ui.client_num.setRowCount(i + 1)


#打印图表
    def printGraph(self, tab1, tab2, tab3):
        ax1 = plt.subplot(3,1,1)
        ax2 = plt.subplot(3,1,2)
        ax3 = plt.subplot(3,1,3)
        # 三个子图

        x = list(range(len(tab1)))
        x1 = list(range(len(tab2)))
        x2 = list(range(len(tab3)))
        #x = ["ss", 's', 's', 's', 'a', 'a', 'a']
        width = 0.4

        ticks, ticks1, ticks2 = [], [], []
        num_list, num_list1, num_list2 = [], [], []
        for item in tab1:
            ticks.append(item[0])
            num_list.append(item[1])
        for item in tab2:
            ticks1.append(item[0])
            num_list1.append(item[1])        
        for item in tab3:
            ticks2.append(item[0])
            num_list2.append(item[1])

        plt.sca(ax1)
        plt.bar(x, num_list, width=width, label='贷款',fc = 'y')
        plt.legend()
        plt.ylabel("金额")
        plt.xticks(x, ticks)
        plt.title("贷款", y=-0.1)
       
        plt.sca(ax2)
        plt.bar(x1, num_list1, width=width, fc = 'r',label='储蓄')
        plt.xticks(x1, ticks1)
        plt.ylabel("金额")
        plt.title("储蓄", y=-0.1)

        plt.sca(ax3)
        plt.bar(x2, num_list2, width=width, fc = 'b', label='用户')
        plt.xticks(x2, ticks2)
        plt.ylabel("人数")
        plt.title("用户数", y=-0.1)

        plt.show()
        # plt.ion()
        # plt.pause(100)
        # plt.close()
        
