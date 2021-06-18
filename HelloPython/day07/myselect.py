import pymysql as pysql

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

sql = "SELECT COL01, COL02, COL03 FROM SAMPLE"
cur.execute(sql)

conn.commit()

rows = cur.fetchall()
print(rows)


conn.close()


