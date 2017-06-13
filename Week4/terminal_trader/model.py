#!/usr/bin env python3

import pandas as pd

from wrapper import Markit
import orm


def retrieve_company_data(company_name):
    markit_object = Markit()
    company_data = pd.DataFrame.from_dict(markit_object.company_search(company_name))
    return company_data


def retrieve_quote(ticker_symbol):
    markit_object = Markit()
    quote_data = markit_object.get_quote(ticker_symbol)
    return quote_data


def identity_verified(username, password):
    return orm.verify_identity(username, password)


def username_available(username):
    return orm.username_available(username)


def create_user(username, password, name):
    orm.create_users(username, password, name)

#retrieve_company_data("apple")
#retrieve_quote("GOOG")
#print(identity_verified('kv','fj'))
#print(username_available('as'))
#create_users('uk', 'blah', 'Uday')