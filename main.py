import random

print("Welcome to Akhil, Sandeep, and Ethan's Feature Selection Algorithm.\n")
numOfFeatures = int(input("Please enter total number of features: "))
print("\n")

print("Type the number of the algorithm you want to run.\n")
print("1. Forward Selection\n2. Backward Elimination\nBertie's Special Algorithm\n")
algorithmChoice = int(input())
print("\n")

randomVal = str(round(random.uniform(0, 100), 1))
print("Using no features and \"randon\" evalution, I get an accuracy of " + randomVal + "%\n")

if algorithmChoice == 1:
    print()
elif algorithmChoice == 2:
    print()
elif algorithmChoice == 3:
    print()

