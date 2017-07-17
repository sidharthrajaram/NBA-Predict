from googleapiclient.discovery import build
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import urllib.request
from io import StringIO
import numpy as np
import re

DATA_FILE = "scraped_stats.csv"

my_api_key = "AIzaSyBFduswXFFPsvWucTdrHN7uL0050WH4SMo" #if it expires just update it fellas 
my_cse_id = "013234493367067861201:e_sqh9dvrhy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def statRetrieval(player):

	results = google_search(player, my_api_key, my_cse_id, num=1)
	prelim_url = results[0]["formattedUrl"]

	# print("RESULTS")
	# print(results[0]["formattedUrl"])
	url = ""
	if "https://" not in prelim_url: 
		url = "https://"+results[0]["formattedUrl"]
	else:
		url = prelim_url

	print("Accessing",url)

	# url = ""
	player_feature_tensor = []

	print()
	with urllib.request.urlopen(url) as response:
		r = response.read().decode('latin-1')   		

	content = re.sub(r'(?m)^\<!--.*\n?', '', r)
	content = re.sub(r'(?m)^\-->.*\n?', '', content)

	soup = BeautifulSoup(content, 'html.parser')
	tables = soup.findAll('table')

	#boiler plate but whatever
	reg_table_rows = tables[0].findAll('tr')
	reg_data = reg_table_rows[1].findAll('td')

	reg_stats = []
	reg_stats = np.asarray(reg_stats)

	adv_table_rows = tables[4].findAll('tr')
	adv_data = adv_table_rows[1].findAll('td')

	adv_stats = []
	adv_stats = np.asarray(adv_stats)

	for d in range(len(adv_data)):
		if(d>=4):
			stat = adv_data[d].text
			try:
				adv_stats = np.append(adv_stats,float(stat))
				# print(float(stat))
			except(ValueError):
				adv_stats = np.append(adv_stats, float(0))
				pass

	for d in range(len(reg_data)):
		if(d>=5):
			stat = reg_data[d].text
			try:
				reg_stats = np.append(reg_stats, float(stat))
				# print(float(stat))
			except(ValueError):
				reg_stats = np.append(reg_stats, float(0))
				pass

	# print(reg_stats)
	# print()
	# print(adv_stats)
	player_feature_tensor.append(reg_stats)
	player_feature_tensor.append(adv_stats)

	# print("PFT:")
	# print(np.asarray(player_feature_tensor))

	np.savetxt(DATA_FILE, player_feature_tensor,fmt='%1.3f', delimiter=',', newline='\r\n')
	print("DATA SAVED!")


#testing section
if __name__ == "__main__":

	# try:
	statRetrieval("KARLANTHONYTOWNS")
	# except:
	# 	print("We couldn't get the data on this player!")
