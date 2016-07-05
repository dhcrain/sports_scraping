from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.


def sports_scraping_index(request):
    player_name = request.GET.get("player_name") or "John Simon"
    player_type = request.GET.get("player_type")
    search_url = "http://www.nfl.com/players/search?category=name&filter={}&playerType={}".format(player_name, player_type)
    content = requests.get(search_url).text
    souper = BeautifulSoup(content, "html.parser")
    elements = souper.find(id="result")
    base_url = "http://www.nfl.com/"
    url = base_url + elements.a.attrs['href']
    content = requests.get(url)
    souper = BeautifulSoup(content.text, "html.parser")
    player_bio = str(souper.find(id="player-bio"))
    stats = str(souper.find(id="player-stats-wrapper"))
    context = {
    "player_bio": player_bio,
    "stats": stats,
    "player_name": player_name
    }
    return render(request, "index.html", context)
