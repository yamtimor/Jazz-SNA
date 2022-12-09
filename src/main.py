import wikipedia
from pprint import pprint
from player import Player
from wiki_data_extractor import extract_players, extract_discography


def main():
    list_of_players = extract_players()
    for player in list_of_players:
        print(player)
    # players = create_players(list_of_players)
    # pprint(players)    # for player in players_list:
        # p = Player(player['player'], player['instrument'], 'test', 'test')
        # print(p)
    # pprint(extract_discography(players_list[0]['player']))



if __name__ == "__main__":

    main()