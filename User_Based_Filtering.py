import math
from operator import itemgetter
#################################################
# recommender class does user-based filtering and recommends items 
class UserBasedFilteringRecommender:
    
    # class variables:    
    # none
    
    ##################################
    # class instantiation method - initializes instance variables
    #
    # usersItemRatings:
    # users item ratings data is in the form of a nested dictionary
    #
    # k:
    # the number of nearest neighbors
    # defaults to 1
    #
    # m:
    # the number of recommedations to return
    # defaults to 10
    #
    def __init__(self, usersItemRatings, metric='pearson', k=1, m=10):
        
        # set self.usersItemRatings
        self.usersItemRatings = usersItemRatings
            
        # set self.k
        if k > 0:   
            self.k = k
        else:
            print ("    (FYI - invalid value of k (must be > 0) - defaulting to 1)")
            self.k = 1
         
        # set self.m
        if m > 0:   
            self.m = m
        else:
            print ("    (FYI - invalid value of m (must be > 0) - defaulting to 10)")
            self.m = 10
            

    def pearsonFn(self, userXItemRatings, userYItemRatings):
        
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        
        n = len(userXItemRatings.keys() & userYItemRatings.keys())
        
        for item in userXItemRatings.keys() & userYItemRatings.keys():
            x = userXItemRatings[item]
            y = userYItemRatings[item]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
       
        if n == 0:
            print ("    (FYI - personFn n==0; returning -2)")
            return -2
        
        denominator = math.sqrt(sum_x2 - pow(sum_x, 2) / n) * math.sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            print ("    (FYI - personFn denominator==0; returning -2)")
            return -2
        else:
            return round((sum_xy - (sum_x * sum_y) / n) / denominator, 2)
            

    #################################################
    # make recommendations for userX from the most similar k nearest neigibors (NNs)
    def recommendKNN(self, userX):
        
        PC_Ratings = {}
        for userY in self.usersItemRatings.keys():
            if (userX != userY):     
                PC = self.pearsonFn(self.usersItemRatings[userX], self.usersItemRatings[userY])
                PC_Adj = round((PC + 1) / 2, 4)
                PC_Ratings[userY] = PC_Adj
        # print("PC_Ratings :", PC_Ratings)
        
        # For given userX, get the sorted list of users - by most similar to least similar        
        PC_Rating_Sorted = sorted(PC_Ratings.items(), key=itemgetter(1), reverse=True)
        # print("PC_Rating_Sorted :", PC_Rating_Sorted)

        # Calcualte the weighted average item recommendations for userX from userX's k NNs
        Weight_dn = 0
        for w in range(self.k):
            Weight_dn += PC_Rating_Sorted[w][1]
            
        Weight_List = {} # Build a dictionary to store the weighted scores for each user
        for l in range(self.k):
            Weight_List[PC_Rating_Sorted[l][0]] = round(PC_Rating_Sorted[l][1] / Weight_dn, 4)
        # print("Weight_List :", Weight_List)
    
        # Return list of all recommendations 
        Recommend_List = {}
        for name in self.usersItemRatings.keys() & Weight_List.keys():
            for band in self.usersItemRatings[name].keys():
                if band not in Recommend_List:
                    # if band not in self.usersItemRatings[name].keys():
                    Recommend_List[band] = round(Weight_List[name] * self.usersItemRatings[name][band], 2)
                else:
                    Recommend_List[band] = round(Recommend_List[band] + Weight_List[name] * self.usersItemRatings[name][band], 2)
                    
        # Return Final Recommend_List(sorted highest to lowest ratings) based on number of m
        Recommend_List_Final = {}
        for band1 in Recommend_List.keys():
            if band1 not in self.usersItemRatings[userX]:
                Recommend_List_Final[band1] = Recommend_List[band1]
        return sorted(Recommend_List_Final.items(), key=itemgetter(1), reverse=True)[:self.m]
        print()
