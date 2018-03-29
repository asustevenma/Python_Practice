print()
import math

# Define Pearson Correlation function
def pearsonD(userratings1, userratings2):
    sumPQ = 0 #summation of P * Q
    sumP = 0 #summation of P
    sumQ = 0 #summation of Q
    sumP2 = 0 #summation of P square
    sumQ2 = 0 #summation of Q square
    n = len(userratings1.keys() & userratings2.keys()) # sample size
    
    for i in (userratings1.keys() & userratings2.keys()):
        sumP += userratings1[i]
        sumQ += userratings2[i]
        sumP2 += math.pow(userratings1[i], 2)
        sumQ2 += math.pow(userratings2[i], 2)
        sumPQ += userratings1[i] * userratings2[i]

    Pearson_nm = (sumPQ - (sumP * sumQ / n))
    Pearson_dm = (math.sqrt(sumP2 - (math.pow(sumP, 2) / n)) * math.sqrt(sumQ2 - (math.pow(sumQ, 2) / n)))
    PearsonD = round((Pearson_nm/ Pearson_dm), 4)
    return PearsonD

# Given 2 rating dictionaries
UserPRatings = {'Apple':1, 'Samsung':5, 'Nokia':7, 'Motorola':8, 'LG':5, 'Sony':1, 'Blackberry':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

# Call the function and print out
Pearson_Value = pearsonD(UserPRatings, UserQRatings)
print('Pearson correlation value is', Pearson_Value)
print()
# End
