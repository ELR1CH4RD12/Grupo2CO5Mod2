class ScoreManager:
    def __init__(self):
        self.death_count = 0
        self.score = 0
        self.highest_score_list = []
        self.highest_score = 0

    def deathCount(self):
        self.death_count += 1

    def update_score(self):
        self.score += 1
        return self.score
    def scorelist(self, score):
        self.highest_score_list.append(score)

    def highscore(self):
        if len(self.highest_score_list) > 1:
            self.highest_score = max(self.highest_score_list)
        else:
            self.highest_score = self.score
        return self.highest_score