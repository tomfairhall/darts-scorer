# Darts Scorer v0.1.0
#         if throw[0] == "t":
#            score_round += 3*(int(throw.split("t")[1]))
#        elif throw[0] == "d":
 #           score_round += 2*(int(throw.split("d")[1]))
#
# Valid inputs 0 - 20, d1 - d20, t1 - t20, sb, db

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("home", help="Home team name")
parser.add_argument("away", help="Away team name")
parser.add_argument("score", help="Enter starting score")

args = parser.parse_args()

print("Welcome to darts scorer v0.1!")
print(args.home, "v.", args.away)
print("Starting points:", args.score)

def check_busted(score_hit, score_remaining):
    if score_hit - score_remaining < 0:
        print("Busted!")
        return True
    else:
        return False

# how to check if scores are right... regrex?
def check_score(throws):
    score_round = 0

    for throw in throws:
        if throw[0] == "t":
            continue
        elif throw[0] == "d":
            continue
        elif throw == "sb":
            continue
        elif throw == "db":
            continue
        elif int(throw) >= 0 or int(throw) <= 20:
            continue
        else:
            print("Please input valid scores!")
            return False

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def turn(self):
        throws = input("Enter " + self.name + "'s throws:").split()

        if len(throws) > 3 or len(throws) < 3:
            print("Enter only 3 throws!")
        else:
            check_score()
            check_busted()

            
        print(self.name + "'s", "score:", self.score)

home = Player(args.home, int(args.score))
away = Player(args.away, int(args.score))

while True:
    home.turn()
    away.turn()






