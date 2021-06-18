import requests
from bs4 import BeautifulSoup
import urllib
import datetime

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


response = requests.get("http://stock.hankyung.com/apps/rank.panel_sub?market=1")
response.encoding = "euc-kr"
soup = BeautifulSoup(response.text, "html.parser")
sbjs = soup.select(".sbj")

crw_date = datetime.datetime.now().strftime("%Y%m%d,%H%M")

arr = []
for sbj in sbjs:
    s_name = sbj.text
    s_code = sbj.a["href"].split("=")[1]
    price = sbj.parent.select("td")[1].text.replace(",", "")
    arr.append((s_name,s_code,price,crw_date))
    
insertStock(arr)


    
    


