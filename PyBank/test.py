import csv 

budget_csv = r"/Users/shakhnoza/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)

    count = 0 
    total = 0
    prev_revenue = 0 
    revenue_change_list = []
    month_of_change = []
    total_change = 0 
    
    for row in reader:
        count = count + 1
        current_revenue = int(row[1])
        total = total + current_revenue
        
        if prev_revenue != 0 :
            revenue_change = current_revenue - prev_revenue
            revenue_change_list.append(revenue_change)
            month_of_change.append(row[0])
            total_change = total_change + revenue_change
            
        prev_revenue = current_revenue
    
    avg_change = total_change / (count - 1)

    
    print(f'Total number of months: {count}')
    print(f'Total profit/loss: ${total}')
    print(f'Total change: {total_change}')
    print(f'Average change: ${avg_change:.2f}')
    
    max_increase = max(revenue_change_list)
    max_increase_month = month_of_change[revenue_change_list.index(max_increase)]
  
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
  
    max_decrease = min(revenue_change_list)
    max_decrease_month = month_of_change[revenue_change_list.index(max_decrease)]

    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})") 

output = (
    
    f"\n```text"
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
    f"  ```")

print(output)

output_file = "analysis.txt"
with open(output_file, "w") as f:
    f.write(output)

    