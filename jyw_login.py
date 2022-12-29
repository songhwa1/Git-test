import csv
# import sys

from PyQt5.QtGui import QIntValidator   # 라인 에디터 숫자만 입력 받기 위해
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("jyw_login.ui")[0]


class LoginClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_SW.setCurrentIndex(0)
        self.csv = list()
        self.csv_list()
        self.check1 = False
        self.check2 = False
        self.id = ''
        self.phone_lineEdit.setValidator(QIntValidator(self))  # 밸리 데이터 를 사용 하여 라인 에디터 숫자만 입력 받기

        self.Home1_Button.clicked.connect(self.close)
        self.login_Button.clicked.connect(self.login)
        self.signup_Button.clicked.connect(self.page2)

        self.Home2_Button.clicked.connect(self.page1)
        self.duplication_Button.clicked.connect(self.reduplication)
        self.join_Button.clicked.connect(self.signup)
        self.agree1_checkBox.clicked.connect(self.agree_set)

    def page1(self):
        self.clear()
        self.login_SW.setCurrentIndex(0)

    def page2(self):
        self.login_SW.setCurrentIndex(1)

    def csv_list(self):
        self.csv = list()
        with open('Userinfo .csv', 'r', newline='') as f:
            csv_list = csv.reader(f)
            for i in csv_list:
                self.csv.append(i)

    def login(self):
        self.csv_list()
        success = False
        user_id = self.login_id_lineEdit.text()
        password = self.login_pw_lineEdit.text()
        if user_id and password:
            for i in self.csv:
                if user_id == i[0] and password == i[1]:
                    success = True
        if success:
            self.id = user_id
            QMessageBox.about(self, '안내창', '로그인 성공')
            self.close()
        else:
            self.clear()
            QMessageBox.critical(self, '안내창', '로그인 실패')

    def clear(self):
        self.login_id_lineEdit.clear()
        self.login_pw_lineEdit.clear()
        self.name_lineEdit.clear()
        self.id_lineEdit.clear()
        self.pw_lineEdit.clear()
        self.pw2_lineEdit.clear()
        self.phone_lineEdit.clear()
        self.address_lineEdit.clear()
        self.agree1_checkBox.setCheckState(False)
        self.agree2_checkBox.setCheckState(False)
        self.agree3_checkBox.setCheckState(False)
        self.agree4_checkBox.setCheckState(False)

    def agree_set(self):
        if self.agree1_checkBox.checkState():
            self.agree2_checkBox.setCheckState(True)
            self.agree3_checkBox.setCheckState(True)
            self.agree4_checkBox.setCheckState(True)
        else:
            self.agree2_checkBox.setCheckState(False)
            self.agree3_checkBox.setCheckState(False)
            self.agree4_checkBox.setCheckState(False)

    def signup(self):
        self.password()
        user_name = self.name_lineEdit.text()
        user_id = self.id_lineEdit.text()
        password = self.pw_lineEdit.text()
        phon = self.phone_lineEdit.text()
        address = self.address_lineEdit.text()
        agree1 = self.agree1_checkBox.checkState()
        agree2 = self.agree2_checkBox.checkState()
        agree3 = self.agree3_checkBox.checkState()
        user_list = [user_id, password, user_name, phon, address]
        if user_name and phon and address and agree1 and agree2 and agree3 and self.check1 and self.check2:
            with open('Userinfo .csv', 'a', newline='') as f:
                word = csv.writer(f)
                word.writerow(user_list)
            QMessageBox.about(self, '안내창', '가입 완료')
            self.page1()
        elif not self.check2:
            return
        elif not user_id:
            QMessageBox.critical(self, '안내창', '아이디 를 입력 하세요.')
        elif not self.check1:
            QMessageBox.critical(self, '안내창', '아이디 중복 확인을 하세요.')
        elif not agree1:
            QMessageBox.critical(self, '안내창', '약관에 동의 하세요')
        elif not address:
            QMessageBox.critical(self, '안내창', '주소를 입력 하세요')
        elif not phon:
            QMessageBox.critical(self, '안내창', '전화 번호를 입력 하세요')
        elif not user_name:
            QMessageBox.critical(self, '안내창', '이름을 입력 하세요')

    def password(self):
        success = False
        password1 = self.pw_lineEdit.text()
        password2 = self.pw2_lineEdit.text()
        if not password1:
            QMessageBox.critical(self, '안내창', '비밀 번호를 입력 하세요')
        elif not password2:
            QMessageBox.critical(self, '안내창', '비밀 번호 확인을 입력 하세요')
        elif password1 == password2:
            success = True
        else:
            QMessageBox.critical(self, '안내창', '비밀 번호가 다르게 입력됨')
        self.check2 = success

    def reduplication(self):
        success = True
        user_id = self.id_lineEdit.text()
        if user_id:
            for i in self.csv:
                if user_id == i[0]:
                    success = False
            if success:
                self.duplication_Button.setText('사용 가능')
                QMessageBox.about(self, '안내창', '아이디 사용 가능')
            else:
                self.duplication_Button.setText('중복 확인')
                QMessageBox.critical(self, '안내창', '아이디 중복')

        self.check1 = success


# 아이디/ 비밀 번호/ 이름/ 연락처/ 주소
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = loginClass()
#     myWindow.show()
#     app.exec_()
