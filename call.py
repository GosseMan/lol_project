import requests
import json
import api_tool

api_key = "RGAPI-6a377f3a-7ddf-42fe-9f2c-bf1469161a10"

summoner_json = api_tool.call_summoner()
matchlist_json = api_tool.call_matchlist(summoner_json['accountId'])
champ_json = api_tool.call_champ()

with open('champ_engtokor.json', 'r') as champ_engtokor:
    champEtoK_json = json.load(champ_engtokor)
with open('game_type.json', 'r') as game_type:
    gameType_json = json.load(game_type)


for matches in matchlist_json:
    for champ in champ_json["data"]:
        # print(champ_json["data"][champ]["key"], " /// ", matches["champion"])
        if int(champ_json["data"][champ]["key"])==matches["champion"]:
            if str(matches['queue']) in gameType_json:
                print(gameType_json[str(matches['queue'])],'-',champEtoK_json[champ], '-' ,matches["role"],":",matches["lane"])
            else:
                print('기타모드 -',champEtoK_json[champ], '-' ,matches["role"],":",matches["lane"])
            exp_json = api_tool.call_exp(summoner_json['id'],str(matches['champion']))
            print("숙련도 : ",exp_json['championPoints'])
            match_json = api_tool.call_match(str(matches["gameId"]))
            # print(matchdetail_json.text)
            print("승패 : "+match_json['teams'][0]['win'])
            

