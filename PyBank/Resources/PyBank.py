#PyBank
#import budget data 
import os
import csv 

bankpath=os.path.join('..','Resources','Budget_Data.csv')

with open(bankpath) as bankfile:
    bankreader = csv.reader(bankfile, delimiter=',')
    #print(bankreader)

    bank_header = next(bankreader)
    month = []
    rev = []
    revenue_change = []
    monthly_change = []
    
    #print(f"Header: {bank_header}")               

#Months       
    for row in bankreader:
        month.append(row[0])
        rev.append(row[1])
    #print(len(month))
    
 #Revenue 
    rev_int = map(int,rev)
    total_revenue = (sum(rev_int))
    #print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(rev) - 1):
        profit_loss = int(rev[i+1]) - int(rev[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    #print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    profitgains = revenue_change.index(profit_increase)
    month_increase = month[profitgains+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    profitloss = revenue_change.index(profit_decrease)
    month_decrease = month[profitloss+1]

#Print Statements
output(
print(f'Financial Analysis')
print("Total Months: " + str(len(month)))
print("Total Revenue: $ " + str(total_revenue)) 
print("Average monthly change: $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)
