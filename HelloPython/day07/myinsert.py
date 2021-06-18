import pymysql as pysql

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

sql = "INSERT INTO SAMPLE VALUES(3, 3, 3)"
print(cur.execute(sql))
if(cur.execute(sql) > 0):
    print("인서트가 완료되었습니다.")

conn.commit()


sql1 = "SELECT COL01, COL02, COL03 FROM SAMPLE"
cur.execute(sql1)

rows = cur.fetchall()
print(rows)

cur.close()
conn.close()
