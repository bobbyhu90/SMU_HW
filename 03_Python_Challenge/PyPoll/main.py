#imports libaries
import os
import csv

#create variable needed
total_votes = int(0)
poll = {}
csvpath = os.path.join ("Resources", "election_data.csv")


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #calculate total votes
        total_votes += 1
        #add data to poll dictionary, each candidate gets a count of votes to them
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1


#Election Results
 # -------------------------
 # Total Votes: 3521001
 # -------------------------
 # Khan: 63.000% (2218231)
 #Correy: 20.000% (704200)
 #Li: 14.000% (492940)
 #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
#print total votes
print(
    "",
    "Election Results\n",
    "-------------------------\n", 
    "Total Votes:",total_votes, "\n",
    "-------------------------\n",
)
#calculate and print each candidate with percentage and number of votes to them
for candidate in poll:
    print(candidate, ":", round(poll[candidate]/total_votes*100, 1), "% (", poll[candidate], ")")
print("-------------------------")
#calculate and print winner of the election
for candidate in poll:
    if poll[candidate] >= total_votes/2:
        print("Winner:", candidate)


#write data in a seperate text file
with open('election_results.txt', "w") as text:
    text.write("\n")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Values:" + str(total_votes) + "\n")
    text.write("-------------------------\n")
    for candidate in poll:
        text.write(str(candidate) + ":" + str(round(poll[candidate]/total_votes*100 + 1)) + "% (" + str(poll[candidate]) + ")\n")
    text.write("-------------------------\n")
    for candidate in poll:
        if poll[candidate] >= total_votes/2:
           text.write("Winner:" + str(candidate))