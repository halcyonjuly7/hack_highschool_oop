import sys

from game import Game

if __name__ == "__main__":
    if len(sys.argv) == 2:
        game = Game(sys.argv[1])
        game.run()
