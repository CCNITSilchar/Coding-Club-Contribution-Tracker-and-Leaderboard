import math

class contribution_calculator:

    # Input container for coding contest score calculator
    score = []                           # Stores the input ranks of all contestants in a contest
    normalized_score = []                # Stores the normalized rank of all contestants for a contest
    mean = 0                             # To store mean rank
    standard_deviation = 0               # To store standard deviation of ranks
    no_of_participants = 0               # No of participants in a contest

    # Output score container for all platforms.
    contribution_score = []

    # Github contribution calculator. Fits the curve with offset of 1 every 50 stars. Curve: 20*(stars - 49)^(1/5) + floor((stars-1)/50) 
    def github_contribution_score(self):
        for stars in self.score:
            if stars >= 50:
                self.contribution_score.append( 20* math.pow(stars - 49 ,1/5) + (stars-1)//50 )
            else:
                self.contribution_score.append( 0.0 )

    # Calculates mean of input score and updates mean(class variable)
    def get_mean(self):
        total_score = 0
        for individual_score in self.score:
            total_score = total_score + individual_score
        self.mean = total_score/self.no_of_participants

    # Calculates standard deviation of input score and updates standard_deviation(class variable)
    def get_standard_deviation(self):
        total_score_squared = 0
        for individual_score in self.score:
            total_score_squared = total_score_squared + individual_score**2
        variance = total_score_squared/self.no_of_participants - (self.mean**2)
        self.standard_deviation = math.sqrt(variance)

    # Fits normalized distribution curve for the input score.
    def get_normalized_score(self):
        self.get_mean()
        self.get_standard_deviation()

        # To prevent the condition when all participants have same score and hence division by zero error.
        if(self.standard_deviation < 0.75):
            self.standard_deviation = 0.75

        for participant in range(self.no_of_participants):
            # As lower ranks should have higher values hence all normalized values are multiplied by -1.
            self.normalized_score.append((-1 * (self.score[participant] - self.mean))/self.standard_deviation)

    # Calculates contribution score for contests.      
    def contest_contribution_score(self):
        
        self.get_normalized_score()
        # Standardised_score calculates the score based on exponential distribution done on normalized score.
        standardised_score = list(self.normalized_score)
        for participant in range( self.no_of_participants ):
            standardised_score[participant] = 1.1**self.normalized_score[participant] + self.normalized_score[participant]

        #To set minimum score as 0.25 and maximum score as 1
        min_score = 0.25 - min(self.normalized_score)
        for participant in range( self.no_of_participants ):
            standardised_score[participant] = standardised_score[participant] + min_score
        max_score = max(standardised_score)
        for participant in range( self.no_of_participants ):
            standardised_score[participant] = standardised_score[participant] / max_score

        # To provide bonus score to top ranks.
        for participant in range(self.no_of_participants):
            standardised_score[participant] = ( standardised_score[participant] + 10/math.sqrt(self.score[participant]))

        self.contribution_score = list(standardised_score)
        
    def get_contribution_score(self):
        return self.contribution_score

    # Intializer for score calculator. Requires platofrm(string) and  score(list) input. It initializes with input values and performs calculations.
    def __init__(self, platform, score=[]): 
        #To update class variables with input values
        self.score = list(score)
        self.no_of_participants = len(score)

        #if scoring is required for github, then platform should be set as "github".
        if(platform == "github"):
            #calculates the contribution score on the basis of stars in score input.
            self.github_contribution_score()

        #score calculator for coding platforms. Initializes the class variables with input values and performs calculations.
        if(platform != "github"):
            self.contest_contribution_score()