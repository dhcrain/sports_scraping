from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import Http404


# Create your views here.


def sports_scraping_index(request):
    base_url = "http://www.nfl.com/"
    player_name = request.GET.get("player_name") or "John Simon"
    player_type = request.GET.get("player_type")
    search_url =  base_url + "players/search?category=name&filter={}&playerType={}".format(player_name, player_type)
    content = requests.get(search_url).text
    souper = BeautifulSoup(content, "html.parser")
    elements = souper.find(id="result")
    try:
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
    except AttributeError:
        no_player = "There are no results for {}, please refine your search".format(player_name)
        context = {"no_player": no_player,}
    return render(request, "index.html", context)
