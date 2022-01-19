# Election_Analysis

## Project Overview

This analysis was intended to expand the original Colorado election audit to provide information on voter turnout for each country, the percentage of votes from each county out of the total count, and the name of the county with the highest turnout. 

Goals of Project:

1. Calculate the total number of votes cast. 
2. Get a compelte list of candidates who recieved votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources Used:

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.2

## Election-Audit Results

![ElectionSummary](https://user-images.githubusercontent.com/94864663/150219753-681db942-4487-4c6e-8125-5b9d6940d396.png)


-	A total of 369,711 votes were cast in this congressional election.

### Votes by County

-	Denver country received 82.8% of the vote with 306,055 votes.
-	Jefferson country received 10% of the vote with 38,855 votes.
-	Arapahoe country received 6.7% of the vote with 24,801 votes. 

### County with the Largest Number of Votes

-	**Denver county** with 306,055 votes had the largest number of votes, attributing to nearly 83% of the total votes in this congressional election. 

### Votes by Candidate

-	Diana DeGette received 73.8% of the vote with 272,892 votes.
-	Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
-	Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.

### Election Winner

-   Overall, **Diana DeGette** won the election with 272,892 votes attributing to nearly 74% of all the votes in this congressional election. 

## Challenge Summary

As exhibited above, the script is very useful in extracting pertinent information from a large dataset. The script is also very amiable, in the future, it can be modified to fit a nationwide election, replacing counties with states. This would deal with a much larger dataset but the concept of collecting information on the total number of votes, list of candidates, votes for each candidate, percentage of votes for each candidate and the winner of the popular vote. 

The dataset used in this project collected data on the ballot ID, county name and the preferred candidate from each voter. If the dataset were to collect more data from the voter such as demographic information, the script can easily be refactored to represent this data as well. The election commission can then use this script to discover and represent any trends for voting preference based on age, gender, race, income, employment, education, etc. Specifically, this can be done by extracting these parameters within the for loop and specifying which information to collect with the if statements. 


