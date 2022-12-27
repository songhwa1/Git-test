import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from reserve import Reserve

form_class = uic.loadUiType("Cultural Heritage_main.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Gwangyang.clicked.connect(self.gwangyang_list)
        self.Haenam.clicked.connect(self.haenam)
        self.Sunchang.clicked.connect(self.haenam)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.doubleClicked.connect(self.reserve)
        self.column = 5

    def reserve(self):
        second = Reserve()
        second.exec_()

    def gwangyang_list(self):
        # 이름 4,지정 1,분류 2,번호 3,소재지 6,
        list_G = list()
        with open('전라남도 광양시_문화재_20220727.csv', 'r') as f:
            list1 = csv.reader(f)
            for i in list1:
                list_G.append(i)
        self.tableWidget.setRowCount(len(list_G)-1)
        self.tableWidget.setColumnCount(self.column)
        for i in range(1, len(list_G)):
            self.tableWidget.setItem(i-1, 0, QTableWidgetItem(list_G[i][4]))
            self.tableWidget.setItem(i-1, 1, QTableWidgetItem(list_G[i][1]))
            self.tableWidget.setItem(i-1, 2, QTableWidgetItem(list_G[i][2]))
            self.tableWidget.setItem(i-1, 3, QTableWidgetItem(list_G[i][3]))
            self.tableWidget.setItem(i-1, 4, QTableWidgetItem(list_G[i][6]))

    def haenam(self):
        # 이름 1,지정 4,분류 5,번호 3,소재지 9
        list_G = list()
        with open('전라남도 해남군_문화재_20220406.csv', 'r') as f:
            list1 = csv.reader(f)
            for i in list1:
                list_G.append(i)
        self.tableWidget.setRowCount(len(list_G)-1)
        self.tableWidget.setColumnCount(self.column)
        for i in range(1, len(list_G)):
            self.tableWidget.setItem(i-1, 0, QTableWidgetItem(list_G[i][1]))
            self.tableWidget.setItem(i-1, 1, QTableWidgetItem(list_G[i][4]))
            self.tableWidget.setItem(i-1, 2, QTableWidgetItem(list_G[i][5]))
            self.tableWidget.setItem(i-1, 3, QTableWidgetItem(list_G[i][3]))
            self.tableWidget.setItem(i-1, 4, QTableWidgetItem(list_G[i][9]))

    def sunchang(self):
        # 이름 2,지정 0,분류 1,번호 4,소재지 5
        list_G = list()
        with open('전라북도_순창군_문화재현황_20160630.csv', 'r') as f:
            list1 = csv.reader(f)
            for i in list1:
                list_G.append(i)
        self.tableWidget.setRowCount(len(list_G)-1)
        self.tableWidget.setColumnCount(self.column)
        for i in range(1, len(list_G)):
            self.tableWidget.setItem(i-1, 0, QTableWidgetItem(list_G[i][2]))
            self.tableWidget.setItem(i-1, 1, QTableWidgetItem(list_G[i][0]))
            self.tableWidget.setItem(i-1, 2, QTableWidgetItem(list_G[i][1]))
            self.tableWidget.setItem(i-1, 3, QTableWidgetItem(list_G[i][4]))
            self.tableWidget.setItem(i-1, 4, QTableWidgetItem(list_G[i][5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()