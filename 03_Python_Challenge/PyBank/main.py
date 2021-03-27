#imports all the libaries 
import os
import csv

#Create variables for all the data
month = 0
month_list = []
change_list =[]
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
total = 0

csvpath = os.path.join ("Resources", "budget_data.csv")

#code for opening the files and reading it
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    first = next(csvreader)
    month += 1
    previous = int(first[1])
    total = total + int(first[1])
    
#loop for adding all the things in each row for each data
    for row in csvreader:
        
        month +=  1
        total = total + int(first[1])
        change = int(row[1]) - previous
        previous = int(row[1])
        change_list = change_list + [change]
        month_list = month_list + [row[0]]

        #finding the greatest increase
        if change > greatest_increase[1]:

            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        
        #finding out the greates decrease
        elif change < greatest_decrease[1]:

            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
#average 
average = sum(change_list)/len(change_list)


#Financial Analysis
 # ----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)


#print all the data 
print("")
print("Financial Analysis")
print("------------------")
print("Total Months: ", month)
print("Total: $", total)
print("Average Change: $", round(average, 2))
print(f"Greatest Increase in Profits:" + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
print(f"Greatest Decrease in Profits:" + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

#writing all the data as a txt file called "financial_analysis"
with open('financial_analysis.txt', "w") as text: 
    text.write("Financial Analysis\n")
    text.write("------------------------------------------------------------------------------------------")
    text.write(f"Total Months: {month}\n")
    text.write(f"Total Profits: ${total}\n")
    text.write(f"Average Change: ${average }\n") 
    text.write(f"Greatest Increase in Profits:" + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")\n")
    text.write(f"Greatest Decrease in Profits:" + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")\n")
    text.write("------------------------------------------------------------------------------------------")
