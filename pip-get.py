import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class TestListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.list = parent

    def rowCount(self, index):
        return 1000

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if not self.list.indexWidget(index):
                button = QtGui.QPushButton("This is item #%s" % index.row())
                self.list.setIndexWidget(index, button)
                button.setVisible(False)
            return QtCore.QVariant()

        if role == Qt.SizeHintRole:
            return QtCore.QSize(100, 50)

    def columnCount(self, index):
        pass


def main():
    app = QtGui.QApplication(sys.argv)

    window = QtGui.QWidget()

    list = QtGui.QListView()
    model = TestListModel(list)

    list.setModel(model)
    list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)

    layout = QtGui.QVBoxLayout(window)
    layout.addWidget(list)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()