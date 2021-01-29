print()
import math
import rating # The object of class similarity

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
    
        Min_Dist = 0
        
        if (r < 0):
            print('Error! r should be greater than 0 !!')
            return -87
    
        else:               
            for k in self.ratings1.keys() & self.ratings2.keys():
                Min_Dist += math.pow(math.fabs(self.ratings1[k] - self.ratings2[k]), r)
            Min_Dist = math.pow(Min_Dist, 1/r)
        
        return round(Min_Dist, 4)

    # Pearson Correlation between two vectors
    def pearson(self):
        
        sumPQ = 0 #summation of P * Q
        sumP = 0 #summation of P
        sumQ = 0 #summation of Q
        sumP2 = 0 #summation of P square
        sumQ2 = 0 #summation of Q square
        n = len(self.ratings1.keys() & self.ratings2.keys()) # sample size
        
        for i in (self.ratings1.keys() & self.ratings2.keys()):
            sumP += self.ratings1[i]
            sumQ += self.ratings2[i]
            sumP2 += math.pow(self.ratings1[i], 2)
            sumQ2 += math.pow(self.ratings2[i], 2)
            sumPQ += self.ratings1[i] * self.ratings2[i]
        
        Pearson_nm = (sumPQ - (sumP * sumQ / n))
        Pearson_dm = (math.sqrt(sumP2 - (math.pow(sumP, 2) / n)) * math.sqrt(sumQ2 - (math.pow(sumQ, 2) / n)))
        Pearson_Corr = round((Pearson_nm/ Pearson_dm), 4)
        
        return round(Pearson_Corr, 4)

# user ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

# Caculations
UserRating = rating.similarity(UserPRatings, UserQRatings)

Manhattan_Dist = UserRating.minkowski(1)
print('Manhattan_Distance = ', Manhattan_Dist)

Euclidean_Dist = UserRating.minkowski(2)
print('Euclidean Distance = ', Euclidean_Dist)

Minkowski_Dist = UserRating.minkowski(3)
print('Minkowski Distance = ', Minkowski_Dist)

Pearson = UserRating.pearson()
print('Pearson Correlation = ', Pearson)
print()
