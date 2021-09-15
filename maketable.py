import pymysql


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