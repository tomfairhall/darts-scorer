# Darts Scorer v0.1.0
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

def check_number(number):
    try:
        int(number)
        return True
    except:
        return False

def check_busted(score_turn, score_remaining):
    return(score_remaining - score_turn < 0)

def check_score_turn(throws):
    score_turn = 0

    for throw in throws:   
        if len(throw) <= 2:
            if check_number(throw):
                score_throw = int(throw)
                if score_throw <= 20:
                    score_turn += score_throw
        elif len(throw) == 3:
            if throw == "sb":
                score_turn += 25
            elif throw == "db":
                score_turn += 50
            else:
                score_throw = throw[1] + throw[2]
                if check_number(score_throw):
                    if throw[0] == "d":
                        score_turn += int(score_throw)*2
                    elif throw[1] == "t":
                        score_turn += int(score_throw)*3
        else:
            print("Please enter valid input!")
            score_turn = 0   
    
    return score_turn
    

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def turn(self):
        throws = input("Enter " + self.name + "'s throws:").split()

        if len(throws) > 3 or len(throws) < 3:
            print("Enter only 3 throws!")
            self.turn()
        else:
            score_turn = check_score_turn(throws)
            if check_busted(score_turn, self.score):
                print(self.name, "is busted!")
            else:
                self.score -= score_turn

        print(self.name, "scored:", score_turn)
        print(self.name, "has", self.score, "to go")

home = Player(args.home, int(args.score))
away = Player(args.away, int(args.score))

player_list = [home, away]

while True:
    for player in player_list:
        player.turn()
        if player.score == 0:
            print(player.name, "won!")
            break
    else:
        continue
    break