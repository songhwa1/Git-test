import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import Qt

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Cultural Heritage_main.ui")[0]


#화면을 띄우는데 사용되는 Class 선언

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Sunchang.clicked.connect(self.Search_Sunchang)
        self.Gwangyang.clicked.connect(self.Search_Gwangyang)
        self.Haenam.clicked.connect(self.Search_Haenam)
        # tableWidget 수정 불가
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # tableWidget 열 넓이 조절
        self.tableWidget.setColumnWidth(0, 224)
        self.tableWidget.setColumnWidth(1, 121)
        self.tableWidget.setColumnWidth(2, 121)
        self.tableWidget.setColumnWidth(3, 121)
        self.tableWidget.setColumnWidth(4, 224)


    def Search_Sunchang(self):
        read_list = []
        with open("전라북도_순창군_문화재현황_20160630..csv", "r", encoding='cp949') as f:
            reader = csv.reader(f)
            for line in reader:
                read_list.append(line)

        self.tableWidget.setRowCount(len(read_list))


        row = 0
        for i in read_list:
            print(i)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(i[2]))    #이름
            self.tableWidget.setItem(row, 1, QTableWidgetItem(i[0]))    #지정/구분(ex.국가/도)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(i[1]))    #분류(ex.보물/무형)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(i[4]))    #번호
            self.tableWidget.setItem(row, 4, QTableWidgetItem(i[5]))    #소재지
            row += 1


    def Search_Gwangyang(self):
        read_list = list()    # 빈 리스트 생성
        with open("전라남도 광양시_문화재_20220727.csv", "r", encoding='cp949') as f:
            reader = csv.reader(f)  # 전체 파일 읽기
            for line in reader:
                read_list.append(line)       # 읽은 파일의 index(row)를 리스트화

        self.tableWidget.setRowCount(len(read_list))    # tableWidget의 행 지정

        row = 0
        for j in read_list:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(j[4]))    #이름
            self.tableWidget.setItem(row, 1, QTableWidgetItem(j[1]))    #지정/구분(ex.국가/도)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(j[2]))    #분류(ex.보물/무형)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(j[3]))    #번호
            self.tableWidget.setItem(row, 4, QTableWidgetItem(j[6]))    #소재지
            row += 1

    def Search_Haenam(self):
        read_list = []
        with open("전라남도 해남군_문화재_20220406.csv", "r", encoding='cp949') as f:
            reader = csv.reader(f)
            for line in reader:
                read_list.append(line)

        self.tableWidget.setRowCount(len(read_list))

        row = 0
        for k in read_list:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(k[1]))    #이름
            self.tableWidget.setItem(row, 1, QTableWidgetItem(k[4]))    #지정/구분(ex.국가/도)
            self.tableWidget.setItem(row, 2, QTableWidgetItem(k[5]))    #분류(ex.보물/무형)
            self.tableWidget.setItem(row, 3, QTableWidgetItem(k[4]))    #번호
            self.tableWidget.setItem(row, 4, QTableWidgetItem(k[9]))    #소재지
            row += 1





if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()