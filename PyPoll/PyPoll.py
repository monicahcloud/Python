import os
import csv

candidates = []
votes = 0
votecount = []
polldata = ['1', '2']


# Start For Loop through file
for files in polldata:
    pypoll = csvpath = os.path.join("PyPoll CSV.csv")
      
    with open(pypoll) as pypollfile:
       pypollreader = csv.reader(pypollfile, delimiter=',')
       line = next(pypollreader,None)
       
       for line in pypollreader:        
            votes = votes +1
            candidate = line[2]
          
            # add votes to candidate running total.
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                votecount[candidate_index] = votecount[candidate_index] + 1

            
            else:
                candidates.append(candidate)
                votecount.append(1)
               
    #Declare the other variables:
    percentages = []
    max_votes = votecount[0]
    max_index = 0
    
    #Work out percentages and winner (in a For Loop)
    for count in range(len(candidates)):
        vote_percentage = votecount[count]/votes*100
        percentages.append(vote_percentage)
        if votecount[count] > max_votes:
            max_votes = votecount[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
   
    percentages = [round(i,2) for i in percentages]
    
   
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {votes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({votecount[count]})")
    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")

    #Export file name and open as text file
    output_file = pypoll[0:-4]
    write_pypoll = f"{output_file}pypoll_results.txt"
    filewriter = open(write_pypoll, mode = 'w')
    
    # Write results to export text file
    filewriter.write("Election Results\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Total Votes:  {votes}\n")
    filewriter.write("-----------------------------\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]}% ({votecount[count]})\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Winner:  {winner}\n")
    filewriter.write("-----------------------------\n")
    
    # Close the text file
    filewriter.close()