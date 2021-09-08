import json
import requests
import time
api_key = "RGAPI-6a377f3a-7ddf-42fe-9f2c-bf1469161a10"
tmp_key = "60ysuDs_5TzndzPkQa8fBT3XAikjhb05cAHcc9WQ-bd05b9e25qw5Dw6Yvh6CvGU1iD5L4xqfFNlnA"

def latest_version():
    version_url = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    version_list = json.loads(version_url.text)
    return version_list[0]
version = latest_version()

def call_summoner(name):
    #name = input("Summoner GAME ID : ")
    url  = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return json.loads(res.text)
    except:
        print("call_summoner Error" + res.text)
        return 0

def call_matchlist(accountid, beginIndex, endIndex):
    url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountid + "?endIndex=" + str(endIndex) + "&beginIndex=" + str(beginIndex)
    # v5로 바꿔야 할거같음
    # URL_match = "https://kr.api.riotgames.com/lol/match/v5/matches/by-puuid/" +summoner_json+['puuid']+"/ids"
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        #print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return (json.loads(res.text)).get("matches")
    except:
        print("call_summoner Error" + res.text)
        return 0

def call_champ():
    url = "http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion.json"
    res = requests.get(url, headers={"X-RIOT-Token":api_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        #print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return (json.loads(res.text)).get("matches")
    except:
        print("call_summoner Error" + res.text)

def call_exp(user_id,champ_code):
    url = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+user_id+"/by-champion/"+champ_code
    res = requests.get(url, headers={"X-RIOT-Token":api_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        #print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return (json.loads(res.text)).get("matches")
    except:
        print("call_summoner Error" + res.text)
        return 0
    return 0

def call_match(gameId):
    url = "https://kr.api.riotgames.com/lol/match/v4/matches/" + gameId
    res = requests.get(url, headers={"X-RIOT-Token":api_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return json.loads(res.text)
    except:
        print('Error) Call Match')

def call_match_v5(gameId):
    url = "https://asia.api.riotgames.com/lol/match/v5/matches/" + gameId
    res = requests.get(url, headers={"X-RIOT-Token":tmp_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        #print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return (json.loads(res.text)).get("matches")
    except:
        print("call_summoner Error" + res.text)
        return 0

def call_match_timeline(gameId):
    url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/" + gameId
    res = requests.get(url, headers={"X-RIOT-Token":api_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        #print(res.text)
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return (json.loads(res.text)).get("matches")
    except:
        print("call_summoner Error" + res.text)
        return 0

def call_user_tier(division,tier,queue,page):
    #division에는 I, II, III, IV
    #tier에는 DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, IRON
    #queue에는 RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
    #page는 출력할 page수
    url = 'https://kr.api.riotgames.com/lol/league/v4/entries/'+queue+'/'+tier+'/'+division+'?page='+str(page)
    res = requests.get(url,headers={"X-RIOT-Token":api_key})
    try:
        res = requests.get(url, headers={"X-RIOT-Token":api_key})
        while res.status_code == 429:
            time.sleep(60)
            print('---(Code 429)Waiting---')
            res = requests.get(url, headers={"X-RIOT-Token": api_key})
        return json.loads(res.text)
    except:
        print('Error) Call Match')

    '''
    elif res.status_code == 400:
        print("Summoner Error) 400 (Bad Request) : This error indicates that there is a syntax error in the request and the request has therefore been denied.")
    elif res.status_code == 401:
        print("Summoner Error) : 401 (Unauthorized) This error indicates that the request being made did not contain the necessary authentication credentials (e.g., an API key) and therefore the client was denied access.")
    elif res.status_code == 403:
        print("Summoner Error) : 403 (Forbidden) This error indicates that the server understood the request but refuses to authorize it.")
    elif res.status_code == 404:
        print("Summoner Error) : 404 (Not Found) This error indicates that the server has not found a match for the API request being made.")
    elif res.status_code == 415:
        print("Summoner Error) : 415 (Unsupported Media Type) This error indicates that the server is refusing to service the request because the body of the request is in a format that is not supported.")
    elif res.status_code == 429:
        print("Summoner Error) : 429 (Rate Limit Exceeded) This error indicates that the application has exhausted its maximum number of allotted API calls allowed for a given duration.")
    elif res.status_code == 500:
        print("Error) : 500 (Internal Server Error) This error indicates an unexpected condition or exception which prevented the server from fulfilling an API request.")
    elif res.status_code == 503:
        print("Error) : 503 (Service Unavailable) This error indicates the server is currently unavailable to handle requests because of an unknown reason. The Service Unavailable response implies a temporary condition which will be alleviated after some delay.")
    else:
        print("Unknown Error")
    return 0
    '''
