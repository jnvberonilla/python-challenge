# First import the os module
# This creates file paths across OS
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')



with open(csvpath,"r") as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
    data = list(reader)
    total_months = (len(data) - 1)

#print (total_months)


# Calculate Revenue Change
with open (csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #header
    header = next(csvreader)

    #lists?
    profit = []
    profit_change = []

    for row in csvreader:
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])

increase = max(profit_change)
decrease = min(profit_change)

month_increase = profit_change.index(max(profit_change))
month_decrease = profit_change.index(min(profit_change))


print ("Financial Analysis")
print ("-----------------------------------------")
print ("Total Months: " + str(total_months))
print (f"Total: ${sum(profit)}")
print (f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
#print (f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
#print (f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")  

output = open("output.txt", "w")
line1 = ("Financial Analysis")
line2 = ("-----------------------------------------")
line3 = ("Total Months: " + str(total_months))
line4 = (f"Total: ${sum(profit)}")
line5 = (f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
#line6 = (f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
#line7 = (f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")
output.write('{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5))