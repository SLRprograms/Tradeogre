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

    #returns raw data of all the markets.
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

    #returns list of product names with raw markets data.
    def marketsNames(self, markets):
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

    #uses raw markets data and a market name to get specific market information.
    #needs list of names because of tradeogres odd JSON structure.
    #data_type: 'price', 'volume', 'high', 'low', 'bid', 'ask', 'initialprice'.
    def marketsGet(self, markets, names, name, data_type):
        index = 0
        for i in range(0,len(names)):#get the product index
            if names[i] == name:
                index = i
                break
        return float(markets[index]['BTC-'+name][data_type])

    #returns a list of orderbook data with the price as [orderPrice,amountBooked].
    #because of tradeogres wierd JSON structure,
    #price is needed to incriment through the data.
    #buys are in order from highest price (BID) to lowest price.
    #sells are in order from lowest price (ASK) to highest price.
    def orderBook(self, product, side):
        attempts = 0
        while True:
            try:
                r = requests.get(self.api_url + '/orders/BTC-'+str(product))
                book = r.json()[side]
                orderPrice = []
                amountBooked = []
                for i in book:
                    orderPrice.insert(len(orderPrice),i)
                if side == 'buy':
                    orderPrice = list(reversed(sorted(orderPrice)))
                elif side == 'sell':
                    orderPrice = list(sorted(orderPrice))
                for i in orderPrice:
                    amountBooked.insert(len(amountBooked),book[i])
                return [orderPrice,amountBooked]
            except:
                attempts += 1
                print 'FAILED orderBook ' + str(attempts)
                time.sleep(60)


