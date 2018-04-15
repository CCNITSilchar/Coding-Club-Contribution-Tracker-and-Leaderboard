import math

class contribution_calculator_contest:
    score = []
    normalized_score = []
    contribution_score = []
    points_per_question = 0.2
    mean = 0
    standard_deviation = 0
    no_of_participants = 0

    codeforces = 0.25
    codechef = 0.15
    hackerearth = 0.2

    def __init__(self, score=[], value_per_question = 0.25, site=""):
        self.score = list(score)
        self.no_of_participants = len(score)
        self.points_per_question = value_per_question

        if(site == "codeforces"):
            self.points_per_question = self.codeforces
        if(site == "hackerearth"):
            self.points_per_question = self.hackerearth
        if(site == "codechef"):
            self.points_per_question = self.codechef

    def get_mean(self):
        total_score = 0
        for individual_score in self.score:
            total_score += individual_score
        self.mean = total_score/self.no_of_participants

    def get_standard_deviation(self):
        total_score_squared = 0
        for individual_score in self.score:
            total_score_squared = total_score_squared + individual_score**2
        variance = total_score_squared/self.no_of_participants - self.no_of_participants*(self.mean**2)
        self.standard_deviation = math.sqrt(variance)

    def get_normalized_score(self):
        self.get_mean()
        self.get_standard_deviation()

        if(self.standard_deviation < 0.75):
            self.standard_deviation = 0.75

        self.normalized_score = list(self.score);
        for participant in range(self.no_of_participants):
            self.normalized_score[participant] = (self.score[participant] - self.mean)/self.standard_deviation
            
    def get_contribution_score(self):
        if(self.no_of_participants == 0):
            return []

        self.get_normalized_score()
        standardised_score = list(self.normalized_score)
        minimum = 0.33 - min(standardised_score)
        for participant in range(self.no_of_participants):
            standardised_score[participant] = (standardised_score[participant] + minimum)*0.75
            
        contribution_score = standardised_score
        for participant in range(self.no_of_participants):
            contribution_score[participant] = standardised_score[participant] + self.points_per_question * self.score[participant]
            
        return contribution_score

