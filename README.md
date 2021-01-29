# Python_Practice

## User defined function
This practice is writing a user-defined function. Here a Pearson correlation function is defined. Pearson correlation is a basic calculation for user-based recommendation system.

Define a function called pearsonD. 
* The function takes two dictionary parameters and return the Pearson Correlation
* Using a single for loop to calculate the Pearson Correlation
* The Pearson Correlation calculation considers an item only if it was rated by both users


## User defined class
This practice is writing a user-defined class. Since a user-defined function is built above to calculate Pearson correlation, we can build a user-difined class to contain more functions that will be needed in the further process.

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


## San Francisco Giants Analytics
A hitting coach is concerned that one of his hitters chases too much. He asks for information that will help him and the hitter work on the problem. Data is provided from TrackMan. Please create any information or visuals that you would give to the coach.

## Wargaming
Wargaming provides a data set which contains gamers' data such as win percentage, spend amount, package sold, play time to answer	what makes players spend money and what makes players buy package.

## Polynomial Regression
Given a certain product's unit price and unit sold, find the optimal unit price which maximize the revenue
