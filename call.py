import requests
import json

api_key = "RGAPI-6a377f3a-7ddf-42fe-9f2c-bf1469161a10"

name = input("Summoner GAME ID : ")
URL  = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
res = requests.get(URL, headers={"X-RIOT-Token":api_key})
print(res)
if res.status_code ==200:
    print(res.text)
else:
    print("No player")


json_summoner = json.loads(res.text)
input_account = json_summoner['accountId']
# v5로 바꿔야 할거같음
# URL_match = "https://kr.api.riotgames.com/lol/match/v5/matches/by-puuid/" +json_summoner['puuid']+"/ids"
URL_match = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + input_account
res_match = requests.get(URL_match, headers={"X-RIOT-Token":api_key})
print(res_match.text)
json_object = json.loads(res_match.text)
match_object = json_object.get("matches")
version = "11.15.1"
champ_json = requests.get("http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion.json")
champ_object = json.loads(champ_json.text)


with open('champ_engtokor.json', 'r') as champ_engtokor:
    champ_EtoK = json.load(champ_engtokor)

with open('game_type.json', 'r') as game_type:
    game_code = json.load(game_type)


for matches in match_object:
    for champ in champ_object["data"]:
        # print(champ_object["data"][champ]["key"], " /// ", matches["champion"])
        if int(champ_object["data"][champ]["key"])==matches["champion"]:
            if str(matches['queue']) in game_code:
                print(game_code[str(matches['queue'])],'-',champ_EtoK[champ], '-' ,matches["role"],":",matches["lane"])
            else:
                print('기타모드 -',champ_EtoK[champ], '-' ,matches["role"],":",matches["lane"])
            exp_json = requests.get("https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+json_summoner['id']+"/by-champion/"+str(matches['champion']), headers={"X-RIOT-Token":api_key})
            exp_object = json.loads(exp_json.text)
            
            print("숙련도 : ",exp_object['championPoints'])
            URL_matchdetail = "https://kr.api.riotgames.com/lol/match/v4/matches/" +str(matches["gameId"])
            matchdetail_json = requests.get(URL_matchdetail,headers={"X-RIOT-Token":api_key})
            matchdetail_object = json.loads(matchdetail_json.text)
            # print(matchdetail_json.text)
            print("승패 : "+matchdetail_object['teams'][0]['win'])
            

