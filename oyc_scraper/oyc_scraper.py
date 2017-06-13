#! usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from selenium.webdriver.common.by import By


base_url = "http://oyc.yale.edu"
resource_path = "/political-science/plsc-114#sessions"


def retrieve_lecture_links():

	x = requests.get(base_url + resource_path)
	soup = BeautifulSoup(x.content, 'html.parser')

	all_td = soup.find_all('td', class_="views-field views-field-field-session-display-title-value")

	lect_links = []

	for _ in all_td:
		lect_links.append(base_url + str(_.a.get('href')))

	return lect_links


def get_transcript_links(lecture_link):

	x = requests.get(lecture_link)
	soup = BeautifulSoup(x.content, 'html.parser')
	return base_url + soup.find('a', id='course_media_transcript').get('onclick').split("'")[1]


def get_transcript(transcript_link):
	x = requests.get(transcript_link)
	soup = BeautifulSoup(x.content, 'html.parser')
	return soup.find('div', class_="views-row views-row-1 views-row-odd views-row-first views-row-last")


def clean_transcript(transcript):

	new_tran = str(transcript)
	new_tran = re.sub('<h3>', '\n\n', new_tran)
	new_tran = re.sub('<p>', '\n', new_tran)
	new_tran = re.sub('<[^<]+?>', '', new_tran)
	return new_tran


def write_transcript(transcript, i):
	file_name = "lecture_" + str(i) + "_transcript.txt"
	f = open(file_name, 'w')
	f.write(transcript)
	f.close()


def retrieve_transcripts():
	i = 0
	lect_links = retrieve_lecture_links()

	for _ in lect_links:

		transcript_url = get_transcript_links(_)
		transcript = get_transcript(transcript_url)
		i += 1
		cleaned = clean_transcript(transcript)
		write_transcript(cleaned, i)

def selenium_transcripts():

	lect_links = retrieve_lecture_links()
	driver = webdriver.Firefox()
	#driver.get(lect_links[0])

	for _ in lect_links:

		driver.get(_)
		driver.find_element_by_id("course_media_transcript").click()

		lecture_window = driver.window_handles[0]
		transcript_window = driver.window_handles[1]
		driver.switch_to.window(transcript_window)

		##
		blah = driver.find_element_by_id("transcript_course_title")
		print(blah.text)

		driver.close()
		driver.switch_to.window(lecture_window)
		blah = driver.find_element_by_id("overview")
		print(blah.text)


	driver.close()

#retrieve_transcripts()

selenium_transcripts()