# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vieta\OneDrive\Documents\mangareader\keyboard.ui'
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
        MainWindow.resize(1068, 350)
        MainWindow.setMinimumSize(QtCore.QSize(875, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../AppData/Local/IIT Jodhpur UGRI/Software/AIIMS Logo 32X32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, -1, -1, 11)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 11, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(4, 13, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action1_Graph = QtGui.QAction(MainWindow)
        self.action1_Graph.setObjectName(_fromUtf8("action1_Graph"))
        self.action2_Graph = QtGui.QAction(MainWindow)
        self.action2_Graph.setObjectName(_fromUtf8("action2_Graph"))
        self.action4_Graph = QtGui.QAction(MainWindow)
        self.action4_Graph.setObjectName(_fromUtf8("action4_Graph"))
        self.actionAuthor = QtGui.QAction(MainWindow)
        self.actionAuthor.setObjectName(_fromUtf8("actionAuthor"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addAction(self.actionStop)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.action1_Graph)
        self.menuView.addAction(self.action2_Graph)
        self.menuView.addAction(self.action4_Graph)
        self.menuAbout.addAction(self.actionInfo)
        self.menuAbout.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Brain Keyboard", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "~ `", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "! 1", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "@ 2", None))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "# 3", None))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "$ 4", None))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "% 5", None))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "^ 6", None))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "& 7", None))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "* 8", None))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "( 9", None))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("MainWindow", ") 0", None))
        item = self.tableWidget.item(0, 11)
        item.setText(_translate("MainWindow", "- _", None))
        item = self.tableWidget.item(0, 12)
        item.setText(_translate("MainWindow", "+ =", None))
        item = self.tableWidget.item(0, 13)
        item.setText(_translate("MainWindow", "BkSp", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Tab", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Q", None))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "W", None))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "E", None))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "R", None))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "T", None))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("MainWindow", "Y", None))
        item = self.tableWidget.item(1, 7)
        item.setText(_translate("MainWindow", "U", None))
        item = self.tableWidget.item(1, 8)
        item.setText(_translate("MainWindow", "I", None))
        item = self.tableWidget.item(1, 9)
        item.setText(_translate("MainWindow", "O", None))
        item = self.tableWidget.item(1, 10)
        item.setText(_translate("MainWindow", "P", None))
        item = self.tableWidget.item(1, 11)
        item.setText(_translate("MainWindow", "{ [", None))
        item = self.tableWidget.item(1, 12)
        item.setText(_translate("MainWindow", "} ]", None))
        item = self.tableWidget.item(1, 13)
        item.setText(_translate("MainWindow", "| \\", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Caps Lock", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "A", None))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "S", None))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "D", None))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", "F", None))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("MainWindow", "G", None))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("MainWindow", "H", None))
        item = self.tableWidget.item(2, 7)
        item.setText(_translate("MainWindow", "J", None))
        item = self.tableWidget.item(2, 8)
        item.setText(_translate("MainWindow", "K", None))
        item = self.tableWidget.item(2, 9)
        item.setText(_translate("MainWindow", "L", None))
        item = self.tableWidget.item(2, 10)
        item.setText(_translate("MainWindow", ": ;", None))
        item = self.tableWidget.item(2, 11)
        item.setText(_translate("MainWindow", "\" \'", None))
        item = self.tableWidget.item(2, 12)
        item.setText(_translate("MainWindow", "Enter", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Shift", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "Z", None))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "X", None))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "C", None))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("MainWindow", "V", None))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("MainWindow", "B", None))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("MainWindow", "N", None))
        item = self.tableWidget.item(3, 7)
        item.setText(_translate("MainWindow", "M", None))
        item = self.tableWidget.item(3, 8)
        item.setText(_translate("MainWindow", "< ,", None))
        item = self.tableWidget.item(3, 9)
        item.setText(_translate("MainWindow", "> .", None))
        item = self.tableWidget.item(3, 10)
        item.setText(_translate("MainWindow", "? /", None))
        item = self.tableWidget.item(3, 11)
        item.setText(_translate("MainWindow", "Shift", None))
        item = self.tableWidget.item(3, 12)
        item.setText(_translate("MainWindow", "Up", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Ctrl", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "Fn", None))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "Win", None))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "Alt", None))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("MainWindow", "Space", None))
        item = self.tableWidget.item(4, 9)
        item.setText(_translate("MainWindow", "Alt", None))
        item = self.tableWidget.item(4, 10)
        item.setText(_translate("MainWindow", "Ctrl", None))
        item = self.tableWidget.item(4, 11)
        item.setText(_translate("MainWindow", "Left", None))
        item = self.tableWidget.item(4, 12)
        item.setText(_translate("MainWindow", "Down", None))
        item = self.tableWidget.item(4, 13)
        item.setText(_translate("MainWindow", "Right", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.action1_Graph.setText(_translate("MainWindow", "Inspiration Graph", None))
        self.action2_Graph.setText(_translate("MainWindow", "Expiration Graph", None))
        self.action4_Graph.setText(_translate("MainWindow", "Compliance Curve", None))
        self.actionAuthor.setText(_translate("MainWindow", "Developer", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
