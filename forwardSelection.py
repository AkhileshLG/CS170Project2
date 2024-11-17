import random

def pathPrint(numOfFeatures):
    maxAccuracy = str(0)
    featureLst = []
    resultLst = []
    
    for i in numOfFeatures:
        featureVal = i + 1
        featureLst.append(featureVal)

    while len(featureLst) != 0:
        i = 0
        for i in len(featureLst):
            tempAccuracy = str(round(random.uniform(50, 100), 1))
            print("Using feature(s) \{" + featureLst[i] + "\} accuracy is " + tempAccuracy)

            if maxAccuracy <= tempAccuracy:
                maxAccuracy = tempAccuracy