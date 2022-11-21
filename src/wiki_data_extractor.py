import wikipedia
import pandas

# list of bebop jazz players
bebop_players = wikipedia.page("List of bebop musicians").content


class WikiDataExtractor:
    def __init__(self, names):
        self.players = []

    def get_players(self):
        for element in filter(lambda x: bool(x) and not x.startswith("=="), bebop_players.split('\n')):
            self.players.append(element.split('-')[0][:-1])

# if __name__ == "__main__":

