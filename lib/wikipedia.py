import urllib
import urllib2
from BeautifulSoup import BeautifulSoup



class Article:
    article = ''
    data = ''
    summary = ''
        
    def call(self):
        self.article = urllib.quote(self.article)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        resource = opener.open("http://en.wikipedia.org/wiki/" + self.article)
        self.data = resource.read()
        resource.close()
    
    def get_summary(self):
        self.call()
        soup = BeautifulSoup(self.data)
        self.summary = soup.find('div', id="bodyContent").p
        
    def initialize(self):
        self.get_summary()