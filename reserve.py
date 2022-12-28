import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cancel import cancelclass

form_class = uic.loadUiType("CulturalHeritage.ui")[0]

#------------연결시 주석처리
# name = 'aaa'
# address = 'bbb'
# id = 'ccc'
# id = 'ddd'
#------------------------
class Reserve(QDialog, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calendarWidget.clicked.connect(self.select_date)
        self.reserve_pb.clicked.connect(self.reservation)
        self.cancel_pb.clicked.connect(self.cancel_page)
        self.home_pb.clicked.connect(self.gohome)

        self.date = self.calendarWidget.selectedDate()
        self.today = self.calendarWidget.selectedDate()
        self.res_date = str(self.date.year()) + '/' + str(self.date.month()) + '/' + str(self.date.day())
        self.time1.setChecked(True)
        #--------------------연결시 주석처리
        # self.name_set(name)
        # self.address_set(address)
        # self.id_set(id)
        #---------------------------------
        self.hide_date()

    def hide_date(self):
        self.maxday = self.today.addDays(100)
        self.calendarWidget.setDateRange(self.today.addDays(1), self.maxday)

    def select_date(self):
        self.date = self.calendarWidget.selectedDate()
        self.res_date = str(self.date.year()) + '/' + str(self.date.month()) + '/' + str(self.date.day())
        self.set_reserve()

    def set_reserve(self):
        res1 = self.reserve1_text()
        res2 = self.reserve2_text()
        res3 = self.reserve3_text()
        self.reserve1.setText(str(res1))
        self.reserve2.setText(str(res2))
        self.reserve3.setText(str(res3))

    def reserve1_text(self):
        res = 0
        with open('reservation_list.csv', 'r') as f:
            res_list = csv.reader(f)
            for i in res_list:
                if self.res_date in i and self.name in i and self.address in i:
                    if self.time1.text() in i:
                        res += int(i[4])
        return res

    def reserve2_text(self):
        res = 0
        with open('reservation_list.csv', 'r') as f:
            res_list = csv.reader(f)
            for i in res_list:
                if self.res_date in i and self.name in i and self.address in i:
                    if self.time2.text() in i:
                        res += int(i[4])
        return res

    def reserve3_text(self):
        res = 0
        with open('reservation_list.csv', 'r') as f:
            res_list = csv.reader(f)
            for i in res_list:
                if self.res_date in i and self.name in i and self.address in i:
                    if self.time3.text() in i:
                        res += int(i[4])
        return res

    def reservation(self):
        if self.date.dayOfWeek() < 6:
            count = self.count_spinBox.text()
            res_time = ''
            res = 0
            if self.time1.isChecked():
                res_time = self.time1.text()
                res = self.reserve1_text()
            elif self.time2.isChecked():
                res_time = self.time2.text()
                res = self.reserve2_text()
            elif self.time3.isChecked():
                res_time = self.time3.text()
                res = self.reserve3_text()

            if res+int(count) <= 30:
                word = self.name + ',' + self.address + ',' + self.res_date + ',' + res_time + ',' + count + ',' + self.id + '\n'
                with open('reservation_list.csv', 'a', newline='') as f:
                    f.write(word)
                self.set_reserve()
                QMessageBox.about(self, '안내창', '예약이 완료 되었습니다.')
            else:
                QMessageBox.about(self, '안내창', '정원 초과 입니다. 인원 또는 시간을 변경 하세요.')

        else:
            QMessageBox.about(self, '안내창', '주말입니다. 예약 날짜를 변경 하세요.')

    def cancel(self):
        cancel_count = 0
        reservation = list()
        # haed_list =['문화재', '소재지', '날짜', '시간', '예약인원', '회원 아이디']
        with open('reservation_list.csv', 'r') as f:
            res_list = csv.reader(f)
            for i in res_list:
                if self.id not in i and '' not in i and i:
                    reservation.append(i)
                if self.id in i:
                    cancel_count = 1
        with open('reservation_list.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            if reservation:
                for i in reservation:
                    writer.writerow(i)
        self.set_reserve()
        if cancel_count:
            QMessageBox.about(self, '안내창', '예약이 취소 되었습니다.')
        else:
            QMessageBox.about(self, '안내창', '예약 이력이 없습니다.')

    def cancel_page(self):
        self.can = cancelclass(self.id)
        # self.can.set_id(self.id)
        self.can.exec_()

    def gohome(self):
        # QMessageBox.about(self, '안내창', '메인창으로')
        self.close()

    def name_set(self, name):
        self.name = name

    def address_set(self, address):
        self.address = address

    def id_set(self, id):
        self.id = id


# 문화재	/ 소재지 / 날짜 / 시간 / 예약인원 /	회원 아이디

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = Reserve()
#     myWindow.show()
#     app.exec_()