from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import random, csv, sys
from datetime import datetime
from Function import *
from share import *
from Frame import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    SI.login_window = Login()
    SI.login_window.ui.show()
    sys.exit(app.exec_())