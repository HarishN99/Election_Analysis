# The data we need to retrieve
# 1. The total number of votes
# 2. A complete list of candidates who reveived votes
# 3. The percentage of votes each candidate won.
# 4. THe total number of votes each candidate won. 
# 5. THe winner of the lection based on popular vote

# Link file Resources/election_results.csv

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)