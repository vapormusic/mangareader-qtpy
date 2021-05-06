import sys
from PyQt4 import QtGui, QtCore
import keyboard
import pynput

class stackedExample(keyboard.Ui_MainWindow):

   def setupUi(self, MainWindow):
      super(stackedExample, self).setupUi(MainWindow)
      self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
      self.tableWidget.selectionModel().selectionChanged.connect(self.keyboardinput)

   def keyboardinput(self, selected , deselected):
      for index in selected:
        print self.tableWidget.selectedItems()[0].text()
        if len(self.tableWidget.selectedItems()[0].text()) = 1
        
		  
		
def main():
   app = QtGui.QApplication(sys.argv)
   MainWindow = QtGui.QMainWindow()
   ui = stackedExample()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()