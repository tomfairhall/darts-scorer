# Darts Scorer v0.1.0

import curses
from curses import wrapper
import argparse
import player

parser = argparse.ArgumentParser()
parser.add_argument("players", help="Enter player name(s)", action="store", nargs="+")
parser.add_argument("score", help="Enter starting score", type=int)
args = parser.parse_args()

print("Welcome to darts scorer v0.1!")
print("Starting points:", args.score)

player_list = []
for player_name in args.players:
    player_x = player.Player(player_name, args.score)
    player_list.append(player_x)

# game loop
while True:
    for player in player_list:
        player.turn()
        if player.won():
            break
    else:
        continue
    break