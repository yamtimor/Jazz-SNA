import wikipedia
from pprint import pprint
from player import Player

# list of bebop jazz players
bebop_players = wikipedia.page("List of bebop musicians").content

def extract_players():

    players = []

    for element in filter(lambda x: bool(x) and not x.startswith("=="), bebop_players.split("\n")[1:]):
        players.append(
            {
                "player": element.split("-")[0][:-1],
             "instrument": element.split("-")[0][:-1]
            }
        )
    return players

def extract_discography(player):

    page = wikipedia.page(player).content
    discography_with_titles = list(filter(lambda x: bool(x), page.split("== Discography ==")[1].split("\n")))
    discography_with_titles = discography_with_titles[:discography_with_titles.index("== References ==")]

    try:
        leader = discography_with_titles[:discography_with_titles.index("=== As sideman ===")][1:]
        sideman = discography_with_titles[discography_with_titles.index("=== As sideman ===")+1:]

        discography = {
            "leader": leader,
            "sideman": sideman
         }
    except:
        "As sideman and As a leader classification does not exist"

    return discography

