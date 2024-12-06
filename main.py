import random
from forwardSelection import forwardsSelection
from backwardselection import backwardSelection

print("Welcome to Akhil, Sandeep, and Ethan's Feature Selection Algorithm.\n")
numOfFeatures = str(input("Please enter total number of features: "))
print("\n")

print("Type the number of the algorithm you want to run.\n")
print("1. Forward Selection\n2. Backward Elimination\n3. Bertie's Special Algorithm\n")
algorithmChoice = int(input())
print("\n")

if algorithmChoice == 1:
    forwardsSelection(numOfFeatures) 
elif algorithmChoice == 2:
    backwardSelection(numOfFeatures)
elif algorithmChoice == 3:
    print()