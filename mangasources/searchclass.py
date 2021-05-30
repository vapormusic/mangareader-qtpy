class searchclass:
    def __init__ (self):
        self.url = ""
        self.title = ""
        self.author = ""
        self.icon = "" 

    def setUrl(self,url):
        self.url = url

    def setTitle(self,title):
        self.title = title 

    def setAuthor(self,author):
        self.author = author

    def setIcon(self,icon):
        self.icon = icon

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getIcon(self):
        return self.icon                
