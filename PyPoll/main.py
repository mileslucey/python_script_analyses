# imports
import os
import csv
# establishing paths
csv_path = os.path.join('election_data.csv')
output_path = os.path.join("output.txt")
# establishing variables to help with organization
total_votes = 0
khan_votes = 0
khan_percentage = 0
correy_votes = 0
correy_percentage = 0
li_votes = 0
li_percentage = 0
otooley_votes = 0
otooley_percentage = 0
winning_votes = 0
winner = 0
# csv reader
with open(csv_path,newline = '') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter = ',')
	next(csv_reader,None)
# loop to count total votes and # of votes for each candidate
	for row in csv_reader:
		total_votes += 1
		if row[2] == "Khan":
			khan_votes +=1
		elif row[2] == "Correy":
			correy_votes +=1
		elif row[2] == "Li":
			li_votes +=1
		elif row[2] == "O'Tooley":
			otooley_votes +=1
		else:
			pass
# calculate percentages
	khan_percentage = round((khan_votes/total_votes) * 100,3)
	correy_percentage = round((correy_votes/total_votes) * 100,3)
	li_percentage = round((li_votes/total_votes) * 100,3)
	otooley_percentage = round((otooley_votes/total_votes) * 100,3)
# loop to find the winner
	if khan_votes > winning_votes:
		winning_votes = khan_votes
		winner = "Khan"
	elif correy_votes > winning_votes:
		winning_votes = correy_votes
		winner = "Correy"
	elif li_votes > winning_votes:
		winning_votes = li_votes
		winner = "Li"
	elif otooley_votes > winning_votes:
		winning_votes = otooley_votes
		winner = "O'Tooley"
	else:
		pass
# output
output_information = (
	f"\nElection Results\n"
	f"\n----------------------------\n"
	f"\nTotal Votes: {total_votes}\n"
	f"\n----------------------------\n"
	f"\nKhan: {khan_percentage}% ({khan_votes})\n"
	f"\nCorrey: {correy_percentage}% ({correy_votes})\n"
	f"\nLi: {li_percentage}% ({li_votes})\n"
	f"\nO'Tooley: {otooley_percentage}% ({otooley_votes})\n"
	f"\n----------------------------\n"
	f"\nWinner: {winner}\n"
	f"\n----------------------------\n"
	)
print(output_information)
# exports outlet to text file
with open(output_path,"w",newline = '') as txt_output_file:
	txt_output_file.write(output_information)	
