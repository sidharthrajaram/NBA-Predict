import pandas as pd
all_players = ["a"]

def get_unique_id(player):
	return "1234"

def get_player_start(player_id):
	return "2011"


for player in all_players:
	player_id = get_unique_id(player)
	first_season = get_player_start(player_id)
	url = "http://www.basketball-reference.com/players/g/"+player_id"+/gamelog/"+first_season

	a = pd.read_html("http://www.basketball-reference.com/players/g/georgpa01/gamelog/2011")
	#im too tired to write more of this shit 


	#For Each player 
		#Get unique website ID
		#Figure out first season
		#Access page 
		#SCRAPE