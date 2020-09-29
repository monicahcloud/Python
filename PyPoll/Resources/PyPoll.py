import os
import csv
#Iterate
candidates = []
number_votes = 0
vote_counts = []
election_data = ['1', '2']

#Data path is to election data called [election_data.csv](PyRoll/Resources/election_data.csv).
# Start For Loop through file
for files in election_data:
    pypoll = csvpath = os.path.join("PyPoll CSV.csv")
      
#Split the data on commas since that is your delimiter
    with open(pypoll) as pypollfile:
       pypollreader = csv.reader(pypollfile, delimiter=',')
       line = next(pypollreader,None)
        # Using Nested For Loop
       for line in pypollreader:        

            #Establish vote count
            number_votes = number_votes +1
            
            # Establish Candidate
            candidate = line[2]
          
            # add votes to candidate running total. HA a pun.
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1

                # Make new spot for candidate in list
            else:
                candidates.append(candidate)
                vote_counts.append(1)
               
    #Declare the other variables:
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    
    #Work out percentages and winner (in a For Loop)
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
   
    percentages = [round(i,2) for i in percentages]
    
    # Summary print test of election results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {number_votes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
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
    filewriter.write(f"Total Votes:  {number_votes}\n")
    filewriter.write("-----------------------------\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Winner:  {winner}\n")
    filewriter.write("-----------------------------\n")
    
    # Close the text file
    filewriter.close()