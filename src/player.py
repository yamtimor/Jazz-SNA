import wikipedia
from pprint import pprint

class Player:

    def __init__(self, name, instrument, discography, as_sideman):
        self.name = name
        self.instrument = instrument
        self.discography = discography
        self.as_sideman = as_sideman

    def __str__(self):
        return f"info about {self.name}, a {self.instrument} player"
