# Add dependencies
import csv
import os

# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to an output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create variable for accumulator
total_votes = 0
# Create list for candidates
candidate_options = []
# Create dictionary for candidate vote counts
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Create a list for counties
counties_voted = []
# Create a dictionary for county vote counts
county_votes = {}
# Highest candidate and highest count tracker
highest_county = ""
highest_count = 0
highest_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        
        #Print the county name from each row
        county_name = row[1]
        # If the county name does not match any existing county...
        if county_name not in counties_voted:

            # Add it to the list of counties
            counties_voted.append(county_name)

            # Begin tracking county vote count
            county_votes[county_name] = 0

        #Add a vote to the county's count
        county_votes[county_name] += 1

    # Save results to a text file
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count of candidate
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            # Save the candidate results to the text file
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)
        
        # Determine the percentage of votes for each county
        # Iterate through the county list
        for county_name in county_votes:
            # Retrieve vote count of county
            voters = county_votes[county_name]
            # Calculate the percentage of votes
            voter_percentage = float(voters) / float(total_votes) * 100
            # Print the county name and percentage of votes
            county_results = (f"{county_name} county: {voter_percentage:.1f}% ({voters:,})\n")
            print(county_results)
            # Save the county results to the text file
            txt_file.write(county_results)

            # Determine county with highest turnout
            # Determine if the voters are greater than the highest count
            if (voters > highest_count) and (voter_percentage > highest_percentage):
                # If true then set highest_count = voters and highest_percent = voter_percentage
                highest_count = voters
                highest_percentage = voter_percentage
                # Set the winning_county equal to the county's name
                winning_county = county_name

        winning_county_summary = (
            f"---------------------------\n"
            f"Highest Voter Turnout: {winning_county}\n"
            f"Voter Count: {highest_count:,}\n"
            f"Voter Percentage: {highest_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_county_summary)
        # Save the winning county's name to the text file
        txt_file.write(winning_county_summary)
