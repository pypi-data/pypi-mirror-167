# Bazaar.py by Puffball/PuffCode
# v0.1

import importlib.resources
import requests
import json

class Bazaar:
    def __init__(self):
        self.cachedData = []
    
    def updateValues(self):
        res = requests.get("https://api.hypixel.net/skyblock/bazaar").json()['products']
        self.cachedData = res 
    
    def parseItem(self, item):
        with importlib.resources.open_text("bazaarpy", "items.json") as f:
            items = json.load(f)
        #items = json.loads(items)
        # Check if the item argument is a valid name in items.json
        for i in range(len(items['items'])):
            itm = items['items'][i]
            kl = list(itm.keys())
            vl = list(itm.values())
            try:
                pos = vl.index(item)
                pid = kl[pos]
                return pid
            except ValueError:
                pass
        # If the item is not an item name, check if it is a productID
        for i in range(len(items['items'])):
            itm = items['items'][i]
            kl = list(itm.keys())
            vl = list(itm.values())
            try:
                pos = kl.index(item)
                pid = kl[pos]
                return pid
            except ValueError:
                pass
                

    def buyOrders(self, item): # Buy Orders for 'item'
        pid = self.parseItem(item)
        buyOrders = self.cachedData[pid]["buy_summary"]
        return buyOrders

    def sellOrders(self, item): # Sell Orders for 'item'
        pid = self.parseItem(item)
        sellOrders = self.cachedData[pid]["sell_summary"]
        return sellOrders

    def price(self, item): # Buy/Sell Price of 'item'
        pid = self.parseItem(item)
        buyPrice = round(float(self.cachedData[pid]["quick_status"]["buyPrice"]), 1) # Round to 1 decimal place
        sellPrice = round(float(self.cachedData[pid]["quick_status"]["sellPrice"]), 1) # Round to 1 decimal place
        return {"buyPrice": buyPrice, "sellPrice": sellPrice}


    def volume(self, item): # Trading Volume of 'item'
        pid = self.parseItem(item)
        buyVol = int(self.cachedData[pid]["quick_status"]["buyVolume"])
        sellVol = int(self.cachedData[pid]["quick_status"]["sellVolume"])
        return {"buyVolume": buyVol, "sellVolume": sellVol}

    def orderCount(self, item): # Number of Buy/Sell orders open for 'item'
        pid = self.parseItem(item)
        buyCount = int(self.cachedData[pid]["quick_status"]["buyOrders"])
        sellCount = int(self.cachedData[pid]["quick_status"]["sellOrders"])
        return {"buyOrders": buyCount, "sellOrders": sellCount}