# imports
import os
import csv
# establishing paths
csv_path = os.path.join('bank_data.csv')
output_path = os.path.join("output.txt")
# establishing variables to help with organization
total_months = 0
net_pl = 0
total_months_two = 0
first_iteration = True
previous_pl = 0
current_pl = 0
difference_pl = 0
difference_pl_list = []
avg_change = 0
greatest_increase_date = 0
greatest_increase_amount = 0
greatest_decrease_date = 0
greatest_decrease_amount = 0
# csv reader
with open(csv_path,newline = '') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter = ',')
	next(csv_reader,None)
# loops that find the total months, total profit/loss, greatest increase in profit/loss, and greatest decrease in profit/loss
	for row in csv_reader:
		total_months += 1
		net_pl += float(row[1])
# if statement created to skip one iteration because we cannot calculate the difference in profit/loss on the first iteration (nothing to subtract)
		if first_iteration:
			first_iteration = False
		else:
			current_pl = float(row[1])
			difference_pl = current_pl - previous_pl
			difference_pl_list.append(difference_pl)
# if statement to find the greatest increase and decrease in profit/loss
			if difference_pl > greatest_increase_amount:
				greatest_increase_amount = difference_pl
				greatest_increase_date = row[0]
			elif difference_pl < greatest_decrease_amount:
				greatest_decrease_amount = difference_pl
				greatest_decrease_date = row[0]
			else:
				pass 
		previous_pl = float(row[1])
# calculates average change
avg_change = sum(difference_pl_list) / (total_months-1)
# output
output_information = (
	f"\nFinancial Analysis\n"
	f"\n----------------------------\n"
	f"\nTotal Months: {total_months}\n"
	f"\nTotal: ${net_pl}\n"
	f"\nAverage Change: ${avg_change}\n"
	f"\nGreatest Increase in Profits: ${greatest_increase_amount} in {greatest_increase_date}\n"
	f"\nGreatest Decrease in Profits: ${greatest_decrease_amount} in {greatest_decrease_date}\n"
	)
print(output_information)
# exports outlet to text file
with open(output_path,"w",newline = '') as txt_output_file:
	txt_output_file.write(output_information)	