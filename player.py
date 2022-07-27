class Player():
    #TODO: set staring score
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __check_number(self, number):
        try:
            value = int(number)
            return value >= 0 or value <= 20
        except:
            raise ValueError("'" + number + "'" ": value wrong")
    
    def __check_busted(self, score_turn, score_remaining):
        return(score_remaining - score_turn < 0)

    def __value_throw(self, throw):
        if len(throw) <= 2:
            if throw == "sb":
                return 25
            elif throw == "db":
                return 50 
            elif self.__check_number(throw):
                return int(throw)
        elif len(throw) == 3:
            throw_modifier = throw[0]
            throw_value = throw[1] + throw [2]
            if int(throw_value) <= 20:
                if throw_modifier == "d":
                    return 2*int(throw_value)
                elif throw_modifier == "t":
                    return 3*int(throw_value)
                else:
                    raise ValueError("'" + throw + "'" + ": modifier wrong")
            else:
                raise ValueError("'" + throw + "'" + ": number wrong")
        else:
            raise ValueError("'" + throw + "'" + ": value wrong")

    def __check_won(self):
        return self.score == 0

    def won(self):
        return self.__check_won()

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
                    score_turn += self.__value_throw(throw)
                except ValueError as error:
                    print(error)
                    self.turn()

            if self.__check_busted(score_turn, self.score):
                print(self.name, "is busted!")
            else:
                self.score -= score_turn
                print(self.name, "scored:", score_turn)

                if self.__check_won():
                    print(self.name, "won!")
                else:
                    print(self.name, "has", self.score, "to go")