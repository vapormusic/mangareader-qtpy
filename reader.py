import mangareader
import requests
from bs4 import BeautifulSoup , element
from PyQt4 import QtCore, QtGui
import json
from searchcard import SearchCardView
from PIL import Image
import hashlib
import time

class TestListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.list = parent
        self.results = []

    def inputData(self,results):
        self.results = results    

    def rowCount(self, index):
        return len(self.results)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if not self.list.indexWidget(index):
                url = self.results[index.row() ].find('a', attrs={'class':"chapter-name text-nowrap"})['href']
                title = self.results[index.row() ].find('a', attrs={'class':"chapter-name text-nowrap"}).text
                author = self.results[index.row() ].find('span', attrs={'class':"chapter-time text-nowrap"}).text
                icon = ""
                myQCustomQWidget = SearchCardView()
                myQCustomQWidget.setTextUp(title)
                myQCustomQWidget.setTextDown(author)
                myQCustomQWidget.setIcon(icon)
                myQCustomQWidget.setUrl(url)
                myQCustomQWidget.setIndex(index.row() -1)
                print(index.row())

                # # Create QListWidgetItem
                # myQListWidgetItem2 = QtGui.QListWidgetItem(self.list)
                # print(index.row() -1)
                # myQListWidgetItem2.setData(2, (index.row() -1,url)) 
                # # Set size hint
                # myQListWidgetItem2.setSizeHint(myQCustomQWidget.sizeHint())
                # # Add QListWidgetItem into QListWidget
                # self.list.addItem(myQListWidgetItem2)
                self.list.setIndexWidget(index, myQCustomQWidget)
            return QtCore.QVariant()

        if role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(1070, 150)

    def columnCount(self, index):
        pass

class Worker(QtCore.QObject):
    start = QtCore.pyqtSignal(str)
    load_chapters = QtCore.pyqtSignal(element.ResultSet)

    @QtCore.pyqtSlot()
    def processing_chapters( self, url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = requests.get(url, headers=hdr, timeout = 15)
        soup = BeautifulSoup(req.text, 'html.parser')
        preresult = soup.find('ul', attrs={'class':"row-content-chapter"})
        results = preresult.find_all('li', attrs={'class':"a-h"})
        self.load_chapters.emit(results)
        print(len(results))
    

class Ui_MainWindowImpl(mangareader.Ui_MainWindow):
 
    image0 = None
    page = 0
    images = None
    chapter_index = 0
    prevchapter_url = ''
    nextchapter_url = ''
    lastsel1 = None
    lastsel2 = None
    searchresultslist = None
    tmp_index = 0
    thread = None
    shiftbt = False
    url = 'https://manganelo.tv/chapter/please_dont_bully_me_nagatoro/chapter_82'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    def setupUi(self, MainWindow):
        super(Ui_MainWindowImpl, self).setupUi(MainWindow)
        self.next.setStyleSheet("border : 0; background-color: transparent;")
        self.prev.setStyleSheet("border : 0; background-color: transparent;")
        self.dockbar.setVisible(False)
        self.brightness_window.setVisible(False)
        #self.next.setVisible(False)
        #self.prev.setVisible(False)
        ## annoying pycui error fix
        MainWindow.setCentralWidget(self.stackedwidget)
      
        
        # get list of images from 1 chapter ###########

        # req = requests.get(self.url, headers=self.hdr, timeout = 15)        
        # ## data = json.load(response)   
        # # print response.fp.read()
        # soup = BeautifulSoup(req.text, 'html.parser')
        # self.images = soup.find_all('img', attrs={'class':"img-loading"})
        # print self.images[0]['data-src']


        # # load first image #################

        # self.image0 = requests.get(self.images[0]['data-src'],headers=self.hdr, timeout = 15 stream=True)
        # image = QtGui.QImage()
        # image.loadFromData(self.image0.content)
        
        # self.image.setPixmap(QtGui.QPixmap(image))

        #buttons ###########
        self.next.clicked.connect(self.nextpage)
        self.prev.clicked.connect(self.prevpage)
        self.actionExit.triggered.connect(self.actionQuit_fun)
        self.actionComics.triggered.connect(self.searchpage_fun)
        self.actionReader.triggered.connect(self.readerpage_fun)
        self.searchButton.clicked.connect(self.querysearch)
        self.prevchapterbt.clicked.connect(self.prev_chapter)
        self.nextchapterbt.clicked.connect(self.next_chapter)
        self.chapterlist.clicked.connect(self.chapterpage_fun)
        self.dockbutton.clicked.connect(lambda: self.dockbar.setVisible(True))
        self.brightnessbt.clicked.connect(self.getBrightness)
        self.exitbrightness.clicked.connect(lambda: self.brightness_window.setVisible(False))
        self.brightnessslider.valueChanged.connect(self.handleSlider)
        self.brightnessslider.setMinimum(0)
        self.brightnessslider.setMaximum(24)
        self.brightnessslider.setTickInterval(1)
        self.brightnessslider.setSingleStep(1)
        self.minusbrightness.setStyleSheet(self.reducebrightness)
        self.plusbrightness.setStyleSheet(self.increasebrightness)

        

        #self.tableWidget.setStyleSheet("""QTableWidget::item { font-size: 10pt }""")
        #self.tableWidget.mousePressEvent().connect(self.keyboardinput)

        #keyboard buttons ####### boilerplate
        
        self.key_q.clicked.connect( lambda:self.kbinput('q'))
        self.key_w.clicked.connect( lambda:self.kbinput('w'))
        self.key_e.clicked.connect( lambda:self.kbinput('e'))
        self.key_r.clicked.connect( lambda:self.kbinput('r'))
        self.key_t.clicked.connect( lambda:self.kbinput('t'))
        self.key_y.clicked.connect( lambda:self.kbinput('y'))
        self.key_u.clicked.connect( lambda:self.kbinput('u'))
        self.key_i.clicked.connect( lambda:self.kbinput('i'))
        self.key_o.clicked.connect( lambda:self.kbinput('o'))
        self.key_p.clicked.connect( lambda:self.kbinput('p'))
        self.key_l.clicked.connect( lambda:self.kbinput('l'))
        self.key_k.clicked.connect( lambda:self.kbinput('k'))
        self.key_j.clicked.connect( lambda:self.kbinput('j'))
        self.key_h.clicked.connect( lambda:self.kbinput('h'))
        self.key_g.clicked.connect( lambda:self.kbinput('g'))
        self.key_f.clicked.connect( lambda:self.kbinput('f'))
        self.key_d.clicked.connect( lambda:self.kbinput('d'))
        self.key_s.clicked.connect( lambda:self.kbinput('s'))
        self.key_a.clicked.connect( lambda:self.kbinput('a'))
        self.key_z.clicked.connect( lambda:self.kbinput('z'))
        self.key_x.clicked.connect( lambda:self.kbinput('x'))
        self.key_c.clicked.connect( lambda:self.kbinput('c'))
        self.key_v.clicked.connect( lambda:self.kbinput('v'))
        self.key_b.clicked.connect( lambda:self.kbinput('b'))
        self.key_n.clicked.connect( lambda:self.kbinput('n'))
        self.key_m.clicked.connect( lambda:self.kbinput('m'))
        self.key_bksp.clicked.connect( lambda:self.kbinput('bksp'))
        self.key_shift.clicked.connect( lambda:self.kbinput('shift'))
        self.key_space.clicked.connect( lambda:self.kbinput('space'))
        self.key_entr.clicked.connect( lambda:self.kbinput('enter'))
        
    
    def nextpage(self):
        if self.dockbar.isVisible() :
            self.dockbar.setVisible(False)
            print 'ok'
        else:    
         if self.page < len(self.images) -1:
          self.page += 1
          self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr, timeout = 15)    
          image = QtGui.QImage()
          image.loadFromData(self.image0.content)
          self.image.setPixmap(QtGui.QPixmap(image))
         else:
          self.next_chapter()
    


    def prevpage(self):
        if self.dockbar.isVisible() :
            self.dockbar.setVisible(False)
        else:   
         if self.page > 0 :
          self.page += -1
          self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr, timeout = 15)    
          image = QtGui.QImage()
          image.loadFromData(self.image0.content)
          self.image.setPixmap(QtGui.QPixmap(image))
         else:
          self.prev_chapter()      

    def next_chapter(self):
          if self.nextchapter_url != '' :
            self.launchreader(self.nextchapter_url)
          else:
            QtGui.QMessageBox.about(QtGui.QMainWindow(), "L:A_N:application_ID:Last Chapter",
            "<H1>Latest chapter!</H1>".decode("utf8"))  

    def prev_chapter(self):        
          if self.prevchapter_url != '':  
            print self.prevchapter_url          
            self.launchreader(self.prevchapter_url)
          else:
            QtGui.QMessageBox.about(QtGui.QMainWindow(), "L:A_N:application_ID:Last Chapter",
            "<H1>First chapter!</H1>".decode("utf8"))  

    def kbinput(self, char):

        # text = self.mangaSearch.text()
         if len(char) == 1:  
            if self.shiftbt == True: 
                char = char.upper()
            key = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,QtGui.QKeySequence.fromString(str(char))[0],QtCore.Qt.NoModifier,QtCore.QString(char))
            QtCore.QCoreApplication.sendEvent(self.mangaSearch,key)
         elif char == 'space':
            key = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,QtGui.QKeySequence.fromString(str(" "))[0],QtCore.Qt.NoModifier,QtCore.QString(str(" ")))
            QtCore.QCoreApplication.sendEvent(self.mangaSearch,key)
         elif char == "bksp":
            key = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,QtCore.Qt.Key_Backspace,QtCore.Qt.NoModifier)
            QtCore.QCoreApplication.sendEvent(self.mangaSearch,key)  
         elif char == "shift":
            if self.shiftbt == True: 
             self.shiftbt = False
             self.key_shift.setStyleSheet("""""") 
            else: 
             self.shiftbt = True
             self.key_shift.setStyleSheet("""QPushButton{background-color: black;color: white;}""")  
         elif char == "enter":
             self.querysearch() 

    def increasebrightness(self):
        val = int(self.brightnessslider.value())
        if val < 24:
            self.brightnessslider.setValue(val + 1)

    def reducebrightness(self)
        val = int(self.brightnessslider.value())
        if val < 0:
            self.brightnessslider.setValue(val - 1)

    def getBrightness(self):
        import subprocess
        brightness_level = subprocess.check_output('lipc-get-prop com.lab126.powerd flIntensity', shell=True)
        self.brightnessslider.setValue(int(brightness_level))
        self.brightness_window.setVisible(True)         

    def handleSlider(self, val):
        self.setFlIntensity(val)        

    def setFlIntensity(self , level):
        import os
        os.system("lipc-set-prop com.lab126.powerd flIntensity "+ str(int(level)))
        
    def querysearch(self):
        self.searchlist.clear()
        text = self.mangaSearch.text()
        linkurl = str('https://manganelo.tv/search/'+str(text))
        req = requests.get(linkurl, headers=self.hdr, timeout = 15)
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.find_all('div', attrs={'class':"search-story-item"})   
        if len(results) != 0:
            for result in results:
                url = result.find('a', attrs={'class':"item-img"})['href']
                title = result.find('a', attrs={'class':"item-img"})['title'] 
                author = result.find('span', attrs={'class':"text-nowrap item-author"})['title']
                icon = result.find('img', attrs={'class':"img-loading"})['src']
                myQCustomQWidget = SearchCardView()
                myQCustomQWidget.setTextUp(title)
                myQCustomQWidget.setTextDown(author)
                myQCustomQWidget.setIcon(icon)
                myQCustomQWidget.setUrl(url)

                # Create QListWidgetItem
                myQListWidgetItem = QtGui.QListWidgetItem(self.searchlist)
                data = (url , title, author, icon)
                myQListWidgetItem.setData(1, data)
                # Set size hint
                myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                # Add QListWidgetItem into QListWidget
                self.searchlist.addItem(myQListWidgetItem)
                self.searchlist.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.searchlist.itemClicked.connect(self.mangainfo)


    def mangainfo(self, item):
       data = item.data(1).toPyObject()        
       if data != self.lastsel2:
        print(data)
        url = str('https://manganelo.tv')+ data[0]
        title = data[1]
        author = data[2]
        icon = str('https://manganelo.tv')+ data[3]
     
        self.stackedwidget.setCurrentIndex(2)
        self.infotext.setText(title)
        infoimage0 = requests.get(icon,headers=self.hdr, timeout = 15)    
        image = QtGui.QImage()
        image.loadFromData(infoimage0.content)
        self.infoimage.setPixmap(QtGui.QPixmap(image)) 
        try:
         self.thread.terminate()
         self.infochapters.setModel(None)
         self.infochapters.scrollToTop()
        except Exception as e:
         print e   
            
        self.worker = Worker()
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread) 
        self.thread.started.connect(lambda: self.worker.processing_chapters(url))     
        self.worker.load_chapters.connect(self.load_list)
        self.thread.start()

    @QtCore.pyqtSlot(element.ResultSet)
    def load_list(self, results):
        print('ok')
        if len(results) != 0:
            self.tmp_index = -1
            model = TestListModel(self.infochapters)
            model.inputData(results)
            self.infochapters.setModel(model)   
            self.infochapters.clicked.connect(self.saveRes2)


    def saveRes2(self, index): 
        self.launchreader(self.infochapters.model().results[index.row()].find('a', attrs={'class':"chapter-name text-nowrap"})['href'])


        

    def saveRes(self, item): 
        print 'bruh'
        data = item.data(2).toPyObject() 
        if data != self.lastsel2:
          self.lastsel2 = data
          data = item.data(2).toPyObject()     
          self.chapter_index = data[1]
          self.launchreader(data[1])

    def launchreader(self,url):
        self.url = url
        req = requests.get(str('https://manganelo.tv')+ self.url, headers=self.hdr,  timeout = 15)        
        ## data = json.load(response)   
        # print response.fp.read()
        #def xstr(s):
        #    if s is None:
        #       return ''
        #    return str(s)
        soup = BeautifulSoup(req.text, 'html.parser')
        self.images = soup.find_all('img', attrs={'class':"img-loading"})
        prev_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-prev a-h"})
        next_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-next a-h"})
        prev_lk = ''
        next_lk = ''
        if prev_element is not None : prev_lk = prev_element['href']
        if next_element is not None : next_lk = next_element['href']        
        self.prevchapter_url = str(prev_lk)
        self.nextchapter_url = str(next_lk)

        print self.prevchapter_url
        print self.nextchapter_url

        # load first image #################
        self.page = 0
        self.image0 = requests.get(self.images[0]['data-src'],headers=self.hdr, timeout = 15, stream=True)
        image = QtGui.QImage()
        image.loadFromData(self.image0.content)
        self.image0.close()
        self.image.setPixmap(QtGui.QPixmap(image))
        self.stackedwidget.setCurrentIndex(0)  



    def actionQuit_fun(self):
        quit()   

    def searchpage_fun(self):
        self.dockbar.setVisible(False)
        self.stackedwidget.setCurrentIndex(1)
        
    def readerpage_fun(self):
        self.dockbar.setVisible(False)
        self.stackedwidget.setCurrentIndex(0)             

    def chapterpage_fun(self):
        self.dockbar.setVisible(False)
        self.stackedwidget.setCurrentIndex(2)    
 

if __name__ == "__main__":
    import sys
    print(QtGui.QImageReader.supportedImageFormats())
    if len(QtGui.QImageReader.supportedImageFormats()) < 10: 
        #windows
        QtCore.QCoreApplication.addLibraryPath('C:\\Python27\\Lib\\site-packages\\PyQt4\\plugins') 
        #kindle
        QtCore.QCoreApplication.addLibraryPath('/mnt/us/python/lib/python2.7/site-packages/PyQt4/plugins')
    else:
        pass 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindowImpl()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


