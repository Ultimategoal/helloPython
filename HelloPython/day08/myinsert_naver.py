import pymysql as pysql

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

sql = """INSERT INTO jmt (title, link, description, bloggername, bloggerlink, postdate)
        VALUES(%s, %s, %s, %s, %s, %s)"""
cur.execute(sql, ('3','3','3','3','3','3'))
if(cur.execute(sql) > 0):
    print("인서트가 완료되었습니다.")

conn.commit()
cur.close()
conn.close()
