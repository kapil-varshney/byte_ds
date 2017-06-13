#!/usr/bin env python3

import requests
from bs4 import BeautifulSoup as bs
import json


class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"

	def company_search(self, string):
		resource_path = '?input='+string
		x = requests.get(self.lookup_url + resource_path)
		soup = bs(x.content, 'html.parser')
		body = str(soup)
		return json.loads(body)

	def get_quote(self, string):

		resource_path = '?symbol=' + string
		x = requests.get(self.quote_url + resource_path)
		soup = bs(x.content, 'html.parser')
		body = str(soup)
		return json.loads(body)





