import mangareader
import requests
from bs4 import BeautifulSoup
from PyQt4 import QtCore, QtGui
import json
from searchcard import SearchCardView
from PIL import Image


class Ui_MainWindowImpl(mangareader.Ui_MainWindow):
 
    image0 = None
    page = 0
    images = None
    searchresultslist = None
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
        #self.next.setVisible(False)
        #self.prev.setVisible(False)
        ## annoying pycui error fix
        MainWindow.setCentralWidget(self.stackedwidget)

        
        # get list of images from 1 chapter ###########

        req = requests.get(self.url, headers=self.hdr)        
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(req.text, 'html.parser')
        self.images = soup.find_all('img', attrs={'class':"img-loading"})
        print self.images[0]['data-src']


        # load first image #################

        self.image0 = requests.get(self.images[0]['data-src'],headers=self.hdr, stream=True)
        image = QtGui.QImage()
        image.loadFromData(self.image0.content)
        
        self.image.setPixmap(QtGui.QPixmap(image))

        #buttons ###########
        self.next.clicked.connect(self.nextpage)
        self.prev.clicked.connect(self.prevpage)
        self.actionExit.triggered.connect(self.actionQuit_fun)
        self.actionComics.triggered.connect(self.searchpage_fun)
        self.actionReader.triggered.connect(self.readerpage_fun)
        self.searchButton.clicked.connect(self.querysearch)

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

    def nextpage(self):
        if self.page < len(self.images) -1:
          self.page += 1
        self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr)    
        image = QtGui.QImage()
        image.loadFromData(self.image0.content)
        self.image.setPixmap(QtGui.QPixmap(image))
    


    def prevpage(self):
        if self.page > 0 :
          self.page += -1
        self.image0 = requests.get(self.images[self.page]['data-src'],headers=self.hdr)    
        image = QtGui.QImage()
        image.loadFromData(self.image0.content)
        self.image.setPixmap(QtGui.QPixmap(image))  

    def kbinput(self, char):
        text = self.mangaSearch.text()
        if len(char) == 1:   
            text = str(text) + str(char).lower() 
            self.mangaSearch.setText(text)
        elif char == 'space':
            text = str(text) + str(" ") 
            self.mangaSearch.setText(text)
        elif char == "bksp":
            text = str(text)[:-1]
            self.mangaSearch.setText(text)    

    def querysearch(self):
        self.searchlist.clear()
        text = self.mangaSearch.text()
        linkurl = str('https://manganelo.tv/search/'+str(text))
        req = requests.get(linkurl, headers=self.hdr)
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
        print(data)
        url = data[0]
        title = data[1]
        author = data[2]
        icon = data[3]

    def actionQuit_fun(self):
        quit()   

    def searchpage_fun(self):
        self.stackedwidget.setCurrentIndex(1)
        
    def readerpage_fun(self):
        self.stackedwidget.setCurrentIndex(0)             

 

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
