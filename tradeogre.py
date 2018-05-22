import time
import requests
#API commands
class Commands(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.api_url = 'https://tradeogre.com/api/v1'

    #returns raw market data
    def markets(self):
        attempts = 0
        while True:
            try:
                r = requests.get(self.api_url + '/markets')
                return r.json()
            except:
                attempts += 1
                print 'FAILED markets ' + str(attempts)
                time.sleep(60)

    #returns list of product names with raw markets data
    def productNames(self, markets):
        names = []
        data_position = 0
        for data in markets:
            string_position = 7
            names.insert(len(names),'')
            building_name = True
            while building_name:
                string_data = str(data)[string_position]
                if string_data != "'":
                    names[data_position] += string_data
                else:#built name
                    building_name = False
                string_position += 1
            data_position += 1
        return names

    #uses raw markets data and a product name to get specific market information
    #needs products because of tradeogres odd JSON structure
    #data_type: 'price', 'volume', 'high', 'low', 'bid', 'ask', 'initialprice'
    def productGet(self, markets, products, product, data_type):
        index = 0
        for i in range(0,len(products)):#get the product index
            if products[i] == product:
                index = i
                break
        return float(markets[index]['BTC-'+product][data_type])
        
