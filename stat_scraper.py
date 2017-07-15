from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyC-djDYtVMjEJSubc8oaE-W-EEUrHJD0g0"
my_cse_id = "013234493367067861201:e_sqh9dvrhy"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'westbrook', my_api_key, my_cse_id, num=1)
for result in results:
    print(result.keys())

'''
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
'''