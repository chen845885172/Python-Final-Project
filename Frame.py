from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import random, csv, sys
from datetime import datetime
from Function import *
from share import *


class Login:
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("login.ui")
        self.ui.Login_button.clicked.connect(self.login)
        self.ui.applybutton.clicked.connect(self.apply)
        self.ui.find_button.clicked.connect(self.find)
        self.ui.password.returnPressed.connect(self.login)
        users = []
        passwords = []
        with open("用户账号.csv", encoding='GBK') as fp:
            reader = csv.reader(fp)
            for user in reader:
                users.append(user)
        with open("用户密码.csv", encoding='GBK') as fp:
            reader = csv.reader(fp)
            for password in reader:
                passwords.append(password)
        self.users = users[1:]
        self.passwords = passwords[1:]
        self.res = len(self.users)

    def apply(self):
        SI.apply_window = Apply()
        SI.apply_window.ui.show()
        self.ui.close()

    def find(self):
        SI.find_window = Find()
        SI.find_window.ui.show()
        self.ui.close()

    def login(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()
        count = -1
        for user in self.users:
            count += 1
            user_str = "".join(user)
            if user_str == username:
                password_str = "".join(self.passwords[count])
                if password_str == password:
                    SI.second_window = Stats()
                    SI.second_window.ui.show()
                    self.ui.close()
                    break
                else:
                    QMessageBox.about(self.ui,
                                      f'失败',
                                      f'密码错误'
                                      )
                    return
        if count == self.res - 1:
            QMessageBox.about(self.ui,
                              f'失败',
                              f'账号输入错误'
                              )
            return


class Apply:
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Apply.ui")
        self.ui.apply_Button.clicked.connect(self.apply)
        users = []
        with open("用户账号.csv", encoding='GBK') as fp:
            reader = csv.reader(fp)
            for user in reader:
                users.append(user)
        self.users = users[1:]

    def apply(self):
        username = self.ui.user_Edit.text().strip()
        password = self.ui.pass_Edit.text().strip()
        repeat = self.ui.repeat_Edit.text().strip()
        for user in self.users:
            user_str = "".join(user)
            if user_str == username:
                QMessageBox.about(
                    self.ui,
                    f'失败',
                    f'账号已存在'
                )
                # break
                return
        if password != repeat:
            QMessageBox.about(self.ui,
                              f'账号申请失败',
                              f'两次输入的密码不一样'
                              )
            return
        else:
            user1 = []
            user1.append(int(username))
            password1 = []
            password1.append(int(password))
            with open("用户账号.csv", 'a', encoding='GBK') as fp:
                content = csv.writer(fp)
                content.writerow(user1)
                fp.flush()
            with open("用户密码.csv", 'a', encoding='GBK') as fp:
                content = csv.writer(fp)
                content.writerow(password1)
                fp.flush()
            QMessageBox.about(self.ui,
                              f'成功',
                              f'账号申请成功'
                              )
            SI.login_window = Login()
            SI.login_window.ui.show()
            self.ui.close()


class Find:
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("findback.ui")
        self.ui.find_Button.clicked.connect(self.find)
        users = []
        passwords = []
        with open("用户账号.csv", encoding='GBK') as fp:
            reader = csv.reader(fp)
            for user in reader:
                users.append(user)
        with open("用户密码.csv", encoding='GBK') as fp:
            reader = csv.reader(fp)
            for password in reader:
                passwords.append(password)
        self.users = users[1:]
        self.passwords = passwords[1:]
        self.res = len(self.users)

    def find(self):
        username = self.ui.user_Edit.text().strip()
        repeat = self.ui.re_Edit.text().strip()
        if username != repeat:
            QMessageBox.about(self.ui,
                              f'失败',
                              f'两次输入的账号不一样'
                              )
            return
        else:
            count=-1
            for user in self.users:
                count+=1
                user_str = "".join(user)
                if user_str == username:
                    password_str = "".join(self.passwords[count])
                    QMessageBox.about(self.ui,
                                      f'失败',
                                      '密码为：'+password_str+",别再忘了!")
                    break
            SI.login_window = Login()
            SI.login_window.ui.show()
            self.ui.close()

            if count == self.res - 1:
                QMessageBox.about(
                    self.ui,
                    f'失败',
                    f'这个账号没有注册过,回去申请吧!')
                return


