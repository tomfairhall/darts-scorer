import statistics

valid_scores = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "11" : 11,
    "12" : 12,
    "13" : 13,
    "14" : 14,
    "15" : 15,
    "16" : 16,
    "17" : 17,
    "18" : 18,
    "19" : 19,
    "20" : 20,
    "d1" : 2,
    "d2" : 4,
    "d3" : 6,
    "d4" : 8,
    "d5" : 10,
    "d6" : 12,
    "d7" : 14,
    "d8" : 16,
    "d9" : 18,
    "d10" : 20,
    "d11" : 22,
    "d12" : 24,
    "d13" : 26,
    "d14" : 28,
    "d15" : 30,
    "d16" : 32,
    "d17" : 34,
    "d18" : 36,
    "d19" : 38,
    "d20" : 40,
    "t1" : 3,
    "t2" : 6,
    "t3" : 9,
    "t4" : 12,
    "t5" : 15,
    "t6" : 18,
    "t7" : 21,
    "t8" : 24,
    "t9" : 27,
    "t10" : 30,
    "t11" : 33,
    "t12" : 36,
    "t13" : 39,
    "t14" : 42,
    "t15" : 45,
    "t16" : 48,
    "t17" : 51,
    "t18" : 54,
    "t19" : 57,
    "t20" : 60,
    "sb" : 25,
    "db" : 50
}

class Player():      
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.score_list = []
    
    def __check_busted(self, score_turn, score_remaining):
        return(score_remaining - score_turn < 0)

    def __check_won(self):
        return self.score == 0

    def __check_score(self, score):
        return score in valid_scores

    def statistics(self):
        print(self.name + "'s:", end=" ")
        print("average score:", statistics.mean(self.score_list))

    def won(self):
        return self.__check_won()

    def turn(self):
        incorrect_input = True # assume input is incorrect until proven correct
        scores = []

        while incorrect_input:  
            # player inputs scores
            print("Enter", self.name + "'s", "scores", "[" + str(self.score) + "]:", end=" ")
            scores = input().split()
            if len(scores) == 3:
                incorrect_input = False
                for score in scores:
                    if self.__check_score(score):
                        continue
                    else:
                        print(score + ": not a valid score!")
                        incorrect_input = True
            else:
                print("Enter 3 scores only!")

        # check each score
        score_turn = 0
        for score in scores:
            # save score
            self.score_list.append(valid_scores[score])
            # add score to turn score total
            score_turn += valid_scores[score]

        if self.__check_busted(score_turn, self.score):
            print(self.name, "busted!")
        else:
            self.score -= score_turn
            print(self.name, "scored", score_turn, end=" ")

            if self.__check_won():
                print(self.name, "won!")
            else:
                print(self.name, "has", self.score, "remaining")