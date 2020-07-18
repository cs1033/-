from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QMessageBox,QTableWidgetItem


def alarmMessageBox(self, alarm):
    self.alarm = alarm
    QMessageBox.information(self, '提示', self.alarm, QMessageBox.Ok, QMessageBox.Ok)