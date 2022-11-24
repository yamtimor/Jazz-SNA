import wikipedia
from pprint import pprint

# list of bebop jazz players
bebop_players = wikipedia.page("List of bebop musicians").content

def extract_players():
    players = []

    for element in filter(lambda x: bool(x) and not x.startswith("=="), bebop_players.split("\n")[1:]):
        players.append(
            {
                "player": element.split('-')[0][:-1],
             "instrument": element.split('-')[0][:-1]
            }
        )
    return players

if __name__ == "__main__":
    print(extract_players())