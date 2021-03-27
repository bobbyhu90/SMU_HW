import csv
import statistics as st


# Requirements
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


total_month = 0 
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
total_net = 0

file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_month = total_month + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # The total number of months included in the dataset       
        
         total_month = total_month + 1


        # # The net total amount of "Profit/Losses" over the entire period

         total_net = total_net + int(first_row[1])
         net_change = int(row[1]) - previous_net
         previous_net = int(row[1])
         net_change_list = net_change_list + [net_change]
         month_of_change = month_of_change + [row[0]]

# The greatest increase in profits (date and amount) over the entire period

         if net_change > greatest_increase[1]:
             greatest_increase[0] = row[0]
             greatest_increase[1] = net_change


# The greatest decrease in losses (date and amount) over the entire period


         if net_change < greatest_decrease[1]:
             greatest_decrease[0] = row[0]
             greatest_decrease[1] = net_change

net_monthly_average = sum(net_change_list)/len(net_change_list)

# print results
print("Financial Analysis")
print("------------------------------------------------------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total Profits: ${total_net}")
print(f"Average Change: ${net_monthly_average }")
print(f"Greatest Increase in Profits:" + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
print(f"Greatest Decrease in Profits:" + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
print("------------------------------------------------------------------------------------------") 
