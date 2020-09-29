#PyBank
#import budget data 
import os
import csv 

bankpath=os.path.join('Resources','Budget_Data.csv')

analysis_file = os.path.join('Analysis','Cloud_analysis_output.txt')
analysis_output = open(analysis_file, 'w')

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
  
 #Revenue 
    rev_int = map(int,rev)
    total_revenue = (sum(rev_int))

 #Avg Change
    i = 0
    for i in range(len(rev) - 1):
        profit_loss = int(rev[i+1]) - int(rev[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
   
    monthly_change = Total / len(revenue_change)
    
#Greatest Increase
    profit_increase = max(revenue_change)
 
    profitgains = revenue_change.index(profit_increase)
    month_increase = month[profitgains+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
   
    profitloss = revenue_change.index(profit_decrease)
    month_decrease = month[profitloss+1]

Avg_total = round(float(monthly_change),2)
total_month = len(month)

#Print Statements

print(f'Financial Analysis')
analysis_output.write('Financial Analysis \n')
print(f"---------------------------")
analysis_output.write('---------------------------')
print(f'Total Months:   {total_month} \n')
analysis_output.write(f'\nTotal Months: {total_month} \n')
print(f"Total Revenue: $ " + str(total_revenue)) 
analysis_output.write(f'Total Revenue: {total_revenue} \n')
print(f"Average monthly change: $" + str(Avg_total))
analysis_output.write(f'Average monthly change: $ {Avg_total} \n')
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
analysis_output.write(f'Greatest Increase in Profits: {month_increase} (${profit_increase}) \n')
print(f'Greatest Decrease in Revenue: {month_decrease} (${profit_decrease})')
analysis_output.write(f'Greatest Decrease in Revenue: {month_decrease} (${profit_decrease}) \n')