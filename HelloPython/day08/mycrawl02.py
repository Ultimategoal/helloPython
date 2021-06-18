import requests
from bs4 import BeautifulSoup
import urllib

response = requests.get("http://localhost/WEBCRAWL/index.html")
response.encoding = "utf-8"

html = response.text
soup = BeautifulSoup(html, "html.parser")
tbody = soup.tbody
print(tbody.text)


obj_tbody = soup.find("tbody")

objs_td = obj_tbody.select("td")
for td in objs_td:
    print(td.text)



url = "http://localhost/WEBCRAWL/index.html"
req = urllib.request.urlopen(url)
res = req.read()
 
soup = BeautifulSoup(res,'html.parser')
keywords = soup.find_all('td')
keywords = [each_line.get_text().strip() for each_line in keywords[2:3]]
print(keywords)