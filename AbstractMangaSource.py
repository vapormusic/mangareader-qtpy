import mangasources 
class AbstractMangaSource:
  
    @staticmethod
    def getSearchResult(current_source, text):
         return getattr(mangasources, str(current_source)).getSearchResult(text)
        
    @staticmethod
    def listchapters(url):
        for site in mangasources.sourcelist.manga_sites():   
         if site in url: 
          return getattr(mangasources, site).processing_chapters(url)

    @staticmethod
    def listchapterimages(url):
        for site in mangasources.sourcelist.manga_sites():   
         if site in url: 
          return getattr(mangasources, site).image_lists(url)

    @staticmethod
    def getIconFromUrl(url):
        for site in mangasources.sourcelist.manga_sites():   
         if site in url: 
          return getattr(mangasources, site).getmangaiconfromurl(url)

    @staticmethod
    def getHeader(url):
        for site in mangasources.sourcelist.manga_sites():   
         if site in url: 
          return getattr(mangasources, site).getCustomHeader()            