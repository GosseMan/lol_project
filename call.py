import requests
import json

api_key = "RGAPI-78017ae1-e579-41e1-bc41-35ac57be4074"

name = input("Summoner GAME ID : ")
URL  = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
res = requests.get(URL, headers={"X-RIOT-Token":api_key})
if res.status_code ==200:
    print(res.text)
else:
    selectnum("No player")


json_summoner = json.loads(res.text)
print(json_summoner['accountId'])
URL_match = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/m2sn6IZirSDgeDuSlI080rl3yIUdGnLpuBwlT5XxL08R"
res_match = requests.get(URL_match, headers={"X-RIOT-Token":api_key})
print(res_match.text)
