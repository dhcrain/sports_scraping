import requests
from bs4 import BeautifulSoup

search_url = "http://www.nfl.com/players/search?category=name&filter=john+simon&playerType=current"
content = requests.get(search_url)

souper = BeautifulSoup(content.text, "html.parser")

elements = souper.find(id="result")

base_url = "http://www.nfl.com/"
url = base_url + elements.a.attrs['href']

content = requests.get(url)
souper = BeautifulSoup(content.text, "html.parser")
print(souper.find(class_="data-table1"))
