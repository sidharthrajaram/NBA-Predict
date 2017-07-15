from googleapiclient.discovery import build
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
#print statements are updated for python 3 

COLUMNS_START = 5
COLUMNS_END = 30


player_list = open("players.txt", "r")
all_players = []
for player in player_list:
	all_players.append(player)

my_api_key = "AIzaSyC-djDYtVMjEJSubc8oaE-W-EEUrHJD0g0" 
my_cse_id = "013234493367067861201:e_sqh9dvrhy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

# all_players = ["lil dicky", "Lebron James", "Stephen Curry", "Chris Paul"]
player_feature_tensor = []
for player in all_players:
	print("****************************")
	try:
		results = google_search(player, my_api_key, my_cse_id, num=1)
		print(results[0]["formattedUrl"])

		try:
			stats = pd.read_html("https://"+results[0]["formattedUrl"])

			df = pd.DataFrame(stats[0])

			for index, row in df.iterrows():
				if index == 0:
					rookie_stats = row
					break

			rookie_stats = rookie_stats[COLUMNS_START:COLUMNS_END]

			#print statements for python 3 
			print((np.asarray(rookie_stats)))
			print(len((np.asarray(rookie_stats))))

			player_feature_tensor.append((np.asarray(rookie_stats)))
		except(ValueError):
			print("sorry!")
			pass
	except (RuntimeError, TypeError, NameError, KeyError):
		pass
		
#print statements for python 3
print(np.asarray(player_feature_tensor, dtype = float))
np.savetxt('player_stats.txt', np.asarray(player_feature_tensor, dtype = float), delimiter=',') 

