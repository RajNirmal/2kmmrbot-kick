from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.enums import EDOTAGCMsg
import logging
import json

# logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def steamLogin():
    print("steam login success")
    # dota.launch()
    friends = client.friends

    for f in friends:
        print(f.name)
        print(f.rich_presence)
        
    
    
@client.on('ready')
def friend_list_ready(steamFriendList):
    print("Friend list ready")
    print(steamFriendList)

@dota.on('ready')
def fetch_player_card():
    print('dota launched')
    dota.request_top_source_tv_games(search_key='185059559') #wtf is search key doing? 
    
#Only event that is emitted properly
@dota.on('top_source_tv_games')
def top_source_games(message):
    print("Received source games")
    print(message)
    for games in message.game_list:
        print(f"Found game with id {games.lobby_id}")
        for player_id in players:
            if(player_id == '76561199026231378'):
                print('Match found for this player')
        # https://steamcommunity.com/profiles/76561198276703796/
    
#Works but does not contain any useful data for us
@dota.on('profile_data')
def profile_details(details, details2):
    print("Received profile data")
    print(details)
    print(details2)

#Didnt work
@dota.on('matches')
def match_details(match_id, eresult, match):
    print('got match details')
    print(match)
    print(match_id)
    print(eresult)

#Dont remember if it worked or not
@dota.on('player_match_history')
def player_match_history(message):
    print('got message details')
    print(message)


#Gives out complete garbage data that is not useful for us in any manner
@dota.on('profile_card')
def print_profile_card(account_id, profile_card):
    print("Printing profile card")
    if account_id == 428247593:
        print (profile_card)


def match_details_handler():
    print("coming to match details handler")

with open('steam_credentials.json') as f:
    steam_credentials = json.loads(f.read())
    client.cli_login(steam_credentials['steam_username'],steam_credentials['steam_password'])
    client.run_forever()





