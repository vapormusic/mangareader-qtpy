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
        linkurl = str('https://manganelo.tv/search/'+str(text))
        req = requests.get(linkurl, headers=hdr, timeout = 15)
        ## data = json.load(response)   
        # print response.fp.read()
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.find_all('div', attrs={'class':"search-story-item"}) 
        data = []
        for result in results:     
          url = str('https://manganelo.tv')+ result.find('a', attrs={'class':"item-img"})['href']
          title = result.find('a', attrs={'class':"item-img"})['title'] 
          author = result.find('span', attrs={'class':"text-nowrap item-author"})['title']
          icon = str('https://manganelo.tv')+ result.find('img', attrs={'class':"img-loading"})['src']
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
        preresult = soup.find('ul', attrs={'class':"row-content-chapter"})
        results = preresult.find_all('li', attrs={'class':"a-h"})
        data = []
        for result in results:     
          url = str('https://manganelo.tv')+ result.find('a', attrs={'class':"chapter-name text-nowrap"})['href']
          title = result.find('a', attrs={'class':"chapter-name text-nowrap"}).text
          author = result.find('span', attrs={'class':"chapter-time text-nowrap"}).text
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
        images = soup.find_all('img', attrs={'class':"img-loading"})
        prev_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-prev a-h"})
        next_element = soup.find('a', attrs={'class':"navi-change-chapter-btn-next a-h"})
        return [images, prev_element, next_element]

def getmangaiconfromurl(url):
        return url.replace("/manga/","/mangaimage/")+".jpg"        
         
def getImageHeader(): 
        return  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}