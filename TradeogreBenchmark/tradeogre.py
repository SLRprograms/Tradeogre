import time
import requests
#API commands
class Commands(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.api_url = 'https://tradeogre.com/api/v1'
                
    #returns raw data of an individual product. 
    def ticker(self, product):
        attempts = 0
        while True:
            try:
                r = requests.get(self.api_url + '/ticker/BTC-'+str(product))
                data = r.json()
                return data
            except:
                attempts += 1
                print 'FAILED ticker ' + str(attempts)
                time.sleep(60)
