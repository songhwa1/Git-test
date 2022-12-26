import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("CulturalHeritage.ui")[0]

class Reserve(QDialog, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarWidget.clicked.connect(self.select_date)
        self.pushButton_1.clicked.connect(self.reservation)
        self.date = self.calendarWidget.selectedDate()
        self.today = self.calendarWidget.selectedDate()
        self.rex_date = str(self.date.year()) + '/' + str(self.date.month()) + '/' + str(self.date.day())
        self.time1.setChecked(True)


    def select_date(self):
        self.date = self.calendarWidget.selectedDate()
        self.res_date = str(self.date.year()) + '/' + str(self.date.month()) + '/' + str(self.date.day())
        self.set_reserve()

    def set_reserve(self):
        res1 = 0
        res2 = 0
        res3 = 0
        with open('reservation_list.csv', 'r') as f:
            res_list = csv.reader(f)
            for i in res_list:
                if self.res_date in i:
                    if self.time1.text() in i:
                        res1 += int(i[4])
                    elif self.time2.text() in i:
                        res2 += int(i[4])
                    elif self.time3.text() in i:
                        res3 += int(i[4])
            self.reserve1.setText(str(res1))
            self.reserve2.setText(str(res2))
            self.reserve3.setText(str(res3))

    def reservation(self):
        if self.date > self.today and self.date.dayOfWeek() < 6:
            count = self.count_spinBox.text()
            res_time = 0
            if self.time1.isChecked():
                res_time = self.time1.text()
            elif self.time2.isChecked():
                res_time = self.time2.text()
            elif self.time3.isChecked():
                res_time = self.time3.text()

            word = ''+','+''+','+ self.res_date +','+ res_time + ',' + count + ','+'\n'

            with open('reservation_list.csv', 'a') as f:
                f.write(word)

            self.set_reserve()

        else:
            print('날짜 변경')


# 문화재	/ 소재지 / 날짜 / 시간 / 예약인원 /	회원 아이디

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Reserve()
    myWindow.show()
    app.exec_()