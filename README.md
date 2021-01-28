# Python_Practice

## User defined function
This practice is talking about how to write a user-defined function. Here I build a Pearson correlation function for practing because Pearson correlation is a basic calculation for user-based recommendation system.

Define a function called pearsonD. 
* The function takes two dictionary parameters and return the Pearson Correlation
* Using a single for loop to calculate the Pearson Correlation
* The Pearson Correlation calculation considers an item only if it was rated by both users


## User defined class
This practice is talking about how to write a user-defined class. Since I've built a user-defined function to calculate Pearson correlation, I can go into next step to build a user-difined class to contain more functions that will be needed in the following steps.

Define a class called similarity.
* Code up the Class method called minkowski which takes a single parameter r, and returns the Minkowki Distance between the two dictionaries
* Code up the Class method called pearson which takes no parameters, and returns the Pearson Correlation between the two dictionaries
* Create an object of class similarity. Initialize it with rating dictionaries UserPRatings and UserQRatings. Call the minkowski and pearson class methods to calculate the measures between the two dictionaries


## Social Network Analysis
This practice is going to use Amazon Product Co-purchase data to make Book Recommendations using Social Network Analysis.
* Get the books that have been co-purchased with the purchasedAsin in the past
* Filter down to the most similar books
* Get the books that are still connected to the purchasedAsin by one hop (called the neighbors of the purchasedAsin) after the above clean-up, and assign the resulting list to purchasedAsinNeighbors
* Come up with a **composite measure** to make the Top Five book recommendations based on one or more of the following metrics associated with neighbors in purchasedAsinNeighbors
* Print Top 5 recommendations based on your composite measure
