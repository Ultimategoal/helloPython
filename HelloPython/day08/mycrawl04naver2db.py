import requests
from bs4 import BeautifulSoup

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request

import pymysql as pysql

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

sql = """INSERT INTO jmt (title, link, description, bloggername, bloggerlink, postdate)
        VALUES(%s, %s, %s, %s, %s, %s)"""


client_id = "lsS47FVIoywdBoOaQMgG"
client_secret = "ETrbfw8z3U"
encText = urllib.parse.quote("대흥동맛집")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    xml = response_body.decode('utf-8')
    
    soup = BeautifulSoup(xml, "xml")
    items = soup.select("item")
    
    for item in items:
        title = item.title.text
        link = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate = item.postdate.text
        
        print(title)
        print(link)
        print(description)
        print(bloggername)
        print(bloggerlink)
        print(postdate)
        cnt = cur.execute(sql, (title,link,description,bloggername,bloggerlink,postdate))
        print(cnt)
        
        
else:
    print("Error Code:" + rescode)
    
    
conn.commit()
cur.close()
conn.close()
