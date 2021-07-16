
class PlayerInputs:
    def __init__(self, p2_input):
        self.p2_input = p2_input

    def getPlayer1Input(self):
        p1_input = input('Player 1 please enter your chosen word: ')
        return p1_input

    def player2Letters(self):
        letters = []
        letters.append(self.p2_input)


    def getPlayer2Input(self):
        self.p2Input = input('P2 please guess a letter: ')
        return self.p2Input


class CheckWord(PlayerInputs):
    def __init__(self):