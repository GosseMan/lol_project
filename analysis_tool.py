# -*- coding: utf-8 -*-

import json
import requests
import time
import os
from io import BytesIO
import api_tool

#Both individualPosition and teamPosition are computed by the game server and are different versions of the most likely position played by a player. The individualPosition is the best guess for which position the player actually played in isolation of anything else. The teamPosition is the best guess for which position the player actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc. Generally the recommendation is to use the teamPosition field over the individualPosition field.
def check_lane(summonerName, gameId):
    match_json = api_tool.call_match(gameId)
    for i in match_json.get("info").get("participants"):
        #print(i.get("summonerName").encode('utf-8').strip())
        #print(summonerName.strip())
        if i.get("summonerName").replace(" ", "").strip().lower().encode('utf-8') ==summonerName:
            if i.get("teamPosition")==i.get("individualPosition"):
                return i.get("individualPosition")
    else:
        return "UNKNOWN"
    return 0

def check_lane_n(summonerName, n):
    summoner_json = api_tool.call_summoner(summonerName)
    summonerName = summonerName.replace(" ", "").strip().lower()
    puuid = summoner_json.get("puuid")
    match_list = api_tool.call_matchlist(puuid,1,20)
    pos_dict = {"TOP":0, "JUNGLE":0, "MIDDLE":0, "BOTTOM":0, "UTILITY":0, "UNKNOWN":0}
    k=0
    for i in match_list:
        match_json = api_tool.call_match(i)
        #print(match_json.get("info").get("queueId"))
        if match_json.get("info").get("queueId")==420:
            k+=1
            #print(check_lane(summonerName, i))
            pos_dict[check_lane(summonerName,i)]+=1
        if k==n:
            break
    print(summonerName)
    print(pos_dict)
    print(max(pos_dict.keys(), key=lambda k : pos_dict[k]))
    return pos_dict, max(pos_dict.keys(), key=lambda k : pos_dict[k])

    for i in match_json.get("info").get("participants"):
        if i.get("summonerNmae")==summonerNmae:
            if i.get("teamPosition")==i.get("individualPosition"):
                return i.get("individualPosition")
    else:
        return "unknown"
    return 0

def challenger_list():
    challenger_json = api_tool.call_user_challenger("RANKED_SOLO_5x5")
    #with open("./challenger.json", 'w') as outfile:
    #    json.dump(challenger_json, outfile, indent=4, sort_keys=True)
    chal_list = []
    for i in challenger_json.get("entries"):
        #print(i.get("summonerName"))
        chal_list.append(i.get("summonerName"))
    return chal_list

def main():
    chal_list = challenger_list()

    # 1. challenger list
    f = open("./challenger_list", 'w')
    for i in chal_list:
        f.write(i.encode('utf-8'))
        f.write('\n')
    f.close()

    # 2. challenger position list
    f = open("./challenger_position_list", 'w')
    for i in chal_list:
        pos_dict, position = check_lane_n(i,10)
        f.write(i.encode('utf-8').replace(" ", "").strip().lower())
        f.write('\t')
        f.write(position)
        f.write('\n')
    return

if __name__ == "__main__":
    main()