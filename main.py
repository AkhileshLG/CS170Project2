import random
from forwardSelection import pathPrint
from backwardselection import backwardSelection
print("Welcome to Akhil, Sandeep, and Ethan's Feature Selection Algorithm.\n")
numOfFeatures = str(input("Please enter total number of features: "))
print("\n")

print("Type the number of the algorithm you want to run.\n")
print("1. Forward Selection\n2. Backward Elimination\nBertie's Special Algorithm\n")
algorithmChoice = int(input())
print("\n")

randomVal = str(round(random.uniform(50, 100), 1))
print("Using no features and \"randon\" evaluation, I get an accuracy of " + randomVal + "%\n")

maxAccuracy = str(0)
featureLst = []
result = []
featureLstInput = 1
maxValue = 1

for i in numOfFeatures:
    featureLst.append(featureLstInput)
    featureLstInput += 1

if algorithmChoice == 1:
    while len(featureLst) != 0:
        for x in featureLst:
            currentVal = str(x)
            tempAccuracy = str(round(random.uniform(50, 100), 1))
            print("Using feature(s) \{" + currentVal + "\} accuracy is " + tempAccuracy)

            if maxAccuracy <= tempAccuracy:
                maxAccuracy = tempAccuracy
                maxValue = currentVal
        
        result.append(maxValue)
        featureLst.remove(maxValue)
            
elif algorithmChoice == 2:
    backwardSelection(numOfFeatures)
elif algorithmChoice == 3:
    print()