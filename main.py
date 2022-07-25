# Darts Scorer v0.1.0
# 
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

def busted(score_hit, score_remaining):
    if 

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def turn(self):
        throws = input("Enter " + self.name + "'s throws:").split()

        if len(throws) > 3 or len(throws) < 3:
            print("Enter only 3 throws!")
        else:
            for throw in throws:
                if throw[0] == "t":
                    self.score -= 3*(int(throw.split("t")[1]))
                elif throw[0] == "d":
                    self.score -= 2*(int(throw.split("d")[1]))
                elif throw == "sb":
                    self.score -= 25
                elif throw == "db":
                    self.score -= 50
                elif int(throw) >= 0 or int(throw) <= 20:
                    self.score -= int(throw)
                else:
                    print("Please input valid scores!")
        print(self.name + "'s", "score:", self.score)

home = Player(args.home, int(args.score))
away = Player(args.away, int(args.score))

while True:
    home.turn()
    away.turn()






