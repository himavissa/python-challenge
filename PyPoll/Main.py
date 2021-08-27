import os
import csv
election_result = os.path.join("..","python-challenge","election_data.csv")

uniquecandidates = []
total_votes = 0
num_of_votes = []
#A list to contain all the percentages of votes of each candidate
percent_votes = []


with open(election_result,encoding='utf-8-sig') as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=",")
      #Read the header row
      csv_header = next(csv_file)
      for row in csv_reader:
          #Total votes cast
          total_votes = total_votes + 1
          # --- get unique candidate names and individual vote counts and store in lists ---
        # if the first candidate is not in the list check condition and add to the list
          
          if row[2] not in uniquecandidates:
              uniquecandidates.append(row[2])
              index = uniquecandidates.index(row[2])
              #Add 1 to vote count
              num_of_votes.append(1)
              
          else:
              #get the index if the candidate and increase vote count
              index = uniquecandidates.index(row[2])
              num_of_votes[index] = num_of_votes[index] + 1
        #Calculate percentajge votes for each candidate

print("Election Results")
print("-----------------------")

print(f"Total Votes: {str(total_votes)}")


for i in range(len(uniquecandidates)):
    percentage = (num_of_votes[i]/total_votes) * 100
    percentage = round(percentage,2)
    percent_votes.append(percentage)
    print(f"{uniquecandidates[i]}:{str(percent_votes[i])}% ({str(num_of_votes[i])})")
    print("-----------------------")
     #Find winning candidate and print Output
    winner = max(num_of_votes)
    index = num_of_votes.index(winner)
    winning_candidate = uniquecandidates[index]
    print("Winner :",str(winning_candidate))

    #exporting to Output file
    output = open("Output.txt","w")
    line1 = "Election Results"
    line2 = "--------------------------"
    line3 = str(f"Total Votes: {str(total_votes)}")
    line4 = str("--------------------------")
    output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
    for i in range(len(uniquecandidates)):
        percentage = (num_of_votes[i]/total_votes) * 100
        percentage = round(percentage,2)
        percent_votes.append(percentage)
        line5= str(f"{uniquecandidates[i]}:{str(percent_votes[i])}% ({str(num_of_votes[i])})")
        output.write('{}\n'.format(line5))
        line6 = "-----------------------"
     #Find winning candidate and print Output
        winner = max(num_of_votes)
        index = num_of_votes.index(winner)
        winning_candidate = uniquecandidates[index]
        line7 = str(f"Winner: {winning_candidate}")
        line8 = "--------------------------"
        output.write('{}\n{}\n{}\n'.format(line5, line6, line7,line8))







      
    
    
      






      