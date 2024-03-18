Original node library - https://www.npmjs.com/package/dota2
https://github.com/Arcana/node-dota2

Node library migrated to go - https://github.com/paralin/go-dota2

Python library by valve - https://github.com/ValvePython/dota2

Python game state integration - https://github.com/Daniel-EST/dota2gsipy

Python reference- https://github.com/daveknippers/AghanimsWager/blob/main/DotaBet_GC.py
Things to think about 

Should I be added to the friend list?
Rich presence?
Should I get the lobby id of friends?

RIch presence response -

steam login success
ShieldBro - playing unranked 
{'status': '#DOTA_RP_PLAYING_AS', 'steam_display': '#DOTA_RP_PLAYING_AS', 'num_params': '3', 'party': 'party_id: 28695284236657676 party_state: IN_MATCH open: false members { steam_id: 76561198388513321 }', 'WatchableGameID': '28695284238816623', 'param0': '#DOTA_lobby_type_name_unranked', 'param1': '1', 'param2': '#npc_dota_hero_tidehunter'}


steam login success
ShieldBro - spectating
{'status': '#DOTA_RP_SPECTATING', 'steam_display': '#DOTA_RP_SPECTATING', 'num_params': '0', 'WatchableGameID': '0', 'watching_server': '[A:1:2079334404:28679]', 'watching_from_server': '[A:1:751587355:28679]'}