import requests
import json
import api_tool

api_key = "RGAPI-6a377f3a-7ddf-42fe-9f2c-bf1469161a10"

summoner_json = api_tool.call_summoner()
matchlist_json = api_tool.call_matchlist(summoner_json['accountId'])
champ_json = api_tool.call_champ()
print(summoner_json)
with open('champ_engtokor.json', 'r',encoding='UTF8') as champ_engtokor_file:
    champEtoK_json = json.load(champ_engtokor_file)
with open('game_type.json', 'r',encoding='UTF8') as game_type_file:
    gameType_json = json.load(game_type_file)

output_dict = {}
output_dict['user_name'] = summoner_json['name']
output_dict['match_log'] = []
n=0
i=0
for matches in matchlist_json:

    if i==1:
        break;
    i = i + 1
    for champ in champ_json["data"]:
        # print(champ_json["data"][champ]["key"], " /// ", matches["champion"])
        if int(champ_json["data"][champ]["key"])==matches["champion"]:
            champ_name = champEtoK_json[champ]
            if str(matches['queue']) in gameType_json:
                game_type = gameType_json[str(matches['queue'])]
            else:
                game_type = '기타모드'
            print(game_type, '-', champEtoK_json[champ], '-', matches["role"], ":", matches["lane"])
            exp_json = api_tool.call_exp(summoner_json['id'],str(matches['champion']))
            print("숙련도 : ",exp_json['championPoints'])
            match_json = api_tool.call_match(str(matches["gameId"]))
            #print(match_json)
            match_timeline_json = api_tool.call_match_timeline(str(matches["gameId"]))
            print(match_timeline_json)
            with open('output.json', 'w') as outfile:
                json.dump(match_timeline_json, outfile, indent=4)
            # print(matchdetail_json.text)
            print("승패 : "+match_json['teams'][0]['win'])

    n=n+1
    output_dict['match_log'].append({"match_index":n, "game_type":game_type, "champ": champ_name,"role" : matches["role"], "lane" : matches["lane"], "result":match_json['teams'][0]['win']})
#print(output_dict)


'''
with open('output.json', 'w') as outfile:
    json.dump(output_dict, outfile, indent=4)
'''