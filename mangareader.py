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
        MainWindow.setEnabled(True)
        MainWindow.resize(1072, 1448)
        self.stackedwidget = QtGui.QStackedWidget(MainWindow)
        self.stackedwidget.setObjectName(_fromUtf8("stackedwidget"))
        self.centralwidget = QtGui.QWidget()
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dockbutton = QtGui.QPushButton(self.centralwidget)
        self.dockbutton.setGeometry(QtCore.QRect(0, 1280, 1072, 121))
        self.dockbutton.setAutoRepeatDelay(299)
        self.dockbutton.setFlat(True)
        self.dockbutton.setObjectName(_fromUtf8("dockbutton"))
        self.next = QtGui.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(130, 0, 951, 1281))
        self.next.setFlat(True)
        self.next.setObjectName(_fromUtf8("next"))
        self.prev = QtGui.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(0, 0, 120, 1281))
        self.prev.setFlat(True)
        self.prev.setObjectName(_fromUtf8("prev"))
        self.image = QtGui.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 1072, 1448))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/download.png")))
        self.image.setScaledContents(True)
        self.image.setObjectName(_fromUtf8("image"))
        self.image.raise_()
        self.dockbutton.raise_()
        self.next.raise_()
        self.prev.raise_()
        self.stackedwidget.addWidget(self.centralwidget)
        self.centralwidget2 = QtGui.QWidget()
        self.centralwidget2.setEnabled(True)
        self.centralwidget2.setObjectName(_fromUtf8("centralwidget2"))
        self.mangaSearch = QtGui.QLineEdit(self.centralwidget2)
        self.mangaSearch.setGeometry(QtCore.QRect(20, 10, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.mangaSearch.setFont(font)
        self.mangaSearch.setObjectName(_fromUtf8("mangaSearch"))
        self.searchButton = QtGui.QPushButton(self.centralwidget2)
        self.searchButton.setGeometry(QtCore.QRect(440, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchlist = QtGui.QListWidget(self.centralwidget2)
        self.searchlist.setGeometry(QtCore.QRect(0, 130, 1071, 1241))
        self.searchlist.setObjectName(_fromUtf8("searchlist"))
        self.stackedwidget.addWidget(self.centralwidget2)
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
        self.actionReader = QtGui.QAction(MainWindow)
        self.actionReader.setObjectName(_fromUtf8("actionReader"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionComics)
        self.menuFile.addAction(self.actionReader)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "L:A_N:application_ID:MangaReader", None))
        self.dockbutton.setText(_translate("MainWindow", "PushButton", None))
        self.next.setText(_translate("MainWindow", "PushButton", None))
        self.prev.setText(_translate("MainWindow", "PushButton", None))
        self.mangaSearch.setText(_translate("MainWindow", "Manga here", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionComics.setText(_translate("MainWindow", "Comics", None))
        self.actionReader.setText(_translate("MainWindow", "Reader", None))

