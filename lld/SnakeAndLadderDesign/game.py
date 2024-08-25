from models import Player, Jumper

class Game:
    def __init__(self):
        self.board = [i for i in range(101)]
        self.players = []
        self.jumpers = []

    def addPlayer(self, player: Player):
        self.players.append(player)

    def addJumper(self, jumper: Jumper):
        self.board[jumper.start] = jumper.end
