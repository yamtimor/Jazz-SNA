import wikipedia
from pprint import pprint
from player import Player
from wiki_data_extractor import extract_players, extract_discography


def main():
    players_list = extract_players()
    # for player in players_list:
        # p = Player(player['player'], player['instrument'], 'test', 'test')
        # print(p)
    pprint(extract_discography(players_list[0]['player']))

if __name__ == "__main__":
    main()