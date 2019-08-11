import os
import csv

csvpath = os.path.join('.','Resources','budget_data.csv')
count=0 
total=float(0)
total_dif=float(0)
max_month=""
max=0
min_month=""
min=0

with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     
     #read head
     #print(csvreader)
     csv_header = next(csvreader)
     
     #first row

     row = next(csvreader)
     i1=float(row[1])
     #print(row[0]+" "+row[1]+" "+str(i1))
     #count first row
     count= count+1
     total = total+i1

     #from second row
     for row in csvreader:
         x = float(row[1])
    
         count = count+1
         total = total+x
         
         #diffence compared to previous month
         i1=x-i1
         total_dif=total_dif+i1
         #print(str(count)+" "+row[0]+" "+str(x)+" "+str(total_dif))
         
         
         #max
         if (i1>=max):
             max=i1
             max_month=row[0]
             
         #min
         if (i1<=min):
             min=i1
             min_month=row[0]      
         
         #assign value to compare for next period
         i1=x     
 

#output
with open("PyBank_Output.txt", "w") as text_file:

  print("Financial Analysis", file=text_file)
  print("----------------------------", file=text_file)       
  print("Total Months: "+str(count), file=text_file)
  print("Total: "+"${:.0f}".format(total), file=text_file)
  print("Average  Change: "+"${:.2f}".format(total_dif/(count-1)), file=text_file) 
  print("Greatest Increase in Profits: "+max_month+" "+"("+"${:.0f}".format(max)+")", file=text_file)
  print("Greatest Decrease in Profits: "+min_month+" "+"("+"${:.0f}".format(min)+")", file=text_file)

