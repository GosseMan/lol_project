import pymysql

class uploader:
    def __init__(self, hostname, username, password, database_name):
        self.db = pymysql.connect(
            host=hostname,
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("set names utf8")
        self.db.commit()

    def insert_match(self,insert_row):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("set names utf8")
        self.db.commit()
        SQL_QUERY = """
        INSERT INTO LatestMatch(name, matchid, win, killn, death,assist,champ,item0,item1,item2,item3,item4,item5,item6,spell1,spell2)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE matchid = %s, win = %s, killn = %s, death = %s,assist = %s,champ = %s,item0 = %s,item1 = %s,item2 = %s,item3 = %s,item4 = %s,item5 = %s,item6 = %s,spell1 = %s,spell2 = %s
        """
        cursor.execute(SQL_QUERY,insert_row+insert_row[1:])
        self.db.commit()
        return 0

    def update_LatestMatch(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
        SQL_QUERY = """
        IF (SELECT 1=1 FROM LatestMatch where name = "{}") then
        BEGIN
            UPDATE LatestMatch SET name=%s, match=%s, win=%s, killn=%s, death=%s, assist=%s, champ=%s,
            item0=%s,item1=%s,item2=%s,item3=%s,item4=%s,item5=%s,item6=%s,spell1=%s,spell2=%s
        END;
        ELSE
        BEGIN  
            INSERT INTO LatestMatch(name, matchid, win, killn, death,assist,champ,item0,item1,item2,item3,item4,item5,item6,spell1,spell2)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        END;
        END IF;
        """.format(name_p)
        cursor.execute(SQL_QUERY,[name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p,
                                  item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p,
                                  name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p,
                                  item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p])
        self.db.commit()
        return 0

    def update_match(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
        SQL_QUERY = """
        UPDATE LatestMatch SET matchid={}, win={}, killn={}, death={},assist={},champ={},item0={},item1={},item2={},item3={},item4={},item5={},item6={},spell1={},spell2={}
        where name="{}"
        """.format( match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p,name_p)
        cursor.execute(SQL_QUERY)
        self.db.commit()
        return 0

def main():
    host = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
    user = "won"
    pw = "gosseyongwon"
    db_name = "test"
    latest_up = uploader(host,user,pw,db_name)
    return
if __name__ == "__main__":
    main()