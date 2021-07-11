from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import random, csv, sys
from datetime import datetime
from share import *


class Stats(QMainWindow):
    bool_start = False
    list_samples = []

    def __init__(self):
        # 把csv内容读入 对象属性
        rows = []
        with open('学生名单.csv', encoding='GBK') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        self.rows = rows[1:]
        # 从文件中加载UI定义
        super().__init__()
        self.ui = uic.loadUi("Function.ui")
        self.ui.pB_Start.clicked.connect(self.pB_Start)
        self.ui.pB_Save.clicked.connect(self.pB_Save)
        self.ui.pB_Show.clicked.connect(self.pB_Show)
        self.ui.pB_Quit.clicked.connect(self.pB_Quit)
        self.ui.pB_Insert.clicked.connect(self.pB_Insert)
        rownum = len(self.rows)
        self.ui.lE_Total.setText(str(rownum))

    # 抽样
    def pB_Start(self):
        num = self.ui.inputlabel.text().strip()
        self.sample = random.sample(self.rows, int(num))
        print(type(self.sample))
        print(self.sample)


        showText = ''
        for row in self.sample:
            showText += f'{"    ".join(row)}\n'
        print(showText)
        self.ui.Browser.setPlainText(showText)

    # 保存抽样数据
    def pB_Save(self):
        # 将本次抽样追加记录“学生名单.csv”的新列，抽中的名单标记“抽中”，没有抽中的不标记
        if not self.sample:
            QMessageBox.about(self.ui,
                              f'失败',
                              f'你还没有抽样呢!'
                              )
            return
        prefix = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'sample{prefix}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.sample)

        QMessageBox.about(self.ui,
                          f'成功',
                          f'已经保存到 sample{prefix}.csv'
                          )

    # 显示全班名单
    def pB_Show(self):
        showText = ''
        for row in self.rows:
            showText += f'{"    ".join(row)}\n'

        self.ui.Browser.setPlainText(showText)

    def pB_Insert(self):
        text=[]
        with open('学生信息.csv', 'r') as p:
            reader = csv.DictReader(p)
            for row in reader:
                new_row=list(row.values())
                text.append(new_row)
        with open(f'学生名单.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(text)
            f.flush()
        QApplication.processEvents()
        QMessageBox.about(self.ui,
                          f'成功',
                          f'导入成功'
                          )


    def pB_Quit(self):
        sys.exit()
