# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
from PIL import Image
import numpy 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1712, 934)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 150, 1031, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cam = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cam.setObjectName("cam")
        self.verticalLayout.addWidget(self.cam)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(1160, 850, 171, 51))
        self.start.setObjectName("start")
        self.Trigger = QtWidgets.QPushButton(self.centralwidget)
        self.Trigger.setGeometry(QtCore.QRect(1440, 850, 171, 51))
        self.Trigger.setObjectName("Trigger")
        self.Model = QtWidgets.QComboBox(self.centralwidget)
        self.Model.setGeometry(QtCore.QRect(1440, 180, 181, 31))
        geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        self.Model.addItems(geek_list)
        self.Model.setObjectName("Model")
        # self.Model.addItem("")
        # self.Model.addItem("")
        # self.Model.addItem("")
        # self.Model.addItem("")
        self.Pos = QtWidgets.QComboBox(self.centralwidget)
        self.Pos.setGeometry(QtCore.QRect(1440, 270, 181, 31))
        self.Pos.setObjectName("Pos")
        self.perc_ent = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.perc_ent.setGeometry(QtCore.QRect(1440, 360, 181, 31))
        self.perc_ent.setObjectName("perc_ent")
        self.Model_number = QtWidgets.QLabel(self.centralwidget)
        self.Model_number.setGeometry(QtCore.QRect(1120, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Model_number.setFont(font)
        self.Model_number.setObjectName("Model_number")
        self.Position = QtWidgets.QLabel(self.centralwidget)
        self.Position.setGeometry(QtCore.QRect(1120, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Position.setFont(font)
        self.Position.setObjectName("Position")
        self.Percentage = QtWidgets.QLabel(self.centralwidget)
        self.Percentage.setGeometry(QtCore.QRect(1120, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Percentage.setFont(font)
        self.Percentage.setObjectName("Percentage")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1100, 410, 601, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.img.setObjectName("img")
        self.verticalLayout_2.addWidget(self.img)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cam.setText(_translate("MainWindow", "cam"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.Trigger.setText(_translate("MainWindow", "Trigger"))
        # geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        # self.Model.addItem(geek_list)
        # self.Model.setItemText(0, _translate("MainWindow", "RR20"))
        # self.Model.setItemText(1, _translate("MainWindow", "RR28"))
        # self.Model.setItemText(2, _translate("MainWindow", "RT34"))
        # self.Model.setItemText(3, _translate("MainWindow", "RT37"))
        self.Model_number.setText(_translate("MainWindow", "Model Number"))
        self.Position.setText(_translate("MainWindow", "Camera Position"))
        self.Percentage.setText(_translate("MainWindow", "Percentage"))
        self.img.setText(_translate("MainWindow", "TextLabel"))
        self.start.clicked.connect(self.Initialize)
        self.Trigger.clicked.connect(self.trigger)

    def Initialize(self):
        # scale_percent = 60
        cam_1 = cv2.VideoCapture('test.mp4')
        # cam_1 = cv2.VideoCapture(0)
        while True:
            ret, self.img = cam_1.read()
            # print(ret)
            if not ret:
                print("Where is Camera ?")

            image = self.resized(self.img, 60)
            # width = int(self.img.shape[1] * scale_percent / 100)
            # height = int(self.img.shape[0] * scale_percent / 100)
            # dim = (width, height)
            
            # # resize image
            # self.resized = cv2.resize(self.img, dim, interpolation = cv2.INTER_AREA)

            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            print(h, w)
            bytes_per_line = ch * w
            convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
            # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, QtCore.Qt.KeepAspectRatio)
            # self.image = convert_to_Qt_format.copy()
            self.cam.setPixmap(QtGui.QPixmap.fromImage(convert_to_Qt_format))

            cv2.waitKey(0)

    def resized(self, img, scale):
        width = int(img.shape[1] * scale / 100)
        height = int(img.shape[0] * scale / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return resized

    def trigger(self):
        # print(type(self.resized))
        img_1 = self.img
        
        cv2.imwrite("trigger.jpg", img_1)
        img = cv2.imread('trigger.jpg')
        img = self.resized(img, 25)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_img.shape
        s = ch * w
        print(h, w)
        
        convert_to_Qt= QtGui.QImage(rgb_img.data, w, h, s, QtGui.QImage.Format_RGB888)
        # p = convert_to_Qt.scaled(551, 381, QtCore.Qt.KeepAspectRatio)
        # self.image = p.copy()
        im = Image.fromarray(numpy.uint8(convert_to_Qt))
        cv2.imshow("L", img)
        self.img.setPixmap(QtGui.QPixmap.fromImage(im))
        cv2.waitKey(0)


        

          
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
