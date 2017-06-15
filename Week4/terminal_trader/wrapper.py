#!/usr/bin env python3

import requests
import json


class Markit:

	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"

	def company_search(self, string):
		resource_path = '?input='+string
		content = str(requests.get(self.lookup_url + resource_path).content, 'utf-8')
		return json.loads(content)

	def get_quote(self, string):
		resource_path = '?symbol=' + string
		content = str(requests.get(self.quote_url + resource_path).content, 'utf-8')
		return json.loads(content)


#print(Markit().company_search("apple"))
#print(Markit().get_quote("AAPL"))