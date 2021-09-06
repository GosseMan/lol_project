import requests
import json
import pymysql

def insert_match(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
    hostname = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
    username = "won"
    password = "gosseyongwon"
    database_name = "test"

    db_test = pymysql.connect(
        host=hostname,
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8"
    )
    # 클라이언트에 insert할 때 한글 깨짐 방지
    cursor = db_test.cursor(pymysql.cursors.DictCursor)
    cursor.execute("set names utf8")
    db_test.commit()
    SQL_QUERY = """
    INSERT INTO LatestMatch(name, matchid, win, killn, death,assist,champ,item0,item1,item2,item3,item4,item5,item6,spell1,spell2)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE matchid = %s, win = %s, killn = %s, death = %s,assist = %s,champ = %s,item0 = %s,item1 = %s,item2 = %s,item3 = %s,item4 = %s,item5 = %s,item6 = %s,spell1 = %s,spell2 = %s
    """
    cursor.execute(SQL_QUERY,[name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p, \
                              match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p])
    db_test.commit()
    return 0

def update_LatestMatch(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
    hostname = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
    username = "won"
    password = "gosseyongwon"
    database_name = "test"

    db_test = pymysql.connect(
        host=hostname,
        port=3306,
        user=username,
        passwd=password,
        db=database_name,

        charset="utf8"
    )
    # 클라이언트에 insert할 때 한글 깨짐 방지
    cursor = db_test.cursor(pymysql.cursors.DictCursor)
    cursor.execute("set names utf8")
    db_test.commit()
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
    db_test.commit()
    return 0

def update_match(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
    hostname = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
    username = "won"
    password = "gosseyongwon"
    database_name = "test"

    db_test = pymysql.connect(
        host=hostname,
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8"
    )
    # 클라이언트에 insert할 때 한글 깨짐 방지
    cursor = db_test.cursor(pymysql.cursors.DictCursor)
    cursor.execute("set names utf8")
    db_test.commit()
    SQL_QUERY = """
    UPDATE LatestMatch SET matchid={}, win={}, killn={}, death={},assist={},champ={},item0={},item1={},item2={},item3={},item4={},item5={},item6={},spell1={},spell2={}
    where name="{}"
    """.format( match_p, win_p, kill_p, death_p, assist_p, champ_p, item0_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p,name_p)
    cursor.execute(SQL_QUERY)
    db_test.commit()
    return 0

def main():
    hostname = "lolproject.c4qilc1sbgk7.ap-northeast-2.rds.amazonaws.com"
    username = "won"
    password = "gosseyongwon"
    database_name = "test"

    db_test = pymysql.connect(
        host=hostname,
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8"
    )

    table_name = "LatestMatch"
    # 클라이언트에 insert할 때 한글 깨짐 방지
    cursor = db_test.cursor(pymysql.cursors.DictCursor)
    cursor.execute("set names utf8")
    db_test.commit()
    SQL_QUERY = """
    DROP TABLE IF EXISTS {}
    """.format(table_name)
    cursor.execute(SQL_QUERY)
    db_test.commit()
    SQL_QUERY2 = """
    CREATE TABLE LatestMatch (
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        matchid BIGINT UNSIGNED NOT NULL,
        win BOOLEAN NOT NULL,
        killn INT UNSIGNED NOT NULL,
        death INT UNSIGNED NOT NULL,
        assist INT UNSIGNED NOT NULL,
        champ INT UNSIGNED NOT NULL,
        item0 INT UNSIGNED NOT NULL,
        item1 INT UNSIGNED NOT NULL,
        item2 INT UNSIGNED NOT NULL,
        item3 INT UNSIGNED NOT NULL,
        item4 INT UNSIGNED NOT NULL,
        item5 INT UNSIGNED NOT NULL,
        item6 INT UNSIGNED NOT NULL,
        spell1 INT UNSIGNED NOT NULL,
        spell2 INT UNSIGNED NOT NULL,
        PRIMARY KEY (idx),
        UNIQUE KEY (name) 
        ) DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    """
    # CHARSET 문자열 인코딩, COLLATE 정렬

    cursor.execute(SQL_QUERY2)
    db_test.commit()
    print('hello')
    SQL_QUERY = """
    INSERT INTO LatestMatch(name, matchid, win, killn, death,assist,champ,item0,item1,item2,item3,item4,item5,item6,spell1,spell2)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    #cursor.execute(SQL_QUERY,['티모삼촌띠모',12345,True,3,3,3,100,1,1,1,1,1,1,1,1,1])
    #print('hi')
    #db_test.commit()
    return
if __name__ == "__main__":
    main()