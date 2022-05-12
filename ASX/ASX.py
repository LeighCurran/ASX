"""Abstraction of the ASX API"""
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout

class api:

    def __init__(self):
        self.Error = None
        self.token = None
        self.url = 'https://www.asx.com.au/asx/1/share/'  
        api_adapter = HTTPAdapter(max_retries=2)
        
        """Create a session and perform all requests in the same session"""
        session = requests.Session()
        session.mount(self.url, api_adapter)
        session.headers.update({'Accept': 'application/json', 'User-Agent': 'ASX.py', 'Accept-Encoding' : 'gzip, deflate, br', 'Connection' : 'keep-alive' })
        self.session = session

    def request(self, Symbol): 
        try:
            request = self.session.get(self.url + Symbol)
            if (request.status_code == 200):
                return request.json()
            else:
                self.Error = 'Data request failed: ' + request.reason  
        except Timeout:
            self.Error = 'Data request timed out'

    def getdata(self, Symbol):
        data = self.request(Symbol)
        self.last_price = data['last_price']
        self.open_price = data['open_price']
        self.day_high_price = data['day_high_price']
        self.day_low_price = data['day_low_price']
        self.change_price = data['change_price']
        self.change_in_percent = data['change_in_percent']
        self.bid_price = data['bid_price']
        self.offer_price = data['offer_price']
        self.previous_close_price = data['previous_close_price']
        self.previous_day_percentage_change = data['previous_day_percentage_change']
        self.year_high_price = data['year_high_price']
        self.year_low_price = data["year_low_price"]
        self.year_open_price = data["year_open_price"]
        self.year_change_price = data["year_change_price"]
        self.annual_dividend_yield = data["annual_dividend_yield"]