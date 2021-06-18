import requests

response = requests.get("http://localhost/WEBCRAWL/index.html")
response.encoding = "utf-8"
print(response.text)