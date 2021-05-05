# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vieta\OneDrive\Documents\mangareader\mangareader.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1072, 1448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.prev = QtGui.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(0, 0, 120, 1281))
        self.prev.setFlat(True)
        self.prev.setObjectName(_fromUtf8("prev"))
        self.next = QtGui.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(120, 0, 951, 1281))
        self.next.setFlat(True)
        self.next.setObjectName(_fromUtf8("next"))
        self.image = QtGui.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 1072, 1448))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/download.png")))
        self.image.setScaledContents(True)
        self.image.setObjectName(_fromUtf8("image"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 1280, 1071, 121))
        self.pushButton_3.setAutoRepeatDelay(299)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.image.raise_()
        self.prev.raise_()
        self.next.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionComics = QtGui.QAction(MainWindow)
        self.actionComics.setObjectName(_fromUtf8("actionComics"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionComics)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "L:A_N:application_ID:MangaReader", None))
        self.prev.setText(_translate("MainWindow", "PushButton", None))
        self.next.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionComics.setText(_translate("MainWindow", "Comics", None))

