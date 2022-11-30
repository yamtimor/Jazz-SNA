import wikipedia
from pprint import pprint
from player import Player
from wiki_data_extractor import extract_players


def main():
    players_list = extract_players()
    for player in players_list:
        p = Player(player['player'], player['instrument'], 'test', 'test')
        print(p)


if __name__ == "__main__":
    main()