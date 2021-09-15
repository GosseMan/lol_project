import api_tool
import operator
champ_list = []

host = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
user = "won"
pw = "gosseyongwon"
db_name = "test"

summoner_name = input("ID 입력 : ")
summoner_json = api_tool.call_summoner(summoner_name)
matchlist_json = api_tool.call_matchlist(summoner_json['accountId'], 0, 100)
all_champ = {}
champ_json = api_tool.call_champ()
keytochamp = {}
for champ_eng in champ_json['data']:
    champ_id = champ_json['data'][champ_eng]['key']
    keytochamp[int(champ_id)]=champ_json['data'][champ_eng]['name']

for match in matchlist_json:

    champ_name = keytochamp[match['champion']]
    print(champ_name)
    if not champ_name in all_champ:
        all_champ[champ_name]=1
    else:
        all_champ[champ_name] += 1

champ_sorted = sorted(all_champ.items(), reverse=True, key=operator.itemgetter(1))
print(champ_sorted)
