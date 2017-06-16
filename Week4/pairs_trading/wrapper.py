#!/usr/bin/env python3

import requests
import json


class Scraper:

    def __init__(self):
        self.quote_url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="

    def get_quote(self, symbol):
        path = self.quote_url + symbol

        try:
            content_ = requests.get(path).content
        except:
            return {'Status': 'FAILURE'}

        try:
            obj = json.loads(str(content_, 'utf-8'))
        except:
            return {'Status': 'FAILURE'}

        return obj


if __name__ == "__main__":
    msft_quote = Scraper().get_quote('MSFT')
    goog_quote = Scraper().get_quote('GOOG')
    print(msft_quote, goog_quote)