import pymysql as pysql

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

sql = "UPDATE SAMPLE SET col02 = 4, col03 = 4 where col01 = 2"
print(cur.execute(sql))
if(cur.execute(sql) > 0):
    print("수정이 완료되었습니다.")

conn.commit()

sql1 = "SELECT COL01, COL02, COL03 FROM SAMPLE"
cur.execute(sql1)

rows = cur.fetchall()
print(rows)


conn.close()
