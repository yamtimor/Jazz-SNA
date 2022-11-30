class Player:

    def __init__(self, name, instrument, discography, sideman):
        self.name = name
        self.instrument = instrument
        self.discography = discography
        self.sideman = sideman

    # temporary:
    def __str__(self):
        return f"info about {self.name}"
