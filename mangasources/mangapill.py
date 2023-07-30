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
        urlstring = 'https://www.mangapill.com/quick-search?q='+str(text)

        linkurl = str(urlstring)

        req = requests.get(linkurl, headers=hdr, timeout = 15)
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.select("div > a")
        data = []
        for result in results:     
          url = str('https://www.mangapill.com') + result['href']
          title = result.find('div', attrs={'class':"font-black"}).text
          author = ""
          id = url.split('/')[4]
          icon = 'https://cdn.readdetectiveconan.com/file/mangapill/i/' + id +'.jpeg'
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

        chapterlist_url = url
        
        req = requests.get(chapterlist_url, headers=hdr, timeout = 15)
        soup = BeautifulSoup(req.text, 'html.parser')
        results = soup.select("div#chapters > div > a")
        data = []

        for result in results:     
          url = str('https://www.mangapill.com') +  result['href']
          title = result.text
          author = ""
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
        results = soup.select("img.js-page")

        images = []
        for result in results: 
            image_url = result['data-src']
            images.append(image_url)
        prev_element = soup.find('a', attrs={'data-hotkey':"ArrowLeft"})
        next_element = soup.find('a', attrs={'data-hotkey':"ArrowRight"})
        if prev_element is not None:
            prev_element = {'href': 'https://www.mangapill.com' +  prev_element['href'] } 
        if next_element is not None:
            next_element = {'href': 'https://www.mangapill.com' +  next_element['href'] } 
          
        print(prev_element, next_element)
        return [images, prev_element, next_element]

def getmangaiconfromurl(url):
        # extract ID from url
        id = url.split('/')[4]
        return 'https://cdn.readdetectiveconan.com/file/mangapill/i/' + id +'.jpeg'
         
def getImageHeader(): 
        return  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mangapill.com'}