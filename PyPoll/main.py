# Python Homework - PyPoll

import os
import csv
import numpy as np

# assign file to variable via os path, folder, file name
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

# assign output path for new file via os path, folder, file name
output_path = os.path.join("..", "output", "election_results.txt")

#Array of all data
pyPollData = []
#List array of only voter ID
voterID = []
# List array of only county
county = []
#list array of only canidates
candidates = []
# List array for outfile *** come back to this *** dict may be option
pyPollResultsPrinted = []

# Number of votes
totalVotes = 0


#----------------------------------------------#
# function to get unique values        
def uniqueOccurances(list):
    x = np.array(list)
    uniqueValues = (np.unique(x))
    return uniqueValues
#----------------------------------------------#
# function to count multiple list occurances, print and return results
def countOccurances(list1, list2):

    occurance = {}
    finalTally = []
    for i in range(len(list1)):      
        if list1[i] in list2:
            occuranceCount = list2.count(list1[i])
            tally = ('{0:<10} {1:>2} {2:>8} {3:>8} {4:>8}'.format(list1[i],":", "{:.3%}".format(occuranceCount/totalVotes), " -- Total Votes: ", occuranceCount))
            finalTally.append(tally)
            print(tally)
            
            
            occurance.update({list1[i]:occuranceCount})
        else:
            print("It's not on the list!")
            

    winner = max(occurance, key=occurance.get)
    print("----------------------------------------")        
    print("WINNER: ",max(occurance, key=occurance.get))     
    print("----------------------------------------") 
           
    return (finalTally, winner)
#----------------------------------------------#
def printResultstoFile(finalTally, winner):

    with open("pyPoll.txt", "w") as pyPollResults:
        pyPollResults.write("-----------------------------\n")
        pyPollResults.write("Election Results\n")
        pyPollResults.write("-----------------------------\n")
        pyPollResults.write("Total votes cast: {}\n".format(totalVotes))
        pyPollResults.write("-----------------------------\n")
        pyPollResults.write("Candidates receiving votes: {}, {}, {}, {}".format(*uniqueOccurances(candidates)))
        pyPollResults.write("\n\n")
        pyPollResults.write("Counties participating: {}, {}, {}, {}, {}".format(*uniqueOccurances(county)))
        pyPollResults.write("\n\n")
        pyPollResults.writelines(["%s\n" % row for row in finalTally])
        pyPollResults.write("\n----------------------------------------\n")   
        pyPollResults.write("WINNER: {}\n".format(winner))
        pyPollResults.write("----------------------------------------\n") 


#----------------------------------------------#


with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        #cnt += 1
        pyPollData.append(row)
        voterID.append([row][0][0])
        county.append([row][0][1])
        candidates.append([row][0][2])
        
   

#print(f"pyPollData: {pyPollData[:10]}")        
#print(f"Voter ID: {voterID[:10]}")
#print(f"County: {county[:10]}")
#print(f"Canidates: {canidates[:50]}")

totalVotes = len(pyPollData)

print("-----------------------------")
print("Election Results")
print("-----------------------------")
print("Total votes cast: ", totalVotes)
print("-----------------------------\n")
print("Canidates receiving votes: {}, {}, {}, {}".format(*uniqueOccurances(candidates)))
print()
print("Counties participating: {}, {}, {}, {}, {}".format(*uniqueOccurances(county)))
print()
            
# ------------------------------------------------------------

finalTally, winner = countOccurances((uniqueOccurances(candidates)), candidates)

printResultstoFile(finalTally, winner)