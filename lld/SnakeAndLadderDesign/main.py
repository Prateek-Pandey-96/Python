from game import Game
from models import Player, Jumper
from utils import throwDice
from collections import deque

def init() -> Game:
    game = Game()

    # add two players
    game.addPlayer(Player("Player1"))
    game.addPlayer(Player("Player2"))
    
    # add snakes
    game.addJumper(Jumper(61, 18))
    game.addJumper(Jumper(63, 59))
    game.addJumper(Jumper(16, 6))

    # add ladders
    game.addJumper(Jumper(8, 30))
    game.addJumper(Jumper(55, 65))
    game.addJumper(Jumper(78, 94))
    
    return game

# we will assume the player wins if he crosses 99 position
def playAndGetWinner(game: Game) -> Player:
    queue = deque()

    for player in game.players:
        queue.append((player, 1))
    
    winner = Player(name="not decided yet")
    while True:
        curr, pos = queue.popleft()
        num = throwDice()
        new_pos = pos + num
        if new_pos >= 100:
            winner = curr
            break
        
        if game.board[new_pos]!=new_pos:
            new_pos = game.board[new_pos]
        
        print(f"{curr.name} moved from {pos} to {new_pos}")
        queue.append((curr, new_pos))

    return winner
        

if __name__ == "__main__":
    print("Starting the game")
    
    # initialize Game
    game: Game = init()
    print(game)
    winner: Player = playAndGetWinner(game)

    print(f"winner is: {winner.name}")

    exit()
    

