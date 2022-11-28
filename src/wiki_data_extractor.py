import wikipedia
from pprint import pprint

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

class Player:


    def __init__(self, name, instrument, discography, sideman):
        self.name = name
        self.instrument = instrument
        self.discography = discography
        self.sideman = sideman

    # temporary:
    def __str__(self):
        return f"info about {self.name}"

if __name__ == "__main__":
    player_test = Player('John Coltrane', 'Saxophone', [1,2,3], [4,5])
    print(player_test)
