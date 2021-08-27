import os
import csv
#Open and Read the csv file
budget_data = os.path.join("..","python-challenge","budget_data.csv")
 #Create lists
months =[]
total_change = []

count_months = 0
currmnth_Profit_loses = 0
total_profit_loss = 0
firsttime = 0
prevmnth_profit_loss = 0
profit_loss_change = 0

sum_profit_loss_change = 0
averge_profit_loss = 0
highest_increase = 0
highest_decrease = 0

with open(budget_data,encoding='utf-8-sig') as csv_file:
      csv_reader = csv.reader(csv_file,delimiter=",")
      #Read the header row
      csv_header = next(csv_file)
      #Read through each row in the sheet
      for row in csv_reader:
          count_months = count_months + 1
          #Net amount of total profit/Losses over entire period
          currmnth_Profit_loses = int(row[1])
          total_profit_loss = total_profit_loss + currmnth_Profit_loses
          if (firsttime == 0):
              prevmnth_profit_loss = currmnth_Profit_loses
              firsttime = 1
          else:
              #Calculate change of profit and losses over the entire period
              profit_loss_change = currmnth_Profit_loses-prevmnth_profit_loss
              total_change.append(profit_loss_change)
              prevmnth_profit_loss = currmnth_Profit_loses
              months.append(row[0])
              
              
                           

#Sum of the total change of profit and loss
sum_profit_loss_change = sum(total_change)
             
#Average of the profit/Loss change
averge_profit_loss =  round((sum_profit_loss_change/count_months -1 ),2)
#Find highest increase
highest_increase = max(total_change)
highest_decrease = min(total_change)
#Find the index value of highest and lowest 
highest_index = total_change.index(highest_increase)
lowest_index = total_change.index(highest_decrease)
#Assign the months
highest_month = months[highest_index]
lowest_month = months[lowest_index]




print("Financial Analysis")
print("------------")
print(f"Total Months : {str(count_months)}")
print(f"Net Total : ${str(total_profit_loss)}")
print(f"Average Change : ${averge_profit_loss}")
print(f"Greatest Increase in Profits : {highest_month} $({highest_increase})")
print(f"Greatest Decrease in Losses : {lowest_month} ${(highest_decrease)}")


#Exporting to output file
output = open("Output.txt","w")
line1 = "Financial Analysis"
line2 = "------------"
line3 = str(f"Total Months : {str(count_months)}")
line4 = str(f"Net Total : ${str(total_profit_loss)}")
line5 = str(f"Average Change : ${averge_profit_loss}")
line6 = str(f"Greatest Increase in Profits : {highest_month} $({highest_increase})")
line7 = str(f"Greatest Decrease in Losses : {lowest_month} ${(highest_decrease)}")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3,line4,line5, line6,line7))





              






          
          



            


            




          



          

          

          










