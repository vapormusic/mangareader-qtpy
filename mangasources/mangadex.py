import requests, requests_cache
from searchclass import searchclass
from bs4 import BeautifulSoup , element
import json 
import traceback
import sys

def getSearchResult(text):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        urlstring = 'https://api.mangadex.org/manga?title='+str(text)

        selectedLanguage = ["en"]

        for i in range(len(selectedLanguage)):
              urlstring += '&availableTranslatedLanguage['+ str(i) + ']=' + selectedLanguage[i]

        urlstring += '&includes[]=artist&includes[]=author&includes[]=cover_art&contentRating[]=safe&contentRating[]=suggestive&contentRating[]=erotica&contentRating[]=pornographic'
        linkurl = str(urlstring)

        req = requests.get(linkurl, headers=hdr, timeout = 15)
        data = json.loads(req.text)
        if data['result'] == 'error':
          return []

        results = data['data']
        data = []
        for result in results:     
          url = 'https://api.mangadex.org/manga/' + result['id']
          title = result['attributes']['title']['en']
          relationships = result['relationships']
          author = ""
          icon = ""
          try:
            author_data = next(relationships for relationships in relationships if relationships['type'] == 'author')
            author = author_data['attributes']["name"]
          except: pass  
          try:
            art_data = next(relationships for relationships in relationships if relationships['type'] == 'cover_art')
            icon = 'https://mangadex.org/covers/' + result['id'] +'/' + art_data['attributes']["fileName"] + ".128.jpg"
          except: pass  
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

        filteredlanguage = 'en'

        chapterlist_url = url + "/feed?limit=500&translatedLanguage[]="+ filteredlanguage +"&includes[]=scanlation_group&includes[]=user&order[volume]=desc&order[chapter]=desc&offset=0&contentRating[]=safe&contentRating[]=suggestive&contentRating[]=erotica&contentRating[]=pornographic"
        
        req = requests.get(chapterlist_url, headers=hdr, timeout = 15)
        data = json.loads(req.text)

        if data['result'] == 'error':
          return []

        results = data['data']
        data = []
        for result in results:     
          url = 'https://api.mangadex.org/at-home/server/' +  result['id']
          title = result['attributes']['title']
          author = result['attributes']['createdAt'] 
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
        data = json.loads(req.text)

        if data['result'] == 'error':
          return [[], None, None]
        
        results = data['chapter']['dataSaver']
        baseurl = data['baseUrl']
        hash = data['chapter']['hash']
        data = []
        images = []
        for result in results: 
            image_url = baseurl + '/data-saver/' + hash + '/' + result
            images.append(image_url)
        prev_element = None
        next_element = None
        try:
            url1 = url.replace('https://api.mangadex.org/at-home/server/','https://api.mangadex.org/chapter/') + "?includes[]=manga"
            req1 = requests.get(url1, headers=hdr,  timeout = 10)     
            data = json.loads(req1.text)
            if data['result'] == 'ok':
                results = data['data']['relationships']
                manga_num = data['data']['attributes']['chapter']
                manga_id = next(relationships for relationships in results if relationships['type'] == 'manga')['id']
                url2 = "https://api.mangadex.org/manga/"+ manga_id + "/aggregate?translatedLanguage[]=en"
                req2 = requests.get(url2, headers=hdr,  timeout = 10)     
                data = json.loads(req2.text)
                chapter_list = []
                if data['result'] == 'ok':
                    volumes = data['volumes']
                    for volume_key in volumes.keys():
                        for chapter_key in volumes[volume_key]['chapters'].keys():
                            chapter_list.append({'key': float(chapter_key), 'id': volumes[volume_key]['chapters'][chapter_key]['id']})
                chapter_list = sorted(chapter_list, key=lambda d: d['key']) 
                ##print(chapter_list)
                 ## find prev and next chapter
                for i in range(len(chapter_list)):
                    if chapter_list[i]['key'] == float(manga_num):
                        if i > 0:
                            prev_element = {'href': 'https://api.mangadex.org/at-home/server/' + chapter_list[i-1]['id']}
                        if i < len(chapter_list) - 1:
                            next_element =  {'href': 'https://api.mangadex.org/at-home/server/' + chapter_list[i+1]['id']}
                        break

                
        except Exception as e: traceback.print_exception(*sys.exc_info())
        print(prev_element, next_element)
        return [images, prev_element, next_element]

def getmangaiconfromurl(url):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = requests.get(url+'?includes[]=cover_art', headers=hdr, timeout = 15)
        data = json.loads(req.text)
        if data['result'] == 'error':
          return ""
        result = data['data']
        relationships = result['relationships']
        art_data = next(relationships for relationships in relationships if relationships['type'] == 'cover_art') 
        return 'https://mangadex.org/covers/' + result['id'] +'/' + art_data['attributes']["fileName"] + ".128.jpg"
         
def getImageHeader(): 
        return  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}