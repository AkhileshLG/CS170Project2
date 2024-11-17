import random
from forwardSelection import pathPrint

print("Welcome to Akhil, Sandeep, and Ethan's Feature Selection Algorithm.\n")
numOfFeatures = str(input("Please enter total number of features: "))
print("\n")

print("Type the number of the algorithm you want to run.\n")
print("1. Forward Selection\n2. Backward Elimination\nBertie's Special Algorithm\n")
algorithmChoice = int(input())
print("\n")

randomVal = str(round(random.uniform(50, 100), 1))
print("Using no features and \"randon\" evaluation, I get an accuracy of " + randomVal + "%\n")

if algorithmChoice == 1:
    pathPrint(numOfFeatures)
elif algorithmChoice == 2:
    print()
elif algorithmChoice == 3:
    print()

