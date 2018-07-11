import requests
from bs4 import BeautifulSoup


request = requests.get("http://www.google.com")

print(request.content)