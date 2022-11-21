import wikipedia
import pandas

# list of bebop jazz players
bebop_players = wikipedia.page("List of bebop musicians").content
print(bebop_players)

class Player:
    def __init__(self, name):
        self.name = name

    def request_name(self):
        pass

if __name__ == "__main__":
    for element in bebop_players.split('\n'):
        if element
        print(element)
