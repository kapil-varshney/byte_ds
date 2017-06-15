#!/usr/bin env python3

import pandas as pd

from wrapper import Markit
from orm import ORM


def retrieve_company_data(company_name):
    markit_object = Markit()
    company_data = pd.DataFrame.from_dict(markit_object.company_search(company_name))
    return company_data


def retrieve_market_data(ticker_symbol):
    markit_object = Markit()
    quote_data = markit_object.get_quote(ticker_symbol)
    return quote_data


def identity_verified(username, password):
    return ORM.verify_identity(username, password)


def username_available(username):
    return ORM.username_available(username)


def create_user(username, password, name):
    ORM.create_users(username, password, name)


def retrieve_balance(username):
    return ORM.retrieve_balance(username)


def enough_balance(username, ticker_symbol, num_of_stocks):
    if float(retrieve_market_data(ticker_symbol)['LastPrice'])*num_of_stocks < retrieve_balance(username):
        return True
    else:
        return False


def make_purchase(username, ticker_symbol, volume):
    data = retrieve_market_data(ticker_symbol)
    last_price = float(data['LastPrice'])
    stock_name = data['Name']
    ORM.update_transactions('long', username, ticker_symbol, last_price, volume)
    ORM.update_balance(username, (-1 * volume * last_price))
    ORM.update_holdings(username, ticker_symbol, stock_name, volume, last_price)


def sell_stocks(username, ticker_symbol, volume):
    data = retrieve_market_data(ticker_symbol)
    last_price = float(data['LastPrice'])
    stock_name = data['Name']
    ORM.update_transactions('short', username, ticker_symbol, last_price, volume)
    ORM.update_balance(username, (volume * last_price))
    ORM.update_holdings(username, ticker_symbol, stock_name, (-1 * volume), last_price)


def get_portfolio(username):
    return ORM.fetch_portfolio(username)



retrieve_company_data("abflkdfklm")
#retrieve_market_data("GOOG")
#print(identity_verified('kv','fj'))
#print(username_available('as'))
#create_users('uk', 'blah', 'Uday')
#make_purchase("AAPL")
#Markit.company_search("apple")
#print(retrieve_balance('kapil'))
#print(enough_balance('kapil', 'AAPL', 100))
#make_purchase('kapil', 'AMZN', 10)
#(get_portfolio('kapil'))