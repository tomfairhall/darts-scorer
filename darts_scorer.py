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
            valid_score = False
            while not valid_score:
                print(f"Enter {person.name}'s [{str(person.score - sum(person.score_turn))}] {make_ordinal(x+1)} throw:", end=" ")
                try:
                    person.throw()
                    valid_score = True
                except Exception as err:
                    print(err)
            
            if person.win():
                print(f"{person.name} won!")
                break

            if person.bust():
                person.reset()
                print(f"{person.name} busted!")
                break

        print(f"{person.name} scored: {sum(person.score_turn)}")
        person.reset()

        if person.win():
            break
    else:
        continue
    break

# closing loop
for person in player_list:
    #print(vars(person)) #debug
    print(f"{person.name}'s highest turn: {max(person.turn_list)}")
    print(f"{person.name}'s 3-dart average: {(args.score/len(person.scores_list)) * 3}")