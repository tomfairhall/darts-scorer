# Darts Scorer v0.1.0
import argparse
import player

parser = argparse.ArgumentParser()
parser.add_argument("players", help="Enter player name(s)", action="store", nargs="+")
parser.add_argument("score", help="Enter starting score", type=int)
args = parser.parse_args()

def make_ordinal(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

# hacky way to force list type
player_list = [player.Player(args.players[0], args.score)]
for name in args.players[1:]:
    player_list.append(player.Player(name, args.score))

print("Darts Scorer - Starting Score:", args.score)

# game loop
while True:
    for person in player_list:

        for x in range(3):
            print("Enter " + person.name + "'s [" + str(person.score - sum(person.score_turn)) + "] " + make_ordinal(x+1) + " throw:", end=" ")
            person.throw()
            if person.won():
                print(person.name + " won!")
                break
            elif person.busted():
                print(person.name + " busted!")
                break

        person.score_list.extend(person.score_turn)
        print(person.name + " scored: " + str(sum(person.score_turn)))
        person.score_turn.clear()

        #if person.won:
         #   break
    else: 
        continue
    break

# closing loop
for person in player_list:
    person.statistics()