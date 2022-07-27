# Darts Scorer v0.1.0

import argparse
import player

parser = argparse.ArgumentParser()

parser.add_argument("home", help="Home team name")
parser.add_argument("away", help="Away team name")
parser.add_argument("score", help="Enter starting score")

args = parser.parse_args()

# game setup
print("Welcome to darts scorer v0.1!")
print(args.home, "v.", args.away)
print("Starting points:", args.score)

#TODO: Variable amount of players
home = player.Player(args.home, int(args.score))
away = player.Player(args.away, int(args.score))
player_list = [home, away]

# game loop
while True:
    for player in player_list:
        player.turn()
        if player.won():
            break
    else:
        continue
    break