# Darts Scorer v0.1.0
import argparse
import player

parser = argparse.ArgumentParser()
parser.add_argument("players", help="Enter player name(s)", action="store", nargs="+")
parser.add_argument("score", help="Enter starting score", type=int)
args = parser.parse_args()

# hacky way to force list type
player_list = [player.Player(args.players[0], args.score)]
for name in args.players[1:]:
    player_list.append(player.Player(name, args.score))

print("Darts Scorer - Starting Score:", args.score)

# game loop
while True:
    for person in player_list:
        person.turn()
        if person.won():
            break
    else:
        continue
    break

# closing loop
for person in player_list:
    person.statistics()