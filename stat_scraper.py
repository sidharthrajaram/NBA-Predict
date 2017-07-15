from googleapiclient.discovery import build
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

my_api_key = "AIzaSyC-djDYtVMjEJSubc8oaE-W-EEUrHJD0g0" #NOTE: I USED ALL MY CALLS LOL SO GET A NEW KEY AND REGISTER SHIT
my_cse_id = "013234493367067861201:e_sqh9dvrhy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

PLAYERS = ["Lebron James", "Russell Westbrook", "Stephen Curry", "Paul George", "Kevin Durant"]
for player in PLAYERS:
	results = google_search(player, my_api_key, my_cse_id, num=1)
	print results[0]["formattedUrl"]
	stats = pd.read_html("https://"+results[0]["formattedUrl"])
	df = pd.DataFrame(stats[0])

	for index, row in df.iterrows():
		if index == 0:
			rookie_stats = row
			break
	rookie_stats = rookie_stats[:25]
	print (np.asarray(rookie_stats))[5:]
	print len((np.asarray(rookie_stats))[5:])