import pymysql as pysql

def insertStock(arr):
    conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
    cur = conn.cursor()
    
    sql = """INSERT INTO stock (s_name, s_code, price, crw_date)
            VALUES(%s, %s, %s, %s)"""
    
    cnt = cur.executemany(sql, arr) 
    print(cnt)
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    arr = [
           ('3','3','3','3'),
           ('3','3','3','3'),
           ('3','3','3','3')
          ]
    insertStock(arr)