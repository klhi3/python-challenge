import os
import csv

csvpath = os.path.join('.','Resources','election_data.csv')
#csvpath = os.path.join('.','Resources','test.csv')


#assign first values
count=0 

candidate=[]
total_vote=[]

#read file
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     
     #read head
     #print(csvreader)
     csv_header = next(csvreader)
     
     #first row
     row = next(csvreader)
     candidate.append(row[2])
     total_vote.append(1)
     count=1

     #from second row
     for row in csvreader:
    
         count = count+1

         idx = candidate.index(row[2]) if row[2] in candidate else -1
                 
         if idx == -1 :
            candidate.append(row[2])
            total_vote.append(1)           
         else:
            total_vote[idx]=total_vote[idx]+1
        
#print(candidate)
#print(total_vote) 
#print(count)
 
result_vote = dict(zip(candidate,total_vote))
#print(result_vote)

#output
with open("PyPoll_Output.txt", "w") as text_file:
  
  print("Election Result", file=text_file)
  print("----------------------------", file=text_file)       
  print("Total Votes: "+str(count), file=text_file)
  print("----------------------------", file=text_file)       
 
  max=0
  winner=""
  for x in result_vote:
    print(x+": "+str("{:.3f}%".format(result_vote[x]/count*100))+" ("+str(result_vote[x])+")", file=text_file)
    if (result_vote[x]>max):
        winner=x
        max=result_vote[x]

  print("----------------------------", file=text_file) 
  print("Winner: "+winner, file=text_file)
  print("----------------------------", file=text_file) 

