import csv
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("CulturalHeritage.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class Sub_Window(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 시그널과 슬롯 연결
        self.calendarWidget.clicked.connect(self.Choice_Date)
        self.reserve_pb.clicked.connect(self.Reserve)
        self.cancel_pb.clicked.connect(self.cancel)
        self.home_pb.clicked.connect(self.close)


        # 슬롯
        today = QDate.currentDate()
        tomorrow = today.addDays(1)
        self.calendarWidget.setMinimumDate(tomorrow)
        self.count = 1
        # 예약인원 초기화
        self.Choice_Date()
        self.Update_People()
        self.res = self.Update_People()
        self.reserve1.setNum(int(self.res[0]))
        self.reserve2.setNum(int(self.res[1]))
        self.reserve3.setNum(int(self.res[2]))


# 예약 순서
# 날짜 선택 : 날짜 마다 예약 인원 수 다름, 이전 날짜, 주말은 선택 불가
# csv파일 읽어서 날짜 정보 확인, 같은 날짜가 있으면 예약 인원 수 로 세팅, 없으면 0
# 인원 선택 : 누적되어야함
# 스핀박스 값 추출(csv 파일에 저장예정), 라벨에 반영, 누적 시킴, 30명 초과 시 제한
# 시간 선택
# 라디오 버튼 텍스트값 추출(csv 파일에 저장예정)
# 예약버튼 누르기
# csv 파일에 저장 (예약날짜, 인원, 시간)

    # 날짜 선택 시그널과 연결할 함수
    def Choice_Date(self):
        # 선택한 날짜 정보 문자열로 반환
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        # 함수 불러오기
        self.Update_People()    # 총 예약 인원 보여줌
        self.Weekend()      # 주말 선택 시 예약 불가 알림창
        self.res = self.Update_People()
        self.reserve1.setNum(int(self.res[0]))
        self.reserve2.setNum(int(self.res[1]))
        self.reserve3.setNum(int(self.res[2]))

    # 총 예약 인원을 보여주는 함수
    def Update_People(self):
        list = []   # 빈 리스트 만들어 줌
        # 시간대 별 총 예약 인원 수 저장할 변수
        num1 = 0
        num2 = 0
        num3 = 0

        #파일 열어서 리스트에 정보 저장
        with open("reserve_list.csv", "r", newline="\n", encoding='cp949') as f:
            reader = csv.reader(f)
            for line in reader:
                list.append(line)

        # 리스트에서 원하는 정보 찾기
        for i in range(len(list)):
            # Choice_Date()에서 불러온 self.date(선택한 날짜)
            if self.date == list[i][0]:     # list[i][0] = 날짜
                if list[i][2] == '11:00~12:30':     # list[i][2] = 시간
                    num1 += int(list[i][1])     # 총 예약 인원 구하는 식

                elif list[i][2] == '14:00~15:30':
                    num2 += int(list[i][1])

                elif list[i][2] == '16:00~17:30':
                    num3 += int(list[i][1])
        # label에 정보 세팅
        self.reserve1.setNum(num1)
        self.reserve2.setNum(num2)
        self.reserve3.setNum(num3)
        return num1, num2, num3

    # 주말은 예약 할 수 없게 하는 함수
    def Weekend(self):
        day = self.calendarWidget.selectedDate()    # 선택한 날짜
        self.weekend = day.dayOfWeek()      # .dayOfWeek() = 요일값 반환(월~일=1~7)
        if self.weekend == 6 or self.weekend == 7:
            QMessageBox.critical(self, "예약 불가", "주말은 예약 할  수 없습니다")

    # 현재 선택한 예약 인원
    def Choice_People(self):
        self.count = self.count_spinBox.value()

    # 30명이상 예약시 예약불가
    def limitPeople(self):
        # init에서 가져온 온 총 예약인원
        res0 = int(self.res[0])
        res1 = int(self.res[1])
        res2 = int(self.res[2])
        if res0 > 30:
            res0 -= self.count   # 이전 예약 인원수 구하는 식
            QMessageBox.critical(self, "정원 초과", "예약 인원이 초과 되었습니다.")
            self.reserve1.setNum(res0)

        elif res1 > 30:
            res1 -= self.count
            QMessageBox.critical(self, "정원 초과", "예약 인원이 초과 되었습니다.")
            self.reserve2.setNum(res1)

        elif res2 > 30:
            res2 -= self.count
            QMessageBox.critical(self, "정원 초과", "예약 인원이 초과 되었습니다.")
            self.reserve3.setNum(res2)

    # 총인원 + 현재 예약인원 값 구하는 함수 (30명 제한 시 필요)
    def calPeople(self):
        self.cal1 = self.count + int(self.res[0])
        self.cal2 = self.count + int(self.res[1])
        self.cal3 = self.count + int(self.res[2])


    # 선택한 시간 반환
    def Choice_time(self):
        # 선택된 라디오박스의 시간대 변수에 저장
        if self.time1.isChecked() == True:
            self.choice_time = self.time1.text()

        elif self.time2.isChecked() == True:
            self.choice_time = self.time2.text()

        elif self.time3.isChecked() == True:
            self.choice_time = self.time3.text()

    # 예약 정보(날짜, 인원, 시간) 파일에 저장, 주말은 정보저장 x
    def Reserve(self):
        # 주말에 예약한 정보는 저장x
        self.calPeople()
        if self.weekend == 6 or self.weekend == 7:
            QMessageBox.critical(self, "예약 불가", "주말은 예약 할  수 없습니다")

        # 30명 초과시 정보 저장 x , calPeople()에서 불러온 self.cal1~3
        elif self.cal1 > 30 or self.cal2 > 30 or self.cal3 > 30:
            self.limitPeople()

        else:
            # 예약 버튼 누르고 난 후 시간대 마다 총 예약인원 보여주기 위해 함수 불러옴
            self.Choice_People()    # 선택한 예약 인원 수 보여줌
            self.Choice_time()
            # 파일에 정보 추가
            with open("reserve_list.csv", "a", newline="\n", encoding='cp949') as f:
                line = csv.writer(f)
                line.writerow([self.date, self.count, self.choice_time])
            QMessageBox.information(self, "알림", "예약 완료 되었습니다")
            self.Update_People()    # 총 예약 인원을 보여주는 함수

# 예약취소
# 날짜 선택 > 인원 선택 > 시간 선택 > 정보 대조 파일에 있으면 삭제 후 다시 쓰기

    def cancel(self):
        list = []   # 이중 리스트, 읽어온 파일 정보(리스트) 저장
        index = []  # 이중 리스트, 지울 정보
        self.Choice_Date()
        self.Choice_time()

        with open("reserve_list.csv", "r", newline="\n", encoding='cp949') as f:
            reader = csv.reader(f)
            for line in reader:
                list.append(line)

        # 리스트에서 지울 정보 찾기
        for i in list:      # i = 리스트 [날짜 , 인원, 시간]
            if self.date in i[0] and self.choice_time in i[2]:
                index.append(i)

        with open("reserve_list.csv", "w", newline="\n", encoding='cp949') as f:
                writer = csv.writer(f)
                for line in list:
                    if line not in index:
                        writer.writerow(line)
                    elif line in index:
                        pass
        self.Update_People()


# if __name__ == "__main__":
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     #WindowClass의 인스턴스 생성
#     myWindow = Sub_Window()
#
#     #프로그램 화면을 보여주는 코드
#     myWindow.show()
#
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()