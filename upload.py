import requests
import json
import pymysql

def insert_match(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p):
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
    INSERT INTO LatestMatch(name, matchid, win, killn, death,assist,champ,item1,item2,item3,item4,item5,item6,spell1,spell2)
    VALUES("{}",{},{},{},{},{},"{}","{}","{}","{}","{}","{}","{}","{}","{}")
    """.format(name_p, match_p, win_p, kill_p, death_p, assist_p, champ_p, item1_p, item2_p, item3_p, item4_p, item5_p, item6_p, spell1_p, spell2_p)
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
    CREATE TABLE {} (
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT,
        name TINYTEXT NOT NULL,
        matchid INT UNSIGNED NOT NULL,
        win BOOLEAN NOT NULL,
        killn INT UNSIGNED NOT NULL,
        death INT UNSIGNED NOT NULL,
        assist INT UNSIGNED NOT NULL,
        champ VARCHAR(30) NOT NULL,
        item1 VARCHAR(30) NOT NULL,
        item2 VARCHAR(30) NOT NULL,
        item3 VARCHAR(30) NOT NULL,
        item4 VARCHAR(30) NOT NULL,
        item5 VARCHAR(30) NOT NULL,
        item6 VARCHAR(30) NOT NULL,
        spell1 VARCHAR(30) NOT NULL,
        spell2 VARCHAR(30) NOT NULL,
        PRIMARY KEY (idx)
        ) DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    """.format(table_name)
    # CHARSET 문자열 인코딩, COLLATE 정렬
    cursor.execute(SQL_QUERY2)
    db_test.commit()
    #insert_match("티모삼촌띠모",12345,1,3,3,3,"나르","1","2","3","4","5","6","1","2")
    return
if __name__ == "__main__":
    main()