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

def check_busted(score_turn, score_remaining):
    return(score_remaining - score_turn < 0)

def check_number(number):
    try:
        return int(number)
    except:
        return False

def value_throw(throw):

    if len(throw) <= 2 and check_number(throw) and int(throw) <= 20:
        return int(throw)
    elif len(throw) == 3:
        if throw == "sb":
            return 25
        elif throw == "db":
            return 50
        else:
            throw_modifier = throw[0]
            throw_value = throw[1] + throw [2]
            if check_number(throw_value) and int(throw_value) <= 20:
                if throw_modifier == "d":
                    return 2*int(throw_value)
                elif throw_modifier == "t":
                    return 3*int(throw_value)
                else:
                    raise ValueError("'" + throw + "'" + ": modifier wrong")
            else:
                raise ValueError("'" + throw + "'" + ": number wrong")
    raise ValueError("'" + throw + "'" + ": value wrong")

class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def turn(self):
        # player inputs throws
        throws = input("Enter " + self.name + "'s throws:").split()

        # check if only three throws
        if len(throws) > 3 or len(throws) < 3:
            print("Enter only 3 throws!")
            self.turn()
        else:
            # check each score
            score_turn = 0
            for throw in throws:
                try:
                    score_turn += value_throw(throw)
                except ValueError as error:
                    print(error)
                    self.turn()

            if check_busted(score_turn, self.score):
                print(self.name, "is busted!")
            else:
                self.score -= score_turn

        print(self.name, "scored:", score_turn)
        print(self.name, "has", self.score, "to go")

home = Player(args.home, int(args.score))
away = Player(args.away, int(args.score))

player_list = [home, away]

# game loop
while True:
    for player in player_list:
        player.turn()
        if player.score == 0:
            print(player.name, "won!")
            break
    else:
        continue
    break