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
URL_match = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + input_account
res_match = requests.get(URL_match, headers={"X-RIOT-Token":api_key})
print(res_match.text)
json_object = json.loads(res_match.text)
match_object = json_object.get("matches")
version = "11.14.1"
champ_json = requests.get("http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion.json")
champ_object = json.loads(champ_json.text)

for matches in match_object:
    print(matches["role"],"-",matches["lane"])


with open('champ_engtokor.json', 'w') as champ_engtokor:
    print(champ_engtokor)
    champ_EtoK = json.load(champ_engtokor)
    
    print (champ_EtoK)

for matches in match_object:
    for champ in champ_object["data"]:
        # print(champ_object["data"][champ]["key"], " /// ", matches["champion"])
        if int(champ_object["data"][champ]["key"])==matches["champion"]:
            print(champ_EtoK[champ])

'''
할일 : dump / dumps, load / loads 차이 찾기. champ_engtokor.json 읽는 법 찾기.
'''