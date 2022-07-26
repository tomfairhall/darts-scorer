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
        self.name = name        #Player's name
        self.score = score      #Player's current score
        self.score_turn = []    #Player's current turn scores
        self.turn_list = []     #Player's list of turn scores
        self.scores_list = []   #Player's list of scores

    def bust(self):
        busted = self.score - sum(self.score_turn) < 0
        if busted:
            self.score_turn.clear()
        return busted

    def win(self):
        return self.score - sum(self.score_turn) == 0

    def reset(self):
        self.score -= sum(self.score_turn)
        self.turn_list.append(sum(self.score_turn))
        self.score_turn.clear()

    def throw(self):
        score = input().lower()   
        try:
            self.score_turn.append(valid_scores[score])
            self.scores_list.append(valid_scores[score])
        except:
            raise ValueError(f"'{score}': is not valid!")