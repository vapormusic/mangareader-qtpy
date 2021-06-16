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
        linkurl = str('http://mangahere.today/search?q='+str(text))
        req = requests.get(linkurl, headers=hdr, timeout = 15)
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.find_all('div', attrs={'class':"col-md-6"}) 
        data = []
        for result in results:     
          url = result.find('a', attrs={'class':"tooltips"})['href']
          title = result.find('a', attrs={'class':"tooltips"})['title'] 
          try:
           author1 = result.find('p', attrs={'class':"description descripfix"}).text       
           author = author1[author1.rfind("Author: ")+8:]
           print author
          except: pass
          icon = result.find('img', attrs={'class':"media-object"})['src']
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
        preresult = soup.find('section', attrs={'id':"examples"})
        results = preresult.find_all('li', attrs={'class':"row"})
        data = []
        for result in results:     
          url = result.find('a')['href']
          additionaltitle = result.find('span').text
          title = result.find('a').text 
          author = ("" if additionaltitle is None else additionaltitle[3:])
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
        preimages = soup.find('p', attrs={'id':"arraydata"}).text
        print preimages
        images = preimages.split(",")
        prev_element = soup.find('a', attrs={'class':"LeftArrow prev"})
        next_element = soup.find('a', attrs={'class':"RightArrow"})
        return [images, prev_element, next_element]

def getmangaiconfromurl(url):
        return ""       
         
def getImageHeader(): 
        return {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive', 'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'}
