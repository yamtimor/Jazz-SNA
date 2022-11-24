import wikipedia
import pandas
from pprint import pprint

# list of bebop jazz players
bebop_players = wikipedia.page("List of bebop musicians").content

def wiki_data_extractor():
    players = []
    for element in filter(lambda x: bool(x) and not x.startswith("=="), bebop_players.split('\n')):
        players.append(element.split('-')[0][:-1])

    return players

if __name__ == "__main__":
    print(wiki_data_extractor())