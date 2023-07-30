import requests, requests_cache
from searchclass import searchclass
from bs4 import BeautifulSoup , element
def getSearchResult(text):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        linkurl = str('http://www.nettruyenmax.com/tim-truyen?keyword='+str(text))
        req = requests.get(linkurl, headers=hdr, timeout = 15)
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(req.text, 'html.parser')
        preres = soup.find('div', attrs={'class':"Module Module-170"})
        results = preres.find_all('div', attrs={'class':"item"}) 
        data = []
        print len(results)
        for result in results:     
          url = result.find('a')['href']
          title = result.find('a')['title'][13:]
          author1 = result.find('div', attrs={'class':"message_main"}).find_all('p')[2].getText()
          print author1.find(':')
          if author1.find(':') == 8:
             author = author1[9:]
          else : author = result.find('div', attrs={'class':"message_main"}).find_all('p')[1].getText()[9:]   
          icon = str("https:") + result.find('img',attrs={'class':"lazy"})['src']
          newres = searchclass()
          newres.setUrl(url)
          newres.setTitle(title)
          newres.setAuthor(author)
          newres.setIcon(icon)
          data.append(newres)

        print data 
        return data 


def processing_chapters(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = requests.get(url, headers=hdr, timeout = 15)
        soup = BeautifulSoup(req.text, 'html.parser')
        preresult = soup.find('div', attrs={'id':"nt_listchapter"})
        results = preresult.find_all('div', attrs={'class':"col-xs-5 chapter"})
        data = []
        for result in results:     
          url = result.find('a')['href']
          title = result.find('a').text
          author = ""
          try:
           author = result.find('div', attrs={'class':"col-xs-4 text-center small"}).text
          except: pass
          icon = ""
          newres = searchclass()
          newres.setUrl(url)
          newres.setTitle(title)
          newres.setAuthor(author)
          newres.setIcon(icon)
          data.append(newres) 
        return data     

def image_lists(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = requests.get(url, headers=hdr,  timeout = 15)        
        soup = BeautifulSoup(req.text, 'html.parser')
        box = soup.find('div', attrs={'class':"reading-detail box_doc"})
        images = box.find_all('img')
        prev_element = soup.find('a', attrs={'class':"prev a_prev"})
        next_element = soup.find('a', attrs={'class':"next a_next"})
        for image in images:
            image['src'] = "http:"+image['src']
        return [images, prev_element, next_element]

def getmangaiconfromurl(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = requests.get(url, headers=hdr,  timeout = 15)        
        soup = BeautifulSoup(req.text, 'html.parser')
        box = soup.find('div', attrs={'class':"col-xs-4 col-image"})
        return 'http:'+ box.find('img')['src']
         
def getCustomHeader():
        return  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://www.nettruyenmax.com/'       
        }

def getImageHeader(): 
        return {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://www.nettruyenmax.com/'       
        }

        