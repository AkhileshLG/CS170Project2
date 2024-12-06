import random
import itertools
from loaddata import load_dataset
from NNclassifier import NNClassifier
from validator import Validator

def forwardsSelection(datasetpath):
    features, labels = load_dataset(datasetpath)
    
    randomVal = str(round(random.uniform(50, 100), 1))
    print("Using no features and \"random\" evaluation, I get an accuracy of " + randomVal + "%\n")
    
    overallMaxAccuracy = str(0)
    maxValue = str(0)
    maxIndex = str(0)
    featureLst = []
    resultLst = []
    bestLst = []
    numOfFeatures = int(numOfFeatures)
    
    for i in range(0, numOfFeatures):
        featureLst.append(i + 1)
    
    print("Beginning Search.\n")

    for i in range(0, numOfFeatures):
        maxAccuracy = str(0)
        for j in range(0, len(featureLst)):
            if len(resultLst) == 0:
                tempAccuracy = str(round(random.uniform(30, 60), 1))
                print("     Using feature(s) {" + str(featureLst[j]) + "} arruracy is " + tempAccuracy + "%\n")
            elif len(resultLst) != 0:
                tempAccuracy = str(round(random.uniform(60, 100), 1))
                print("     Using feature(s) {" + ','.join(resultLst) + "," + str(featureLst[j]) + "} arruracy is " + tempAccuracy + "%\n")
            
            if maxAccuracy <= tempAccuracy:
                maxAccuracy = tempAccuracy
                maxValue = str(featureLst[j])
                maxIndex = j

        resultLst.append(maxValue)
        featureLst.pop(maxIndex)

        if overallMaxAccuracy <= maxAccuracy:
            bestLst = resultLst.copy()
            overallMaxAccuracy = str(maxAccuracy)

        if len(featureLst) != 0:
            print("Feature set {" + ','.join(resultLst) + "} was best, accuracy is " + maxAccuracy + "%\n")
        elif len(featureLst) == 0:
            if overallMaxAccuracy <= maxAccuracy:
                print("Feature set {" + ','.join(resultLst) + "} was best, accuracy is " + maxAccuracy + "%\n")
            elif overallMaxAccuracy > maxAccuracy:
                print("Warning, Accuracy has decreased!)")
                print("Feature set {" + ','.join(bestLst) + "} was best, accuracy is " + overallMaxAccuracy + "%\n")