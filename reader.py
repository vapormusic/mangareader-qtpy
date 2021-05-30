import mangareader
import requests
from bs4 import BeautifulSoup , element
from PyQt4 import QtCore, QtGui
import json
from searchcard import SearchCardView
from PIL import Image
import hashlib
import time
import requests_cache
import AbstractMangaSource
import mangasources
urls_expire_after = {
    'manganelo.tv/manga': 300,
    'manganelo.tv/mangaimages': 1800,
    'cm.blazefast.co': 3600,
    'nhanhtruyen.net': 3600,
    '*': 0,
}
requests_cache.install_cache('demo_cache',urls_expire_after=urls_expire_after)
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
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
                url = self.results[index.row() ].getUrl()
                title = self.results[index.row() ].getTitle()
                author = self.results[index.row() ].getAuthor()
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

class TestListModel2(QtCore.QAbstractListModel):
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

                title = str(self.results[index.row()][:str(self.results[index.row()]).rfind("y:_$W|~_:q")])
                url = self.results[index.row()][len(title+"y:_$W|~_:q"):]
                icon = ""
                myQCustomQWidget = SearchCardView()
                myQCustomQWidget.setTextUp(title)
                myQCustomQWidget.setTextDown(url)
                myQCustomQWidget.setIcon(icon)
                myQCustomQWidget.setUrl("")
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
            return QtCore.QSize(1070, 100)

    def columnCount(self, index):
        pass

class Worker(QtCore.QObject):
    start = QtCore.pyqtSignal(str)
    load_chapters = QtCore.pyqtSignal(list)

    @QtCore.pyqtSlot()
    def processing_chapters( self, url):
        #start = time.time()
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        self.load_chapters.emit(AbstractMangaSource.AbstractMangaSource.listchapters(url))
        end = time.time()
        #print(end - start)
        #print(len(results))


class MangaPageWorker(QtCore.QObject):
    start = QtCore.pyqtSignal(str)
    loadimage = QtCore.pyqtSignal(QtGui.QImage, str, int)

    @QtCore.pyqtSlot()
    def processing_image( self, images, page, url):
        #start = time.time()
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive', 'Referer': 'http://www.nettruyentop.com/'}
        image0 = None
        try:
         image0 = requests.get(images[page]['data-src'],headers=hdr, timeout = 15)
        except: 
         image0 = requests.get(images[page]['src'],headers=hdr, timeout = 15)        
        image = QtGui.QImage()
        image.loadFromData(image0.content)
        self.loadimage.emit(image, url, page) 
        #end = time.time()
        #print(end - start) 

class Ui_MainWindowImpl(mangareader.Ui_MainWindow):
    tmpselectedname= None
    selectedname= None
    image0 = None
    page = 0
    images = None
    tmpurl = ""
    chapter_index = 0
    prevchapter_url = ''
    nextchapter_url = ''
    lastsel1 = None
    lastsel2 = None
    searchresultslist = None
    tmp_index = 0
    thread = None
    thread2 = None
    shiftbt = False
    numbt = False
    worker2 = None
    bookmarks = []
    tmpmanga = ""
    selmanga = ""
    currentsource = "manganelo"
    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://www.nettruyentop.com/'}
    def setupUi(self, MainWindow):
        super(Ui_MainWindowImpl, self).setupUi(MainWindow)
        self.next.setStyleSheet("border : 0; background-color: transparent;")
        self.prev.setStyleSheet("border : 0; background-color: transparent;")
        self.dockbar.setVisible(False)
        self.ok.setVisible(True)
        self.pagedock.setVisible(False)
        self.brightness_window.setVisible(False)
        #self.next.setVisible(False)
        #self.prev.setVisible(False)
        ## annoying pycui error fix
        MainWindow.setCentralWidget(self.ok)
      
        
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
        self.dockbutton.clicked.connect(self.showdock)
        self.brightnessbt.clicked.connect(self.getBrightness)
        self.exitbrightness.clicked.connect(lambda: self.brightness_window.setVisible(False))
        self.brightnessslider.valueChanged.connect(self.handleSlider)
        self.brightnessslider.setMinimum(0)
        self.brightnessslider.setMaximum(24)
        self.brightnessslider.setTickInterval(1)
        self.brightnessslider.setSingleStep(1)
        self.pageslider.setMinimum(1)
        self.pageslider.setTickInterval(1)
        self.pageslider.setSingleStep(1)
        self.minusbrightness.clicked.connect(self.reducebrightness)
        self.plusbrightness.clicked.connect(self.increasebrightness)
        self.pageslider.valueChanged.connect(self.pagechangeslider)
        self.searchbt.clicked.connect(self.searchpage_fun)
        self.homebt.clicked.connect(self.homepage_fun)

        self.readerbt.clicked.connect(self.readerpage_fun)
        self.brightnessbt2.clicked.connect(self.getBrightness)
        self.exitbt2.clicked.connect(self.actionQuit_fun)
        self.homebt2.clicked.connect(self.homepage_fun)

        self.readerbt3.clicked.connect(self.readerpage_fun)
        self.searchbt3.clicked.connect(self.searchpage_fun)
        self.brightnessbt3.clicked.connect(self.getBrightness)
        self.exitbt3.clicked.connect(self.actionQuit_fun)

        self.readerbt3_2.clicked.connect(self.readerpage_fun)
        self.searchbt3_2.clicked.connect(self.searchpage_fun)
        self.brightnessbt3_2.clicked.connect(self.getBrightness)
        self.exitbt3_2.clicked.connect(self.actionQuit_fun)
        
        self.bookmarkbt.clicked.connect(self.addbookmark)
        self.bookmarkbt2.clicked.connect(self.addbookmark2)
        self.actionHome.triggered.connect(self.homepage_fun)
        self.homebt3.clicked.connect(self.homepage_fun)

        #self.tableWidget.setStyleSheet("""QTableWidget::item { font-size: 10pt }""")
        #self.tableWidget.mousePressEvent().connect(self.keyboardinput)

        #keyboard buttons ####### boilerplate
        
        self.key_q.clicked.connect( lambda:self.kbinput(str(self.key_q.text().toUtf8())))
        self.key_w.clicked.connect( lambda:self.kbinput(str(self.key_w.text().toUtf8())))
        self.key_e.clicked.connect( lambda:self.kbinput(str(self.key_e.text().toUtf8())))
        self.key_r.clicked.connect( lambda:self.kbinput(str(self.key_r.text().toUtf8())))
        self.key_t.clicked.connect( lambda:self.kbinput(str(self.key_t.text().toUtf8())))
        self.key_y.clicked.connect( lambda:self.kbinput(str(self.key_y.text().toUtf8())))
        self.key_u.clicked.connect( lambda:self.kbinput(str(self.key_u.text().toUtf8())))
        self.key_i.clicked.connect( lambda:self.kbinput(str(self.key_i.text().toUtf8())))
        self.key_o.clicked.connect( lambda:self.kbinput(str(self.key_o.text().toUtf8())))
        self.key_p.clicked.connect( lambda:self.kbinput(str(self.key_p.text().toUtf8())))
        self.key_l.clicked.connect( lambda:self.kbinput(str(self.key_l.text().toUtf8())))
        self.key_k.clicked.connect( lambda:self.kbinput(str(self.key_k.text().toUtf8())))
        self.key_j.clicked.connect( lambda:self.kbinput(str(self.key_j.text().toUtf8())))
        self.key_h.clicked.connect( lambda:self.kbinput(str(self.key_h.text().toUtf8())))
        self.key_g.clicked.connect( lambda:self.kbinput(str(self.key_g.text().toUtf8())))
        self.key_f.clicked.connect( lambda:self.kbinput(str(self.key_f.text().toUtf8())))
        self.key_d.clicked.connect( lambda:self.kbinput(str(self.key_d.text().toUtf8())))
        self.key_s.clicked.connect( lambda:self.kbinput(str(self.key_s.text().toUtf8())))
        self.key_a.clicked.connect( lambda:self.kbinput(str(self.key_a.text().toUtf8())))
        self.key_z.clicked.connect( lambda:self.kbinput(str(self.key_z.text().toUtf8())))
        self.key_x.clicked.connect( lambda:self.kbinput(str(self.key_x.text().toUtf8())))
        self.key_c.clicked.connect( lambda:self.kbinput(str(self.key_c.text().toUtf8())))
        self.key_v.clicked.connect( lambda:self.kbinput(str(self.key_v.text().toUtf8())))
        self.key_b.clicked.connect( lambda:self.kbinput(str(self.key_b.text().toUtf8())))
        self.key_n.clicked.connect( lambda:self.kbinput(str(self.key_n.text().toUtf8())))
        self.key_m.clicked.connect( lambda:self.kbinput(str(self.key_m.text().toUtf8())))
        self.key_bksp.clicked.connect( lambda:self.kbinput('bksp'))
        self.key_shift.clicked.connect( lambda:self.kbinput('shift'))
        self.key_space.clicked.connect( lambda:self.kbinput('space'))
        self.key_entr.clicked.connect( lambda:self.kbinput('enter'))
        self.key_dotperiod.clicked.connect(lambda:self.kbinput(str(self.key_dotperiod.text())))
        self.key_num.clicked.connect( lambda:self.kbinput('num'))

        self.comicselector.addItems(mangasources.sourcelist.manga_sites())
        self.comicselector.currentIndexChanged.connect(self.new_sources)
        try:
         with open('bookmarks.txt') as f:
           self.bookmarks = f.read().splitlines()
         model = TestListModel2(self.bookmarklist)
         model.inputData(self.bookmarks)
         self.bookmarklist.setModel(model)       
         if len(self.bookmarks) > 0:
            self.no_bookmark.setVisible(False)
         self.bookmarklist.clicked.connect(self.saveRes3)
        except: 
         pass      
        
        if self.url == "":
           self.readerbt.setVisible(False)
           self.readerbt3.setVisible(False)
           self.readerbt3_2.setVisible(False)        

    def new_sources(self):
        print(str(self.comicselector.currentText()))
        self.currentsource = str(self.comicselector.currentText())
        self.querysearch()

    def showdock(self):
        page = self.url[:self.url.rfind("/")]
        name = self.selectedname
        combined = name +"y:_$W|~_:q"+page
        if combined in self.bookmarks:
         icon5 = QtGui.QIcon()
         icon5.addPixmap(QtGui.QPixmap(_fromUtf8("bookmarkoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.bookmarkbt.setIcon(icon5)
        else: 
         icon5 = QtGui.QIcon()
         icon5.addPixmap(QtGui.QPixmap(_fromUtf8("bookmarkon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.bookmarkbt.setIcon(icon5)
        self.dockbar.setVisible(True)
        self.pagedock.setVisible(True)
        self.pagecount.setText(str(int(self.page+1))+"/"+str(len(self.images)))
        self.pageslider.setValue(int(self.page+1))
        print(self.page)
        self.pageslider.setMaximum(int(len(self.images)))

    def showbrightness(self):
        self.brightness_window.setVisible(True)
        self.ok2.setVisible(True)    
        

    def nextpage(self):
        if self.dockbar.isVisible() :
            self.dockbar.setVisible(False)
            self.pagedock.setVisible(False)
            print('ok')
        else:    
         if self.page < len(self.images) -1:
          self.page += 1
        #   self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr, timeout = 15)    
        #   image = QtGui.QImage()
        #   image.loadFromData(self.image0.content)
        #   self.image.setPixmap(QtGui.QPixmap(image))
          try:
        #    self.thread2.terminate()
        #    self.thread2.deleteLater()
        #    self.worker2.deleteLater()
        #    self.thread2 = None
        #    self.worker2 = None     
            pass      
          except Exception as e:
           print(e)   
            
          self.worker2 = MangaPageWorker()
          self.thread2 = QtCore.QThread()
          self.worker2.loadimage.connect(self.display_image)
          self.worker2.moveToThread(self.thread2) 
          self.thread2.started.connect(lambda: self.worker2.processing_image(self.images,self.page,self.url))     
          self.thread2.start()

         else:
          self.next_chapter()
    


    def prevpage(self):
        if self.dockbar.isVisible() :
            self.dockbar.setVisible(False)
            self.pagedock.setVisible(False)            
        else:   
         if self.page > 0 :
          self.page += -1
        #   self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr, timeout = 15)    
        #   image = QtGui.QImage()
        #   image.loadFromData(self.image0.content)
        #   self.image.setPixmap(QtGui.QPixmap(image))
        #   try:
        #    self.thread2.terminate()
        #    self.thread2.deleteLater()
        #    self.worker2.deleteLater()
        #    self.thread2 = None
        #    self.worker2 = None  
        #   except Exception as e:
        #    print(e)   
            
          self.worker2 = MangaPageWorker()
          self.thread2 = QtCore.QThread()
          self.worker2.moveToThread(self.thread2) 
          self.thread2.started.connect(lambda: self.worker2.processing_image(self.images,self.page,self.url))  
          self.worker2.loadimage.connect(self.display_image)
          self.thread2.start()
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
            print(self.prevchapter_url)        
            self.launchreader(self.prevchapter_url)
          else:
            QtGui.QMessageBox.about(QtGui.QMainWindow(), "L:A_N:application_ID:Last Chapter",
            "<H1>First chapter!</H1>".decode("utf8"))  

    def kbinput(self, char):

        # text = self.mangaSearch.text()
         
         if char.decode('utf-8') == u"\uFE60":
            char = '&'
         if len(char.decode('utf-8')) == 1:  
            if self.shiftbt == True: 
                char = char.upper()
            key = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,QtGui.QKeySequence.fromString(str(char).decode('utf-8'))[0],QtCore.Qt.NoModifier,QtCore.QString(str(char).decode('utf-8')))
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
             self.key_q.setText('q')
             self.key_w.setText('w')
             self.key_e.setText('e')
             self.key_r.setText('r')
             self.key_t.setText('t')
             self.key_y.setText('y')
             self.key_u.setText('u')
             self.key_i.setText('i')
             self.key_o.setText('o')
             self.key_p.setText('p')
             self.key_l.setText('l')
             self.key_k.setText('k')
             self.key_j.setText('j')
             self.key_h.setText('h')
             self.key_g.setText('g')
             self.key_f.setText('f')
             self.key_d.setText('d')
             self.key_s.setText('s')
             self.key_a.setText('a')
             self.key_z.setText('z')
             self.key_x.setText('x')
             self.key_c.setText('c')
             self.key_v.setText('v')
             self.key_b.setText('b')
             self.key_n.setText('n')
             self.key_m.setText('m')
            else: 
             self.shiftbt = True
             if self.numbt == False:
              self.key_shift.setStyleSheet("""QPushButton{background-color: black;color: white;}""")  
              self.key_q.setText('Q')
              self.key_w.setText('W')
              self.key_e.setText('E')
              self.key_r.setText('R')
              self.key_t.setText('T')
              self.key_y.setText('Y')
              self.key_u.setText('U')
              self.key_i.setText('I')
              self.key_o.setText('O')
              self.key_p.setText('P')
              self.key_l.setText('L')
              self.key_k.setText('K')
              self.key_j.setText('J')
              self.key_h.setText('H')
              self.key_g.setText('G')
              self.key_f.setText('F')
              self.key_d.setText('D')
              self.key_s.setText('S')
              self.key_a.setText('A')
              self.key_z.setText('Z')
              self.key_x.setText('X')
              self.key_c.setText('C')
              self.key_v.setText('V')
              self.key_b.setText('B')
              self.key_n.setText('N')
              self.key_m.setText('M')
             else:
              self.key_q.setText('#')
              self.key_w.setText('%')
              self.key_e.setText('~')
              self.key_r.setText('^')
              self.key_t.setText('[')
              self.key_y.setText(']')
              self.key_u.setText('{')
              self.key_i.setText('}')
              self.key_o.setText('|')
              self.key_p.setText("\\")
              self.key_l.setText(u'\u00B7')
              self.key_k.setText(u'\u2122')
              self.key_j.setText(u'\u00AC')
              self.key_h.setText('`')
              self.key_g.setText('<')
              self.key_f.setText('>')
              self.key_d.setText('_')
              self.key_s.setText('*')
              self.key_a.setText('=')
              self.key_z.setText(u'\u00A9')
              self.key_x.setText(u'\u00AE')
              self.key_c.setText(u'\u00A7')
              self.key_v.setText(u'\u00A2')
              self.key_b.setText(u'\u00A2')
              self.key_n.setText(u'\u20AC')
              self.key_m.setText(u'\u00A3')    
         elif char == "enter":
             self.querysearch() 
         elif char == "num":    
            if self.numbt == True:
             self.shiftbt = False    
             self.numbt = False
             self.key_shift.setStyleSheet("""""")
             self.key_num.setStyleSheet("""""")
             self.key_q.setText('q')
             self.key_w.setText('w')
             self.key_e.setText('e')
             self.key_r.setText('r')
             self.key_t.setText('t')
             self.key_y.setText('y')
             self.key_u.setText('u')
             self.key_i.setText('i')
             self.key_o.setText('o')
             self.key_p.setText('p')
             self.key_l.setText('l')
             self.key_k.setText('k')
             self.key_j.setText('j')
             self.key_h.setText('h')
             self.key_g.setText('g')
             self.key_f.setText('f')
             self.key_d.setText('d')
             self.key_s.setText('s')
             self.key_a.setText('a')
             self.key_z.setText('z')
             self.key_x.setText('x')
             self.key_c.setText('c')
             self.key_v.setText('v')
             self.key_b.setText('b')
             self.key_n.setText('n')
             self.key_m.setText('m')
            else: 
             self.shiftbt = False 
             self.numbt = True
             self.key_shift.setStyleSheet("""""") 
             self.key_num.setStyleSheet("""QPushButton{background-color: black;color: white;}""")  
             self.key_q.setText('1')
             self.key_w.setText('2')
             self.key_e.setText('3')
             self.key_r.setText('4')
             self.key_t.setText('5')
             self.key_y.setText('6')
             self.key_u.setText('7')
             self.key_i.setText('8')
             self.key_o.setText('9')
             self.key_p.setText('0')
             self.key_l.setText('$')
             self.key_k.setText(u"\uFE60")
             self.key_j.setText('(')
             self.key_h.setText(')')
             self.key_g.setText('"')
             self.key_f.setText("'")
             self.key_d.setText('-')
             self.key_s.setText('+')
             self.key_a.setText('/')
             self.key_z.setText('@')
             self.key_x.setText('!')
             self.key_c.setText('?')
             self.key_v.setText(':')
             self.key_b.setText(';')
             self.key_n.setText(',')
             self.key_m.setText(u'\u2026')
    def increasebrightness(self):
        val = int(self.brightnessslider.value())
        if val < 24:
            self.brightnessslider.setValue(val + 1)

    def reducebrightness(self):
        val = int(self.brightnessslider.value())
        if val > 0:
            self.brightnessslider.setValue(val - 1)

    def getBrightness(self):
        if self.brightness_window.isVisible() == False:
         import subprocess
         brightness_level = subprocess.check_output('lipc-get-prop com.lab126.powerd flIntensity', shell=True)
         self.brightnessslider.setValue(int(brightness_level))
         self.brightness_window.setVisible(True) 
        else:  self.brightness_window.setVisible(False) 
      

    def handleSlider(self, val):
        self.setFlIntensity(val)   

    def pagechangeslider(self,val):
        if val != self.page + 1:
         self.page = int(val + 1)
         self.pagecount.setText(str(int(val))+"/"+str(len(self.images)))
        #  self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr, timeout = 15)    
        #  image = QtGui.QImage()
        #  image.loadFromData(self.image0.content)
        #  self.image.setPixmap(QtGui.QPixmap(image))
        #  try:
        #    self.thread2.terminate()
        #    self.thread2.deleteLater()
        #    self.worker2.deleteLater()
        #    self.thread2 = None
        #    self.worker2 = None
        #  except Exception as e:
        #    print(e)   
            
         self.worker2 = MangaPageWorker()
         self.thread2 = QtCore.QThread()
         self.worker2.moveToThread(self.thread2) 
         self.thread2.started.connect(lambda: self.worker2.processing_image(self.images,self.page,self.url))     
         self.worker2.loadimage.connect(self.display_image)
         self.thread2.start()         

    def setFlIntensity(self , level):
        import os
        os.system("lipc-set-prop com.lab126.powerd flIntensity "+ str(int(level)))
        
    def querysearch(self):
      self.searchlist.clear()
      text = self.mangaSearch.text()
      if len(text)> 1:  
        

        # linkurl = str('https://manganelo.tv/search/'+str(text))
        # req = requests.get(linkurl, headers=self.hdr, timeout = 15)
        # ## data = json.load(response)   
        # # print response.fp.read()
        # soup = BeautifulSoup(req.text, 'html.parser')
        print self.currentsource
        results = AbstractMangaSource.AbstractMangaSource.getSearchResult(self.currentsource,text)  
        if len(results) != 0:
            for result in results:
                url = result.getUrl()
                title = result.getTitle()
                author = result.getAuthor()
                icon = result.getIcon()
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
            self.searchlist.scrollToTop()

    def mangainfo(self, item):
       data = item.data(1).toPyObject()        
       if data != self.lastsel2:
        print(data)
        self.tmpurl = data[0]
        url =  data[0]
        title = data[1]
        author = data[2]
        icon = data[3]
        self.stackedwidget.setCurrentIndex(2)
        self.infotext.setText(title)
        infoimage0 = requests.get(icon,headers=self.hdr, timeout = 15)    
        image = QtGui.QImage()
        image.loadFromData(infoimage0.content)
        self.infoimage.setPixmap(QtGui.QPixmap(image)) 
        combined = title +"y:_$W|~_:q"+self.tmpurl
        if combined in self.bookmarks:
         self.bookmarkbt2.setText("Remove bookmarks")
        else: 
         self.bookmarkbt2.setText("Add to bookmarks")
        try:
         self.thread.terminate()
         self.infochapters.setModel(None)
         self.infochapters.scrollToTop()
        except Exception as e:
         print(e)   
        self.tmpselectedname = title   
        self.worker = Worker()
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread) 
        self.thread.started.connect(lambda: self.worker.processing_chapters(url))     
        self.worker.load_chapters.connect(self.load_list)
        self.thread.start()

    def mangainfo2(self, rawurl, title):  
       if (rawurl) != self.lastsel2:
        self.lastsel2 = (rawurl)
        self.bookmarkbt2.setText("Remove bookmarks")   
        url = rawurl
        print(url)
        icon = AbstractMangaSource.AbstractMangaSource.getIconFromUrl(url)
     
        self.stackedwidget.setCurrentIndex(2)
        self.infotext.setText(title)
        if icon != "":
         infoimage0 = requests.get(icon,headers=self.hdr, timeout = 10)    
         image = QtGui.QImage()
         image.loadFromData(infoimage0.content)
         self.infoimage.setPixmap(QtGui.QPixmap(image)) 
        print("ok")
        try:
         self.thread.terminate()
         self.infochapters.setModel(None)
         self.infochapters.scrollToTop()
        except Exception as e:
         print()   
        self.tmpselectedname = title   
        self.worker = Worker()
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread) 
        self.thread.started.connect(lambda: self.worker.processing_chapters(url))     
        self.worker.load_chapters.connect(self.load_list)
        self.thread.start()  

    @QtCore.pyqtSlot(list)
    def load_list(self, results):
        print('ok')
        if len(results) != 0:
            self.tmp_index = -1
            model = TestListModel(self.infochapters)
            model.inputData(results)
            self.infochapters.setModel(model)   
            self.infochapters.clicked.connect(self.saveRes2)

    @QtCore.pyqtSlot(QtGui.QImage, str, int)
    def display_image(self, image, url, page):
        start = time.time()
        if (self.url == url):
            self.image.setPixmap(QtGui.QPixmap(image))  
        end = time.time()
        print("il:" + str(end-start))       


    def saveRes2(self, index): 
        self.launchreader(self.infochapters.model().results[index.row()].getUrl())

    def saveRes3(self,index):
        title = self.bookmarklist.model().results[index.row()][:str(self.bookmarklist.model().results[index.row()]).rfind("y:_$W|~_:q")]
        url = self.bookmarklist.model().results[index.row()][len(title+"y:_$W|~_:q"):]
        print("oof"+url)
        self.mangainfo2(url,title)

    def saveRes(self, item): 
        print('bruh')
        data = item.data(2).toPyObject() 
        if data != self.lastsel2:
          self.lastsel2 = data
          print(self.lastsel2)
          data = item.data(2).toPyObject()     
          self.chapter_index = data[1]
          self.launchreader(data[1])

    def launchreader(self,url):
        self.url = url
        # req = requests.get(str('https://manganelo.tv')+ self.url, headers=self.hdr,  timeout = 15)        
        # ## data = json.load(response)   
        # # print response.fp.read()
        # #def xstr(s):
        # #    if s is None:
        # #       return ''
        # #    return str(s)
        # soup = BeautifulSoup(req.text, 'html.parser')
        # self.images = soup.find_all('img', attrs={'class':"img-loading"})
        # prev_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-prev a-h"})
        # next_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-next a-h"})
        result = AbstractMangaSource.AbstractMangaSource.listchapterimages(url)
        self.selmanga = self.tmpurl
        self.images = result[0]
        prev_element = result[1]
        next_element = result[2]
        prev_lk = ''
        next_lk = ''
        if prev_element is not None : prev_lk = prev_element['href']
        if next_element is not None : next_lk = next_element['href']        
        self.prevchapter_url = str(prev_lk)
        self.nextchapter_url = str(next_lk)
        self.selectedname = self.tmpselectedname
        print(self.prevchapter_url)
        print(self.nextchapter_url)
        # load first image #################
        self.page = 0
        try:
         self.image0 = requests.get(self.images[0]['data-src'],headers=self.hdr, timeout = 15, stream=True)
        except: 
         self.image0 = requests.get(self.images[0]['src'],headers=self.hdr, timeout = 15, stream=True)    
        image = QtGui.QImage()
        image.loadFromData(self.image0.content)
        self.image0.close()
        self.image.setPixmap(QtGui.QPixmap(image))
        self.stackedwidget.setCurrentIndex(0)  


    def addbookmark(self):
        page = self.selmanga
        name = self.selectedname
        combined = name +"y:_$W|~_:q"+page
        if combined in self.bookmarks:
         icon5 = QtGui.QIcon()
         icon5.addPixmap(QtGui.QPixmap(_fromUtf8("bookmarkoff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.bookmarkbt.setIcon(icon5)
         self.bookmarks.remove(combined)
        else: 
         icon5 = QtGui.QIcon()
         icon5.addPixmap(QtGui.QPixmap(_fromUtf8("bookmarkon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.bookmarkbt.setIcon(icon5)
         self.bookmarks.append(combined)

    def addbookmark2(self):
        page = self.tmpurl
        name = self.infotext.text()
        print(page)
        combined = name +"y:_$W|~_:q"+page
        if combined in self.bookmarks:
         self.bookmarkbt2.setText("Add to bookmarks")
         self.bookmarks.remove(combined)
        else: 
         self.bookmarkbt2.setText("Remove bookmarks")
         self.bookmarks.append(combined)

    def actionQuit_fun(self):
       with open('bookmarks.txt', 'w') as textfile:
        for element in self.bookmarks:
         textfile.write(element + "\n")
        textfile.close()
       quit()   

    def searchpage_fun(self):
        self.dockbar.setVisible(False)
        self.pagedock.setVisible(False)
        self.stackedwidget.setCurrentIndex(1)
        if self.url == "":
           self.readerbt.setVisible(False)
           self.readerbt3.setVisible(False)
           self.readerbt3_2.setVisible(False)
        else:
           self.readerbt.setVisible(True)
           self.readerbt3.setVisible(True)
           self.readerbt3_2.setVisible(True)        
        
    def readerpage_fun(self):
        self.dockbar.setVisible(False)
        self.pagedock.setVisible(False)
        self.stackedwidget.setCurrentIndex(0)
        if self.url == "":
           self.readerbt.setVisible(False)
           self.readerbt3.setVisible(False)
           self.readerbt3_2.setVisible(False)
        else:
           self.readerbt.setVisible(True)
           self.readerbt3.setVisible(True)
           self.readerbt3_2.setVisible(True)                     

    def chapterpage_fun(self):
        self.dockbar.setVisible(False)
        self.pagedock.setVisible(False)
        self.stackedwidget.setCurrentIndex(2)
        if self.url == "":
           self.readerbt.setVisible(False)
           self.readerbt3.setVisible(False)
           self.readerbt3_2.setVisible(False)
        else:
           self.readerbt.setVisible(True)
           self.readerbt3.setVisible(True)
           self.readerbt3_2.setVisible(True)                

    def homepage_fun(self):
        self.dockbar.setVisible(False)
        self.pagedock.setVisible(False)
        self.bookmarklist.setModel(None)
        model = TestListModel2(self.bookmarklist)
        model.inputData(self.bookmarks)
        self.bookmarklist.setModel(model)       
        self.bookmarklist.clicked.connect(self.saveRes3)
        if len(self.bookmarks) > 0:
            self.no_bookmark.setVisible(False)
        self.stackedwidget.setCurrentIndex(3)        

       
 

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


