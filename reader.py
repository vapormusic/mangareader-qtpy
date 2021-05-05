import mangareader
import urllib2
from bs4 import BeautifulSoup
from PyQt4 import QtCore, QtGui
import json

class Ui_MainWindowImpl(mangareader.Ui_MainWindow):

    image0 = None
    page = 0
    images = None
    url = 'https://manganelo.tv/chapter/please_dont_bully_me_nagatoro/chapter_82'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    def setupUi(self, MainWindow):
        super(Ui_MainWindowImpl, self).setupUi(MainWindow)
        # get list of images from 1 chapter ###########

        req = urllib2.Request(self.url, headers=self.hdr)
        response = urllib2.urlopen(req)
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(response, 'html.parser')
        self.images = soup.find_all('img', attrs={'class':"img-loading"})
        #print images[0]['data-src']


        # load first image #################

        self.image0 = urllib2.Request(self.images[self.page]['data-src'],headers=self.hdr)
        image0res = urllib2.urlopen(self.image0).read()
        image = QtGui.QImage()
        image.loadFromData(image0res)
        self.image.setPixmap(QtGui.QPixmap(image))

        #buttons ###########
        self.next.clicked.connect(self.nextpage)
        self.prev.clicked.connect(self.prevpage)
        self.actionExit.triggered.connect(self.actionQuit_fun)

    def nextpage(self):
        if self.page < len(self.images) :
          self.page += 1
        self.image0 = urllib2.Request(self.images[self.page]['data-src'],headers=self.hdr)    
        image0res = urllib2.urlopen(self.image0).read()
        image = QtGui.QImage()
        image.loadFromData(image0res)
        self.image.setPixmap(QtGui.QPixmap(image))

    def prevpage(self):
        if self.page > 0 :
          self.page += -1
        self.image0 = urllib2.Request(self.images[self.page]['data-src'],headers=self.hdr)    
        image0res = urllib2.urlopen(self.image0).read()
        image = QtGui.QImage()
        image.loadFromData(image0res)
        self.image.setPixmap(QtGui.QPixmap(image))  

    def actionQuit_fun(self):
        quit()      

 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindowImpl()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
