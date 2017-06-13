#!/usr/bin/env python3

# standard library
import csv
import re

# Third party libraries
from bs4 import  BeautifulSoup
import requests

with open('target_ep/oyc_ep.csv', 'r') as f:
	x = csv.reader(f)
	links = []
	for _ in x:
		links.append(_[0])

	for _ in links:
		y = requests.get(i)
		soup = BeautifulSoup(y.content, 'html.parser')
		s = soup.find_all('a', id = '_media_transcript')
		

