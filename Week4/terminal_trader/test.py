#!/usr/bin env python3

import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd

lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"


def company_search(string):
    resource_path = '?input=' + string
    complete_path = lookup_url + resource_path
    print(complete_path)
    x = requests.get(complete_path)

    soup = bs(x.content, 'html.parser')
    body = str(soup)
    new_dict = json.loads(body)

    print(new_dict)
    print(type(new_dict))

    df = pd.DataFrame.from_dict(new_dict)
    print(df)

company_search("apple")