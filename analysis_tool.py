# -*- coding: utf-8 -*-

import json
import requests
import time
import os
from io import BytesIO
import api_tool
import matplotlib.pyplot as plt

#Both individualPosition and teamPosition are computed by the game server and are different versions of the most likely position played by a player. The individualPosition is the best guess for which position the player actually played in isolation of anything else. The teamPosition is the best guess for which position the player actually played if we add the constraint that each team must have one top player, one jungle, one middle, etc. Generally the recommendation is to use the teamPosition field over the individualPosition field.
def check_lane(summonerName, gameId):
    match_json = api_tool.call_match(gameId)
    for i in match_json.get("info").get("participants"):
        #print(i.get("summonerName").encode('utf-8').strip())
        #print(summonerName.strip())
        if i.get("summonerName").replace(" ", "").strip().lower().encode('utf-8') ==summonerName:
            #if i.get("teamPosition")==i.get("individualPosition"):
            #    return i.get("teamPosition")
            return i.get("individualPosition")
    else:
        return "UNKNOWN"
    return 0

# 최근 n경기 랭크게임 주포지션
def check_lane_n(summonerName, n):
    summoner_json = api_tool.call_summoner(summonerName)
    summonerName = summonerName.replace(" ", "").strip().lower()
    puuid = summoner_json.get("puuid")
    match_list = api_tool.call_matchlist(puuid,1,20)
    pos_dict = {"TOP":0, "JUNGLE":0, "MIDDLE":0, "BOTTOM":0, "UTILITY":0, "UNKNOWN":0, "Invalid":0}
    k=0
    if puuid == None:
        return "", "puuid None"
    for i in match_list:
        match_json = api_tool.call_match(i)
        #print(match_json.get("info").get("queueId"))
        if match_json.get("info").get("queueId")==420:
            k+=1
            lane = check_lane(summonerName,i)
            #print(lane)
            pos_dict[lane]+=1
        if k==n:
            break
    print(summonerName)
    print(pos_dict)
    print(max(pos_dict.keys(), key=lambda k : pos_dict[k]))
    if max(pos_dict.values()) == 0:
        main_position = "No Recent Rank Game"
    else:
        main_position = max(pos_dict.keys(), key=lambda k : pos_dict[k])

    return pos_dict, main_position


def challenger_list():
    challenger_json = api_tool.call_user_challenger("RANKED_SOLO_5x5")
    #with open("./challenger.json", 'w') as outfile:
    #    json.dump(challenger_json, outfile, indent=4, sort_keys=True)
    chal_list = []
    for i in challenger_json.get("entries"):
        #print(i.get("summonerName"))
        chal_list.append(i.get("summonerName"))
    f = open("./challenger_list", 'w')
    for i in chal_list:
        f.write(i.encode('utf-8'))
        f.write('\n')
    f.close()
    return chal_list

# 해당 유저 최근 10 게임중 랭크에서 정글 플레이한 경우 동선 이미지 저장
def jungle_move_map(summonerName):
    summoner_json = api_tool.call_summoner(summonerName)
    summonerName = summonerName.replace(" ", "").strip().lower()
    puuid = summoner_json.get("puuid")
    match_list = api_tool.call_matchlist(puuid,1,10)
    k = 0
    if puuid == None:
        return
    for match in match_list:
        match_json = api_tool.call_match(match)
        # print(match_json.get("info").get("queueId"))
        for i in match_json.get("info").get("participants"):
            if i.get("summonerName").replace(" ", "").strip().lower().encode('utf-8') == summonerName:
                if i.get("individualPosition") == "JUNGLE": # 정글인 게임
                    timeline_json = api_tool.call_match_timeline(match)
                    print(i.get("championName"))

                    for participant in timeline_json.get("participants"):
                        if participant.get("puuid") == puuid:
                            participantId = participant.get("participantId") # 해당 게임에서의 참가자번호
                            break
                    print(participantId)
                    for idx, t in enumerate(timeline_json.get("frames")):
                        print("Timeframe : " + str(idx))
                        print("x : "+str(t.get("participantFrames").get(str(participantId)).get("position").get("x")))
                        print("y : "+str(t.get("participantFrames").get(str(participantId)).get("position").get("y")))

                        # 이 번호를 가지고 timeline_json 에서 timeframe별 좌표 구하면됨
    return



def main():
    #check_lane_n("omgabie" ,10)

    # 1. challenger list json file 생성
    #chal_list = challenger_list()

    # 2. challenger position list
    '''
    file_path = "./challenger_list"
    with open(file_path) as f:
        challenger_list = f.readlines()
        
    f = open("./challenger_position_list", 'w')
    for summonerName in challenger_list:
        summonerName = summonerName.replace(" ", "").strip('\n').strip().lower()
        #print(summonerName)
        pos_dict, position = check_lane_n(summonerName,10)
        f.write(summonerName)
        f.write('\t')
        f.write(position)
        f.write('\n')
    f.close()
    '''
    # 3. challenger position visualization
    # To-Do
    '''
    file_path = "./challenger_position_list"
    f = open(file_path)
    pos_dict={}
    chal_cnt = 0
    while True:
        line = f.readline().strip().split('\t')
        if len(line) <= 1:
            break
        id = line[0]
        pos = line[1]
        if pos in ['MIDDLE', 'UTILITY', 'BOTTOM', 'JUNGLE', 'TOP']:
            chal_cnt += 1
            pos_dict[pos] = pos_dict.get(pos, 0) + 1
    f.close()
    print(pos_dict)
    ratio = []
    labels = ['MIDDLE', 'UTILITY', 'BOTTOM', 'JUNGLE', 'TOP']
    for i in pos_dict:
        ratio.append(pos_dict.get(i))
    print(ratio)
    colors = ['red', 'violet', 'purple', 'olivedrab', 'dodgerblue']
    plt.pie(ratio, labels=labels, autopct = "%.1f%%", colors = colors)
    plt.show()
    '''
    #4. 챌린저 최근경기 동선 이미지 시각화
    jungle_move_map("가쎄삼다")
    # 정글러 추출 및 챔피언*시간대 별 현위치 시각화
    return

if __name__ == "__main__":
    main()