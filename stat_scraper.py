#DEPRECATED, CHECK SCRAPER.PY for current scraper
from googleapiclient.discovery import build
import pandas as pd
from bs4 import BeautifulSoup
import requests
from io import StringIO
import numpy as np
#print statements are updated for python 3 

COLUMNS_START = 5
COLUMNS_END = 30
DATA_FILE = "player_statistics.csv"

player_list = open("players.txt", "r")
all_players = []
for player in player_list:
	all_players.append(player)

my_api_key = " " 
my_cse_id = "013234493367067861201:e_sqh9dvrhy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def statRetrievalOld(player):
	player_feature_tensor = []
	print()
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
			print(np.asarray(rookie_stats))

			player_feature_tensor.append((np.asarray(rookie_stats)))

		except(ValueError):
			print("We weren't able to get the player or the stats!")
			pass
	except (RuntimeError, TypeError, NameError, KeyError):
		print("WOOPS!")
		pass

	np.savetxt(DATA_FILE, player_feature_tensor,fmt='%1.3f', delimiter=',', newline='\r\n')


#testing section
if __name__ == "__main__":

	# statRetrieval("Damian Lillard")

	all_players = ["Damian Lillard"]

	#for caching test
	# player_feature_tensor = np.genfromtxt('player_statistics.csv', delimiter=',', invalid_raise=False)
	player_feature_tensor = []

	for player in all_players:
		print("****************************")
		try:
			results = google_search(player, my_api_key, my_cse_id, num=1)
			url = results[0]["formattedUrl"]
			print(url)

			try:
				stats = pd.read_html("https://"+results[0]["formattedUrl"])

				df = pd.DataFrame(stats[0])

				for index, row in df.iterrows():
					if index == 0:
						rookie_stats = row
						break

				rookie_stats = rookie_stats[COLUMNS_START:COLUMNS_END]

				#print statements for python 3 
				print(np.asarray(rookie_stats))
				print("******")

				print(len((np.asarray(rookie_stats))))
				player_feature_tensor.append((np.asarray(rookie_stats)))

				print()
				print(np.asarray(player_feature_tensor))

				#for caching test
				# player_feature_tensor = np.concatenate((player_feature_tensor, np.atleast_2d(np.asarray(rookie_stats))))

			except(ValueError):
				print("!")
				pass
		except (RuntimeError, TypeError, NameError, KeyError):
			pass

	#print statements for python 3
	np.savetxt(DATA_FILE, player_feature_tensor,fmt='%1.3f', delimiter=',', newline='\r\n')

	existing_data = np.genfromtxt(DATA_FILE, delimiter=',', invalid_raise=False)
	print("UPDATED DATA")
	print(existing_data)

