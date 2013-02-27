class API:
    
    BASE_URL = 'http://127.0.0.1:8274/'
    
    def getJsonDict(self, path):
        import urllib
        rawJson = urllib.urlopen(API.BASE_URL + path).read()
        
        import gluon.contrib.simplejson as json
        jsonDict = json.loads(rawJson)
        
        return jsonDict

api = API()
