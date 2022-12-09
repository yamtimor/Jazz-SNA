import wikipedia
from pprint import pprint
import networkx as nx

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

    try:
        discography_with_titles = discography_with_titles[:discography_with_titles.index("== References ==")]
        leader = discography_with_titles[:discography_with_titles.index("=== As sideman ===")][1:]
        sideman = discography_with_titles[discography_with_titles.index("=== As sideman ===")+1:]

        discography = {
            "leader": leader,
            "sideman": sideman
         }
    except ValueError:
        discography = {}

    return discography



class Player:

    def __init__(self, name, instrument, discography, as_sideman):
        self.name = name
        self.instrument = instrument
        self.discography = discography
        self.as_sideman = as_sideman
        self.as_leader = list(set(discography) - set(as_sideman))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def create_players():
    players = []
    for player in extract_players():
        try:
            discography = extract_discography(player["player"])
            leader = discography.get('leader', [])
            sideman = discography.get('sideman', [])
            if leader or sideman:  # added
                players.append(Player(player["player"], player["instrument"], leader + sideman, sideman))
        except wikipedia.exceptions.PageError as e:
            print(f'Page id "{player["player"]}" does not match any pages. Try another id!')
        except IndexError as e: # added
            print(f'Discography not found. Skipping player.')
    return players

def create_graph(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman)
    return graph


def create_graph_with_instruments(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman, instrument=player.instrument)
    return graph


def create_graph_with_instruments_and_albums(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman, instrument=player.instrument, album=album)
    return graph


def create_graph_with_instruments_and_albums_and_year(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman, instrument=player.instrument, album=album, year=album.split("(")[1].split(")")[0])
    return graph


def create_graph_with_instruments_and_albums_and_year_and_label(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman, instrument=player.instrument, album=album, year=album.split("(")[1].split(")")[0], label=album.split("(")[1].split(")")[1].split("[")[0])
    return graph


def create_graph_with_instruments_and_albums_and_year_and_label_and_genre(players):
    graph = nx.Graph()
    for player in players:
        graph.add_node(player)
    for player in players:
        for album in player.as_leader:
            for sideman in player.as_sideman:
                if sideman in album:
                    graph.add_edge(player, sideman, instrument=player.instrument, album=album, year=album.split("(")[1].split(")")[0], label=album.split("(")[1].split(")")[1].split("[")[0], genre=album.split("(")[1].split(")")[1].split("[")[1].split("]")[0])
    return graph

def create_graphs():

    players = create_players()
    graph_1 = create_graph(players)
    graph_2 = create_graph_with_instruments(players)
    graph_3 = create_graph_with_instruments_and_albums(players)
    graph_4 = create_graph_with_instruments_and_albums_and_year(players)
    graph_5 = create_graph_with_instruments_and_albums_and_year_and_label(players)
    graph_6 = create_graph_with_instruments_and_albums_and_year_and_label_and_genre(players)

    graphs = {
        "graph_1": graph_1,
        "graph_2": graph_2,
        "graph_3": graph_3,
        "graph_4": graph_4,
        "graph_5": graph_5,
        "graph_6": graph_6
    }

    return graphs

create_graphs()