from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import psutil
import urllib.request

# Variables for use in the size() function.
KB = float(1024)
MB = float(KB ** 2) # 1,048,576
GB = float(KB ** 3) # 1,073,741,824
TB = float(KB ** 4) # 1,099,511,627,776

def size(B):
	
	B = float(B)
	if B < KB: return f"{B} Byte/s"
	elif KB <= B < MB: return f"{B/KB:.2f} kb/s"
	elif MB <= B < GB: return f"{B/MB:.2f} mb/s"
	elif GB <= B < TB: return f"{B/GB:.2f} gb/s"
	elif TB <= B: return f"{B/TB:.2f} tb/s"



class mainwindow(QMainWindow):
    def update1(self):
        
        self.counter = psutil.net_io_counters()

        self.upload = self.counter.bytes_sent
        self.download = self.counter.bytes_recv
        self.total = self.upload + self.download

        if self.last_upload > 0:
            if self.upload < self.last_upload:
                self.upload_speed = 0
            else:
                self.upload_speed = self.upload - self.last_upload
        if self.last_download > 0:
            if self.download < self.last_download:
                self.down_speed = 0
            else:
                self.down_speed = self.download - self.last_download
        self.last_upload = self.upload
        self.last_download = self.download

        self.uploading.setText(str(size(self.upload_speed))+" Up")
        self.downloading.setText(str(size(self.down_speed))+" Down")
        # print(size(self.upload_speed))
        

    def connect(self, host='http://google.com'):
            try:
                urllib.request.urlopen(host)
                return True
            except:
                return False
    def recall(self):
        if self.connect()==True:
            self.net = QPixmap('green.png')
        else:
            self.net = QPixmap('yellow.png')
        self.pixmap5 = self.net.scaled(64, 64)
        self.pixmap1 = self.net.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap1)
        self.label.move(55,54)

    def __init__(self):
        
        super().__init__()
        self.last_upload, self.last_download, self.upload_speed, self.down_speed = 0, 0, 0, 0
        # setGeometry(left, top, width, height)
        self.setGeometry(1600, 920, 500, 350)
            # self.res , self.sent, self.total = band()
        self.uploading = QLabel("Calculating...", self)
        self.uploading.setFont(QFont('Tw Cen MT Condensed Extra Bold', 15))
        self.uploading.setStyleSheet("color: rgb(255,255,255)")
        # setGeometry(left, top, width, height)
        self.uploading.setGeometry(100, 30, 330, 30)
        self.uploading.setWordWrap(True)

        self.downloading = QLabel("Calculating...", self)
        self.downloading.setFont(QFont('Tw Cen MT Condensed Extra Bold', 15))
        self.downloading.setStyleSheet("color: rgb(255,255,255)")
        # setGeometry(left, top, width, height)
        self.downloading.setGeometry(100, 70, 330, 30)
        self.downloading.setWordWrap(True)

        # self.net.setGeometry(100, 70, 30, 30)
        self.label = QLabel(self)
        if self.connect()==True:
            self.net = QPixmap('green.png')
        else:
            self.net = QPixmap('yellow.png')
        # self.pixmap5 = self.net.scaled(64, 64)
        self.pixmap1 = self.net.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap1)
        self.label.move(55,54)

        self.timerTime = QtCore.QTimer(self)
        self.timerTime.timeout.connect(self.recall)
        self.timerTime.start(300)


        self.timerTime = QtCore.QTimer(self)
        self.timerTime.timeout.connect(self.update1)
        self.timerTime.start(300)

        
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        

app = QApplication(sys.argv)

window = mainwindow()
window.show()
# style = """ 
#         QLabel{
#             color:#ffffff;
#             -webkit-text-stroke: 1px black;
#         }
#         """
# app.setStyleSheet(style)
# app.setStyleSheet(style)
app.exec_()